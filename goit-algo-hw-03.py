import os
import shutil
import argparse


def copy_files(source_dir, dest_dir):
    # Перебираємо всі елементи у вихідній директорії
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            # Отримуємо розширення файлу
            _, extension = os.path.splitext(file)
            # Перевіряємо, чи існує піддиректорія з назвою розширення
            dest_subdir = os.path.join(dest_dir, extension[1:])  # Відкидаємо крапку в початку розширення
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)  # Створюємо піддиректорію, якщо вона не існує
            # Копіюємо файл у відповідну піддиректорію
            shutil.copy2(file_path, dest_subdir)


def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(description='Copy files recursively and sort them by extension.')
    parser.add_argument('source_dir', type=str, help='path to the source directory')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='path to the destination directory (default is "dist")')
    args = parser.parse_args()

    # Перевірка наявності директорії призначення
    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)  # Створюємо директорію призначення, якщо вона не існує

    # Копіювання файлів та сортування їх за розширенням
    copy_files(args.source_dir, args.dest_dir)


if __name__ == "__main__":
    main()
