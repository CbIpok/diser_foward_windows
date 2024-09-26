from setuptools.depends import extract_constant

import config
from run import Experiment, get_files_with_extension

if __name__ == "__main__":
    waves = get_files_with_extension(f"{config.shared_folder}/set_2/basises/square_center_basis_2", "wave")
    bath = f"{config.shared_folder}/set_2/bathes/-700_1500_2000.bath"
    print(waves)

    exp = Experiment(f"{config.shared_folder}/set_2/info.json",bath,waves[0],"/home/mikhail/python/foward_auto/data/waves")
    exp.root_path = "data/temp"
    exp.out_path = "/home/mikhail/python/foward_auto/data/temp"
    exp.init_json()
    exp.run()
    exp.save_max_height(f"data/wave_{2}.txt")
    exp.save_subduction_zone(f"data/wave_{2}.nc")


