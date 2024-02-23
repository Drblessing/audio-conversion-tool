from pathlib import Path
import os


def move_files_to_top_level(folder_path):
    folder_path = Path(folder_path)
    for folder in folder_path.iterdir():
        if folder.is_dir():
            for file in folder.iterdir():
                if file.is_file():
                    new_path = folder_path / file.name
                    file.rename(new_path)
            os.rmdir(folder)


def remove_string_from_files(folder_path, string):
    folder_path = Path(folder_path)
    for file in folder_path.iterdir():
        if file.is_file():
            new_name = file.name.replace(string, "")
            file.rename(folder_path / new_name)


if __name__ == "__main__":
    folder_path = ""
    # remove_string_from_files(folder_path, "")
