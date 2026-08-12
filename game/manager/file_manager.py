import json
from pathlib import Path

class FileManager:
    def read_json(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write_json(self, file_path, data):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
    def file_exists(self, file_path):
        return Path(file_path).is_file()