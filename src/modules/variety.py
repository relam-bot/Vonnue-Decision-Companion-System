from modules.base_module import BaseModule


class VarietyModule(BaseModule):

    def required_fields(self):
        return ["rainfall_level", "altitude"]

    def run(self):

        rainfall = self.context.get("rainfall_level")
        altitude = self.context.get("altitude")
        disease = self.context.get("disease_pressure")
        market = self.context.get("market_priority")

        if rainfall is None or altitude is None:
            return {
                "explanation": "Insufficient data. Please provide rainfall level and altitude."
            }

        explanation = "Variety Recommendation:\n\n"
        scores = {
            "Malabar": 0,
            "Mysore": 0,
            "Vazhukka": 0
        }

        # Rainfall logic
        if rainfall == "high":
            scores["Malabar"] += 2
            scores["Vazhukka"] += 2
        elif rainfall == "medium":
            scores["Mysore"] += 2

        # Altitude logic
        if altitude == "highland":
            scores["Malabar"] += 2
        elif altitude == "mid":
            scores["Mysore"] += 2

        # Disease logic
        if disease == "high":
            scores["Vazhukka"] += 2

        # Market logic
        if market == "yield":
            scores["Mysore"] += 2
        elif market == "quality":
            scores["Malabar"] += 2

        ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        for variety, score in ranking:
            explanation += f"- {variety}: Score {score}\n"

        explanation += "\nDecision based on climate, altitude, disease pressure, and market preference."

        return {"explanation": explanation}