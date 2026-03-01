from src.modules.base_module import BaseModule


class SoilModule(BaseModule):

    def required_fields(self):
        return ["soil_ph", "soil_drainage"]

    def field_prompt(self, field):
        prompts = {
            "soil_ph": "Enter soil pH value (example: 5.8):",
            "soil_drainage": "Enter drainage condition (poor / moderate / good):"
        }
        return prompts[field]

    def parse_and_store(self, field, user_input, context_manager):

        if field == "soil_ph":
            context_manager.update({"soil_ph": float(user_input)})

        elif field == "soil_drainage":
            context_manager.update({"soil_drainage": user_input.lower()})

    def run(self):

        ph = self.context["soil_ph"]
        drainage = self.context["soil_drainage"]

        score = 100
        summary = "Soil Health Assessment\n\n"

        if 5.5 <= ph <= 6.5:
            summary += "pH is optimal for cardamom.\n"
        elif ph < 5.5:
            summary += "Soil is acidic.\n"
            score -= 15
        else:
            summary += "Soil slightly alkaline.\n"
            score -= 10

        if drainage == "poor":
            summary += "Poor drainage detected.\n"
            score -= 20
        elif drainage == "moderate":
            summary += "Moderate drainage.\n"
        else:
            summary += "Good drainage.\n"

        summary += f"\nSoil Suitability Score: {score}/100\n"

        return {"summary": summary}
