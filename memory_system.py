import json
import os

class NikoMemory:
    def __init__(self):
        self.file_path = "user_data.json"
        self.data = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"user_name": "بشير"}

    def get_name(self):
        return self.data.get("user_name", "بشير")
