from modules.base_module import BaseModule


class FertilizerModule(BaseModule):

    def required_fields(self):
        # At least one of these must be present
        return []  # We validate manually in run()

    def run(self):

        leaf_symptom = self.context.get("leaf_symptom")
        soil_ph = self.context.get("soil_ph")
        nitrogen = self.context.get("nitrogen_level")
        phosphorus = self.context.get("phosphorus_level")
        potassium = self.context.get("potassium_level")

        # ------------------------------
        # Minimum Data Check
        # ------------------------------
        if not any([leaf_symptom, soil_ph, nitrogen, phosphorus, potassium]):
            return {
                "explanation": "Insufficient data. Please provide soil pH, nutrient levels, or leaf symptoms."
            }

        explanation = ""

        # ------------------------------
        # Symptom-based diagnosis
        # ------------------------------
        if leaf_symptom == "yellow":
            explanation += "Likely Nitrogen deficiency.\n"
            explanation += "Recommendation: Apply nitrogen-rich fertilizer.\n"

        elif leaf_symptom == "purple":
            explanation += "Possible Phosphorus deficiency.\n"
            explanation += "Recommendation: Apply phosphate fertilizer.\n"

        # ------------------------------
        # Soil pH logic
        # ------------------------------
        if soil_ph is not None:
            if soil_ph < 5.5:
                explanation += "Soil too acidic. Apply agricultural lime.\n"
            elif soil_ph > 6.5:
                explanation += "Soil slightly alkaline. Adjust fertilizer mix.\n"

        # ------------------------------
        # Nutrient Level Logic
        # ------------------------------
        if nitrogen == "low":
            explanation += "Nitrogen level is low.\n"
        if phosphorus == "low":
            explanation += "Phosphorus level is low.\n"
        if potassium == "low":
            explanation += "Potassium level is low.\n"

        return {"explanation": explanation}