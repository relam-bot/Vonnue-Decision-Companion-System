import json
import os

DATA_FILE = "farm_data.json"

class ContextManager:
    def __init__(self):
        self.context = {}
        self.load_context()

    def load_context(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                try:
                    self.context = json.load(f)
                except:
                    self.context = {}
        else:
            self.context = {}

    def save_context(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.context, f, indent=4)

    def update(self, new_data: dict):
        self.context.update(new_data)
        self.save_context()

    def get(self, key):
        return self.context.get(key)

    def clear(self):
        self.context = {}
        if os.path.exists(DATA_FILE):
            os.remove(DATA_FILE)