import os
import shutil
import argparse


def copy_files(source_dir, dest_dir):
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        if os.path.isdir(item_path):
            # Рекурсивно викликаємо функцію для директорії
            copy_files(item_path, dest_dir)
        elif os.path.isfile(item_path):
            # Отримуємо розширення файлу
            _, extension = os.path.splitext(item)
            # Створюємо піддиректорію для копіювання
            dest_subdir = os.path.join(dest_dir, extension[1:])
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            # Копіюємо файл у відповідну піддиректорію
            shutil.copy2(item_path, dest_subdir)


def main():
    parser = argparse.ArgumentParser(description='Copy files recursively and sort them by extension.')
    parser.add_argument('source_dir', type=str, help='path to the source directory')
    parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='path to the destination directory (default is "dist")')
    args = parser.parse_args()

    if not os.path.exists(args.dest_dir):
        os.makedirs(args.dest_dir)

    copy_files(args.source_dir, args.dest_dir)


if __name__ == "__main__":
    main()
