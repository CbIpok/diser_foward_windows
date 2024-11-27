import os
import json
import re


# Функция для сортировки папок по шаблону *_i_j
def folder_sort_key(folder_name):
    match = re.match(r".*_(\d+)_(\d+)", folder_name)
    if match:
        return int(match.group(1)), int(match.group(2))
    return float('inf'), float('inf')


# Функция для сортировки файлов по шаблону *_i.wave
def file_sort_key(file_name):
    match = re.match(r".*_(\d+)\.wave", file_name)
    if match:
        return int(match.group(1))
    return float('inf')


# Путь к директории
base_dir = r"D:\dmitrienkomy\share\set_4\basises"

# Результирующий список JSON объектов
json_objects = []

# Получаем список папок
folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]
folders.sort(key=folder_sort_key)

# Проходим по каждой папке
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.wave')]

    # Сортируем файлы по шаблону *_i.wave
    files.sort(key=file_sort_key)

    # Создаем JSON объект для каждого файла
    for file in files:
        json_object = {
            "basis": folder,
            "file": file
        }
        json_objects.append(json_object)

# Преобразуем список в формат JSON
json_output = json.dumps(json_objects, indent=4)

# Выводим результат
print(json_output)

# При необходимости можно сохранить результат в файл
with open("server_client/output.json", "w") as json_file:
    json_file.write(json_output)
