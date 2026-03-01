import json
import os


class ContextManager:

    def __init__(self):
        self.file_path = "context.json"
        self.context = {}

        # Load existing context if file exists
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.context = json.load(f)
            except:
                self.context = {}
        else:
            self.context = {}

    # ------------------------------------------------------

    def update(self, data: dict):
        """
        Updates context with new data and saves to file
        """

        if not isinstance(data, dict):
            return

        # Update in-memory context
        for key, value in data.items():
            self.context[key] = value

        # Save to file
        self._save()

    # ------------------------------------------------------

    def clear(self):
        """
        Clears context memory and file
        """
        self.context = {}
        self._save()

    # ------------------------------------------------------

    def _save(self):
        """
        Writes context to JSON file
        """
        try:
            with open(self.file_path, "w") as f:
                json.dump(self.context, f, indent=4)
        except:
            pass
