from src.modules.base_module import BaseModule


class VarietyModule(BaseModule):

    def required_fields(self):
        return ["rainfall_level", "altitude"]

    def field_prompt(self, field):
        prompts = {
            "rainfall_level": "Enter rainfall level (low / medium / high):",
            "altitude": "Enter altitude type (lowland / mid / highland):"
        }
        return prompts[field]

    def parse_and_store(self, field, user_input, context_manager):
        context_manager.update({field: user_input.lower()})

    def run(self):

        rainfall = self.context["rainfall_level"]
        altitude = self.context["altitude"]

        summary = "Cardamom Variety Recommendation\n\n"

        if rainfall == "high" and altitude == "highland":
            summary += "Recommended: Malabar variety.\n"

        elif rainfall == "medium":
            summary += "Recommended: Mysore variety.\n"

        else:
            summary += "Recommended: Vazhukka variety.\n"

        return {"summary": summary}
