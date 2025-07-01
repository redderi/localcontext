import os
import platform
import logging


logger = logging.getLogger(__name__)

skip_dir = {"venv", ".venv", "env", ".env", "__pycache__", ".git"}

class FileManager:
    def __init__(self, output_filename):
        self.__output_filename = output_filename

    def find_os_information(self):
        return f"ОС: {platform.system()}\nСборка ОС {platform.platform()}\n"
           
    def find_project_tree(self, path=".", prefix=""):
        contents = sorted(os.listdir(path))
        tree = ""
        for i, item in enumerate(contents):
            is_last = (i == len(contents) - 1)
            branch = "└── " if is_last else "├── "
            tree += f"{prefix}{branch}{item}\n"
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path) and item not in skip_dir:
                extension = "    " if is_last else "│   "
                tree += self.find_project_tree(item_path, prefix + extension)
        return tree
    
    def find_file_code(self, path=".", filename="localcontext.txt", line_number=None):
        abs_output_path = os.path.abspath(filename)
        contents = sorted(os.listdir(path))
        for item in contents:
            item_path = os.path.join(path, item)
            abs_item_path = os.path.abspath(item_path)
            logging.debug(f"Проверяется: {item_path}")

            if abs_item_path == abs_output_path:
                continue

            if os.path.isdir(item_path) and item not in skip_dir:
                self.find_file_code(item_path, filename, line_number)
            elif os.path.isfile(item_path):
                try:
                    with open(item_path, "r", encoding="utf-8") as current_file:
                        lines = current_file.readlines()
                        logging.debug(f"Файл прочитан: {item_path}")

                    with open(filename, "a", encoding="utf-8") as output_file:
                        logging.debug(f"Код добавлен в файл: {filename}")
                        output_file.write(f"\n\n# {item_path}\n")
                        for idx, line in enumerate(lines, start=1):
                            if line_number is not None:
                                num = str(idx).rjust(line_number, "0")
                                output_file.write(f"{num}: {line}")
                            else:
                                output_file.write(line)

                except UnicodeDecodeError:
                    logging.warning(f"Пропущен (не текстовый): {item_path}")
                except Exception as e:
                    logging.error(f"Ошибка при чтении {item_path}: {e}")
