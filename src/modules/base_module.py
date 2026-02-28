class BaseModule:

    def __init__(self, context):
        self.context = context

    # Default: no required fields
    def required_fields(self):
        return []

    def run(self):
        raise NotImplementedError("Each module must implement run().")