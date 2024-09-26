import json
import os.path
import subprocess



import config
from config import save_stride
from database import FileDatabase


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
        json_template["bathymetry"]["file"] = self.bath_path

        json_template["run"]["name"] = self.name
        json_template["run"]["init-wave"]["file"] = self.wave_path
        json_template["run"]["output-dir"] = self.out_path
        json_template["run"]["save-stride"] = config.save_stride
        with open(self.json_experiment_path, "w") as json_experiment_file:
            json.dump(json_template,json_experiment_file,indent=4)

    def run(self):
        parameters = [self.json_experiment_path]
        subprocess.run([self.runner_path] + parameters)

    def save_max_height(self,filename):
        parameters = [os.path.abspath(f"{self.root_path}/{self.name}_h.nc"), "max_height", filename]
        subprocess.run([self.exporter_2d_path] + parameters)

    def save_subduction_zone(self,filename):
        y_min, y_max,x_min, x_max = [str(cord//config.save_stride) for cord in self.info["mariogramm_zone"]]
        # x_min, x_max, y_min, y_max = map(str,[0, self.info["size"][0]//save_stride, 0 ,self.info["size"][1]//save_stride])
        parameters = [os.path.abspath(f"{self.root_path}/{self.name}_h.nc"), x_min,
                      x_max, y_min, y_max, filename]
        print(parameters)
        subprocess.run([self.exporter_subduction_path] + parameters)


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

if __name__ == "__main__":
    db = FileDatabase("set_2.db")
    waves = get_files_with_extension(f"data/set_2", "wave")
    bathes = get_files_with_extension(f"data/set_2", "bath")
    print(waves)
    print(bathes)
    for bath in bathes:
        for wave in waves:
            exp = Experiment(f"data/set_2/info.json",bath,wave,"data")
            exp.init_json()
            exp.run()
            exp.save_max_height(f"dat.txt")
            exp.save_subduction_zone(f"out.nc")
            db.save_files(bath,wave,f"dat.txt",f"out.nc")
        pass