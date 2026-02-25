import json
import os

class VectorMemory:
    def __init__(self, file_path="memory_system/long_term.db"):
        self.file_path = file_path
        self.memory_data = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        return {}

    def store(self, key, value):
        self.memory_data[key] = {
            "content": value,
            "timestamp": str(os.times()[4]) # توقت افتراضي للبيئة
        }
        with open(self.file_path, 'w') as f:
            json.dump(self.memory_data, f, indent=4)
        print(f"[VectorMemory] Data stored under key: {key}")

    def retrieve(self, key):
        return self.memory_data.get(key, "No memory found.")

if __name__ == "__main__":
    vm = VectorMemory()
    vm.store("identity", "I am Niko, a self-evolving AI.")
    print(f"Retrieved Identity: {vm.retrieve('identity')}")


