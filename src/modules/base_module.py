class BaseModule:

    def __init__(self, context):
        self.context = context

    def required_fields(self):
        return []

    def field_prompt(self, field):
        return f"Please provide {field}:"

    def parse_and_store(self, field, user_input, context_manager):
        context_manager.update({field: user_input})

    def run(self):
        raise NotImplementedError("Each module must implement run().")
