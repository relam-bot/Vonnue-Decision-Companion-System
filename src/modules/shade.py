from src.modules.base_module import BaseModule


class ShadeModule(BaseModule):

    def required_fields(self):
        return ["shade_percent"]

    def field_prompt(self, field):
        return "Enter shade percentage (example: 45):"

    def parse_and_store(self, field, user_input, context_manager):
        context_manager.update({"shade_percent": int(user_input)})

    def run(self):

        shade = self.context["shade_percent"]
        summary = "Shade Requirement Analysis\n\n"

        if shade < 40:
            summary += "Insufficient shade. Risk of sun stress.\n"
        elif 40 <= shade <= 60:
            summary += "Optimal shade for healthy growth.\n"
        else:
            summary += "Excess shade. Risk of fungal diseases.\n"

        return {"summary": summary}
