from modules.base_module import BaseModule


class SoilModule(BaseModule):

    def required_fields(self):
        # Minimum required
        return ["soil_ph", "soil_drainage"]

    def run(self):

        soil_ph = self.context.get("soil_ph")
        drainage = self.context.get("soil_drainage")
        organic = self.context.get("organic_matter")

        if soil_ph is None or drainage is None:
            return {
                "explanation": "Insufficient data. Please provide soil pH and drainage condition."
            }

        explanation = ""
        suitability_score = 100

        # ------------------------------
        # pH Analysis
        # ------------------------------
        if 5.5 <= soil_ph <= 6.5:
            explanation += "Soil pH is optimal.\n"
        elif soil_ph < 5.5:
            explanation += "Soil is acidic.\n"
            suitability_score -= 15
        else:
            explanation += "Soil is slightly alkaline.\n"
            suitability_score -= 10

        # ------------------------------
        # Drainage Analysis
        # ------------------------------
        if drainage == "poor":
            explanation += "Poor drainage detected.\n"
            suitability_score -= 20
        elif drainage == "moderate":
            explanation += "Moderate drainage.\n"
        elif drainage == "good":
            explanation += "Good drainage.\n"

        # ------------------------------
        # Organic Matter
        # ------------------------------
        if organic == "low":
            explanation += "Organic matter is low.\n"
            suitability_score -= 10

        explanation += f"\nSoil Suitability Score: {suitability_score}/100\n"

        return {"explanation": explanation}