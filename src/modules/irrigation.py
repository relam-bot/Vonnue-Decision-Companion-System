from src.modules.base_module import BaseModule


class IrrigationModule(BaseModule):

    def required_fields(self):
        return ["num_plants", "water_availability", "budget"]

    def field_prompt(self, field):
        prompts = {
            "num_plants": "Enter number of plants (example: 150):",
            "water_availability": "Enter water availability (low / medium / high):",
            "budget": "Enter budget level (low / medium / high):"
        }
        return prompts[field]

    def parse_and_store(self, field, user_input, context_manager):

        if field == "num_plants":
            context_manager.update({"num_plants": int(user_input)})

        elif field == "water_availability":
            context_manager.update({"water_availability": user_input})

        elif field == "budget":
            context_manager.update({"budget": user_input})

    def run(self):

        plants = self.context["num_plants"]
        water = self.context["water_availability"]
        budget = self.context["budget"]

        summary = "Irrigation Plan Recommendation\n\n"

        if plants <= 20:
            summary += "Recommended: Manual irrigation\n"
        elif water == "low":
            summary += "Recommended: Drip irrigation (water efficient)\n"
        elif water == "high" and budget == "high":
            summary += "Recommended: Sprinkler system\n"
        else:
            summary += "Recommended: Drip irrigation\n"

        summary += "\nDecision based on farm size, water, and budget."

        return {"summary": summary}
