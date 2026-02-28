from modules.base_module import BaseModule


class IrrigationModule(BaseModule):

    def required_fields(self):
        return ["num_plants", "water_availability", "budget"]

    def run(self):

        num_plants = self.context.get("num_plants")
        water = self.context.get("water_availability")
        budget = self.context.get("budget")

        if num_plants is None or water is None or budget is None:
            return {
                "explanation": "Insufficient data. Please provide number of plants, water availability, and budget."
            }

        explanation = "Irrigation Recommendation:\n\n"
        scores = {}

        # Base Scoring
        scores["Drip"] = 0
        scores["Sprinkler"] = 0
        scores["Manual"] = 0

        # Water availability impact
        if water == "low":
            scores["Drip"] += 3
            scores["Sprinkler"] += 1
        elif water == "medium":
            scores["Drip"] += 2
            scores["Sprinkler"] += 2
        elif water == "high":
            scores["Sprinkler"] += 3
            scores["Manual"] += 2

        # Budget impact
        if budget == "low":
            scores["Manual"] += 3
        elif budget == "medium":
            scores["Sprinkler"] += 2
        elif budget == "high":
            scores["Drip"] += 3

        # Farm size logic
        if num_plants > 200:
            scores["Drip"] += 2
        elif num_plants < 50:
            scores["Manual"] += 2

        # Rank
        ranking = sorted(scores.items(), key=lambda x: x[1], reverse=True)

        for method, score in ranking:
            explanation += f"- {method}: Score {score}\n"

        explanation += "\nDecision based on water availability, budget, and farm size."

        return {"explanation": explanation}