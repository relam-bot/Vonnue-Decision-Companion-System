from src.modules.base_module import BaseModule


class FertilizerModule(BaseModule):

    def required_fields(self):
        return ["leaf_symptom"]

    def field_prompt(self, field):
        return "Describe leaf symptom (example: yellow leaves / brown edges / curling):"

    def parse_and_store(self, field, user_input, context_manager):
        context_manager.update({"leaf_symptom": user_input.lower()})

    def run(self):

        symptom = self.context["leaf_symptom"]

        summary = "Fertilizer Diagnosis\n\n"

        if "yellow" in symptom:
            summary += "Likely Nitrogen deficiency.\n"
            summary += "Apply Urea in split doses.\n"

        elif "brown" in symptom:
            summary += "Likely Potassium deficiency.\n"
            summary += "Apply MOP fertilizer.\n"

        elif "curl" in symptom:
            summary += "Possible micronutrient deficiency.\n"
            summary += "Use micronutrient foliar spray.\n"

        else:
            summary += "Symptom unclear. Conduct soil testing.\n"

        return {"summary": summary}
