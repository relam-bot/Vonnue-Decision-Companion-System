from modules.base_module import BaseModule


class ShadeModule(BaseModule):

    def required_fields(self):
        return ["shade_percent"]

    def run(self):

        shade = self.context.get("shade_percent")

        if shade is None:
            return {
                "explanation": "Insufficient data. Please provide shade percentage."
            }

        explanation = ""

        if 50 <= shade <= 60:
            explanation += "Shade level is optimal for cardamom.\n"
        elif shade < 50:
            explanation += "Shade is insufficient.\n"
            explanation += "Recommendation: Increase canopy cover.\n"
        else:
            explanation += "Excess shade detected.\n"
            explanation += "Recommendation: Thin canopy for better airflow.\n"

        explanation += "\nDecision based strictly on shade percentage."

        return {"explanation": explanation}