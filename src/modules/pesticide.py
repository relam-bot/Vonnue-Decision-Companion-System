from src.modules.base_module import BaseModule


class PesticideModule(BaseModule):

    def required_fields(self):
        return ["pest_query"]

    def field_prompt(self, field):
        return "Describe pest problem (example: capsule borer / aphids / leaf spot):"

    def parse_and_store(self, field, user_input, context_manager):
        context_manager.update({"pest_query": user_input.lower()})

    def run(self):

        pest = self.context["pest_query"]
        summary = "Pest Management Recommendation\n\n"

        if "capsule borer" in pest:
            summary += "Capsule Borer detected.\n"
            summary += "- Install pheromone traps.\n"
            summary += "- Remove infected capsules.\n"
            summary += "- Apply insecticide if severe.\n"

        elif "aphid" in pest:
            summary += "Aphid infestation.\n"
            summary += "- Use neem oil spray.\n"

        else:
            summary += "General pest detected.\n"
            summary += "- Monitor closely.\n"
            summary += "- Follow integrated pest management.\n"

        return {"summary": summary}
