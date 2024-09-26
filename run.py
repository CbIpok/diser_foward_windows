import json
import os.path
import subprocess



import config
from config import save_stride
from database import FileDatabase


def windows_to_wsl_path(windows_path):
    """
    Преобразует путь Windows (локальный или сетевой UNC) в формат WSL.

    :param windows_path: Путь в формате Windows (например, C:\path\to\file.txt или \\server\shared_folder).
    :return: Строка с путем в формате WSL (например, /mnt/c/path/to/file.txt или /mnt/server/shared_folder).
    """
    # Проверяем, является ли путь UNC (сетевая папка)
    if windows_path.startswith('\\\\'):
        # Убираем двойной обратный слэш в начале UNC пути
        unc_path = windows_path[2:]
        # Заменяем обратные слэши на обычные
        wsl_path = unc_path.replace('\\', '/')
        # Добавляем /mnt/ перед преобразованным UNC путем
        return f"/mnt/{wsl_path}"

    # Проверяем, является ли путь локальным (например, C:\path\to\file.txt)
    elif ':' in windows_path:
        # Извлекаем букву диска
        drive_letter = windows_path[0].lower()  # Преобразуем букву диска в нижний регистр
        path = windows_path[2:]  # Убираем букву диска и двоеточие
        # Заменяем обратные слэши на обычные
        path = path.replace('\\', '/')
        # Формируем WSL путь
        return f"/mnt/{drive_letter}{path}"

    else:
        return windows_to_wsl_path(os.path.abspath(windows_path))

class Experiment:
    def __init__(self ,info_path ,bath_path ,wave_path, out_path):
        self.out_path = out_path
        self.wave_path = wave_path
        self.bath_path = bath_path
        self.name = "exp"
        self.root_path = "data"
        self.json_experiment_path = f"{self.root_path}/temp/template_exp.json"
        self.runner_path = f"{config.bin_folder_runner}/TsunamiRunner"
        self.exporter_2d_path = f"{config.bin_folder_export}/export_cdf/netcdf-exporter"
        self.exporter_subduction_path = f"{config.bin_folder_export}/export_cdf_surface/netcdf-exporter-surface"
        with open(info_path, "r") as json_template_file:
            self.info = json.load(json_template_file)


    def init_json(self):
        with open("data/template.json", "r") as json_template_file:
            json_template = json.load(json_template_file)

        json_template["bathymetry"]["width"] = self.info["size"][0]
        json_template["bathymetry"]["height"] = self.info["size"][1]
        json_template["bathymetry"]["file"] = windows_to_wsl_path(self.bath_path)

        json_template["run"]["name"] = self.name
        json_template["run"]["init-wave"]["file"] = windows_to_wsl_path(self.wave_path)
        json_template["run"]["output-dir"] = windows_to_wsl_path(self.out_path)
        json_template["run"]["save-stride"] = config.save_stride
        with open(self.json_experiment_path, "w") as json_experiment_file:
            json.dump(json_template,json_experiment_file,indent=4)

    def run(self):

        command = f"wsl {windows_to_wsl_path(os.path.abspath(self.runner_path))} {windows_to_wsl_path(os.path.abspath(self.json_experiment_path))}"
        result = subprocess.run(command)


    def save_max_height(self,filename):
        parameters = [os.path.abspath(f"{self.root_path}/{self.name}_h.nc"), "max_height", filename]
        command = f"wsl {windows_to_wsl_path(self.exporter_2d_path)} {windows_to_wsl_path(f'{self.root_path}/{self.name}_h.nc')} max_height {windows_to_wsl_path(filename)}"
        subprocess.run(command)

    def save_subduction_zone(self,filename):
        y_min, y_max,x_min, x_max = [str(cord//config.save_stride) for cord in self.info["mariogramm_zone"]]
        # x_min, x_max, y_min, y_max = map(str,[0, self.info["size"][0]//save_stride, 0 ,self.info["size"][1]//save_stride])
        parameters = [os.path.abspath(f"{self.root_path}/{self.name}_h.nc"), x_min,
                      x_max, y_min, y_max, filename]
        print(parameters)
        command = f"wsl {windows_to_wsl_path(self.exporter_subduction_path)} {windows_to_wsl_path(f'{self.root_path}/{self.name}_h.nc')} {x_min} {x_max} {y_min} {y_max} {windows_to_wsl_path(filename)}"
        subprocess.run(command)


def get_files_with_extension(directory, extension):
    """
    Возвращает список полных путей ко всем файлам с определенным расширением в указанной директории.
    """
    files_with_extension = []

    # Проходим по всем файлам и подкаталогам в указанной директории
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                files_with_extension.append(full_path)

    return files_with_extension


set_path = r"\\Dmitrienko-1064.sl.iae.nsk.su\share\set_3"


if __name__ == "__main__":
    db = FileDatabase()
    waves = get_files_with_extension(set_path, "wave")
    bathes = get_files_with_extension(set_path, "bath")
    print(waves)
    print(bathes)
    for bath in bathes:
        for wave in waves:
            exp = Experiment(f"D:\dmitrienkomy\python\diser_input\data\set_3/info.json",bath,wave,"data")
            exp.init_json()
            exp.run()
            exp.save_max_height(f"dat.txt")
            exp.save_subduction_zone(f"out.nc")
            db.save_files(bath,wave,f"dat.txt",f"out.nc")
        pass