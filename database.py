import sqlite3


import os
import shutil

class FileDatabase:
    def __init__(self, base_directory=r"\\Dmitrienko-1064.sl.iae.nsk.su\share\set_4\dataStorage"):
        self.base_directory = base_directory
        if not os.path.exists(self.base_directory):
            os.makedirs(self.base_directory)

    def _sanitize_name(self, name):
        """Заменяет все косые черты на '!' в именах bath и wave"""
        return name.replace('/', '!').replace('\\', '!')

    def save_files(self, bath, wave, txt_file_path, nc_file_path):
        """Сохраняет файлы в папку bath с именем wave"""
        sanitized_bath = self._sanitize_name(bath)
        sanitized_wave = self._sanitize_name(wave)

        # Создаем путь для папки bath
        bath_dir = os.path.join(self.base_directory, sanitized_bath)
        if not os.path.exists(bath_dir):
            os.makedirs(bath_dir)

        # Путь для файлов
        txt_output_path = os.path.join(bath_dir, f'{sanitized_wave}.txt')
        nc_output_path = os.path.join(bath_dir, f'{sanitized_wave}.nc')

        # Копируем файлы
        shutil.copyfile(txt_file_path, txt_output_path)
        shutil.copyfile(nc_file_path, nc_output_path)
        print(f"Files saved to {txt_output_path} and {nc_output_path}")

    def load_files(self, bath, wave, txt_output_path, nc_output_path):
        """Загружает файлы по ключам bath и wave и сохраняет их на диск"""
        sanitized_bath = self._sanitize_name(bath)
        sanitized_wave = self._sanitize_name(wave)

        # Путь для файлов
        bath_dir = os.path.join(self.base_directory, sanitized_bath)
        txt_file_path = os.path.join(bath_dir, f'{sanitized_wave}.txt')
        nc_file_path = os.path.join(bath_dir, f'{sanitized_wave}.nc')

        if os.path.exists(txt_file_path) and os.path.exists(nc_file_path):
            shutil.copyfile(txt_file_path, txt_output_path)
            shutil.copyfile(nc_file_path, nc_output_path)
            print(f"Files loaded to {txt_output_path} and {nc_output_path}")
        else:
            print(f"No files found for bath={bath} and wave={wave}")

    def delete_files(self, bath, wave):
        """Удаляет файлы по ключам bath и wave"""
        sanitized_bath = self._sanitize_name(bath)
        sanitized_wave = self._sanitize_name(wave)

        # Путь для файлов
        bath_dir = os.path.join(self.base_directory, sanitized_bath)
        txt_file_path = os.path.join(bath_dir, f'{sanitized_wave}.txt')
        nc_file_path = os.path.join(bath_dir, f'{sanitized_wave}.nc')

        if os.path.exists(txt_file_path):
            os.remove(txt_file_path)
            print(f"Deleted {txt_file_path}")
        if os.path.exists(nc_file_path):
            os.remove(nc_file_path)
            print(f"Deleted {nc_file_path}")

        # Если папка bath пустая после удаления, удаляем её
        if not os.listdir(bath_dir):
            os.rmdir(bath_dir)
            print(f"Deleted empty directory {bath_dir}")

    def close(self):
        """Завершает работу (в данном случае нет необходимости в закрытии ресурсов)"""
        print("Operation complete, no database connection to close.")



if __name__ == "__main__":
    db = FileDatabase("/mnt/hgfs/shared/set_1.db")
    # db.save_files("1000","0","dat_1000.txt","out_1000.nc")
    db.load_files("1000", "0", "/mnt/hgfs/shared/dat_1000.txt", "/mnt/hgfs/shared/out_1000.nc")