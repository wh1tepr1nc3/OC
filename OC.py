import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(directory)
        file_time = os.path.getmtime(directory)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(directory)
        parent_dir = os.path.dirname(directory)
        print(
            f'Обнаружен файл: {file}, Путь: {file_path}, '
            f'Размер: {file_size} байт, Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')
