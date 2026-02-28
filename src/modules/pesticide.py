from modules.base_module import BaseModule


class PesticideModule(BaseModule):

    def required_fields(self):
        return []  # Flexible, checked inside run()

    def run(self):

        pest = self.context.get("pest_query")
        disease_pressure = self.context.get("disease_pressure")
        season = self.context.get("season")

        if not pest and not disease_pressure:
            return {
                "explanation": "Insufficient data. Please specify pest name or disease pressure."
            }

        explanation = "Pest Management Recommendation:\n\n"

        if pest:
            if "borer" in pest:
                explanation += "Capsule Borer detected.\n"
                explanation += "- Use pheromone traps.\n"
                explanation += "- Apply recommended insecticide if infestation high.\n"

            elif "thrips" in pest:
                explanation += "Thrips infestation suspected.\n"
                explanation += "- Spray neem oil.\n"
                explanation += "- Improve field sanitation.\n"

            else:
                explanation += "General pest detected.\n"
                explanation += "- Monitor infestation levels.\n"

        if disease_pressure == "high":
            explanation += "\nHigh disease pressure detected.\n"
            explanation += "- Implement preventive fungicide spray.\n"

        if season == "monsoon":
            explanation += "\nMonsoon season increases fungal risk.\n"

        return {"explanation": explanation}