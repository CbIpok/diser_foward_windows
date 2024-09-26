import os
import re



import config
from run import Experiment, get_files_with_extension
import shutil
from database import FileDatabase
set_path = r"\\Dmitrienko-1064.sl.iae.nsk.su\share\set_3"
def run(wave):
    db = FileDatabase()
    share_folder = 'share'
    bathes = get_files_with_extension(set_path, "bath")
    bath = bathes[0]
    relative_path_bath = bath.split(share_folder, 1)[-1]
    # Удалим начальный слеш, если он присутствует
    relative_path_bath = relative_path_bath.lstrip('\\/')
    if not os.path.exists(os.path.dirname(relative_path_bath)):
        os.makedirs(os.path.dirname(relative_path_bath))
    shutil.copy(bath,relative_path_bath)

    relative_path_wave = wave.split(share_folder, 1)[-1]
    # Удалим начальный слеш, если он присутствует
    relative_path_wave = relative_path_wave.lstrip('\\/')
    if not os.path.exists(os.path.dirname(relative_path_wave)):
        os.makedirs(os.path.dirname(relative_path_wave))
    shutil.copy(wave, relative_path_wave)


    exp = Experiment(f"{set_path}/info.json",  relative_path_bath, relative_path_wave,
                     "data")
    exp.init_json()
    exp.run()
    exp.save_max_height(f"dat.txt")
    exp.save_subduction_zone(f"out.nc")
    db.save_files(bath, wave, f"dat.txt", f"out.nc")

pattern = re.compile(r'square_center_basis_(\d+)\\-700_basis_(\d+).wave')
def sort_key(file):
    match = pattern.search(file)
    if match:
        i = int(match.group(1))  # Значение i
        j = int(match.group(2))  # Значение j
        return (i, j)
    return (0, 0)


if __name__ == "__main__":
    waves = get_files_with_extension(set_path, "wave")
    bathes = get_files_with_extension(set_path, "bath")
    print(*sorted(waves,key=sort_key),sep="\n")
    output_file = 'server_client/sorted_files.txt'

    # Открываем файл на запись
    with open(output_file, 'w') as f:
        for file in sorted(waves,key=sort_key):
            f.write(file + '\n')
            # run(bathes[0],waves[0],)


