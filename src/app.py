import os
import sys
from src.parser import Parser
from src.file_manager import FileManager

class App:
    def __init__(self):
        parser = Parser()
        self.__operations = parser.parse()
        self.__filename = self.__operations.get("filename") or "localcontext.txt"
        self.__fileManager = FileManager(self.__filename)

    def run(self):
        with open(self.__filename, "w", encoding="utf-8") as file:
            if self.__operations.get("system"):
                file.write("Система:\n")
                file.write(self.__fileManager.find_os_information())
                file.write("-----------\n")
            if self.__operations.get("tree"):
                file.write("Дерево проекта:\n")
                file.write(self.__fileManager.find_project_tree())
            file.write("-----------\n")
            file.write("code:")
        self.__fileManager.find_file_code(path=os.path.dirname(os.path.abspath(sys.argv[0])), 
                                          filename=self.__filename, 
                                          line_number = int(self.__operations["number"]) if self.__operations.get("number") else None)
        