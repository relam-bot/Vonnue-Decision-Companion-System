from modules.base_module import BaseModule


class LabourModule(BaseModule):

    def required_fields(self):
        return ["num_plants", "labour_availability"]

    def run(self):

        num_plants = self.context.get("num_plants")
        labour = self.context.get("labour_availability")
        growth_stage = self.context.get("growth_stage")
        budget = self.context.get("budget")
        terrain = self.context.get("terrain")

        if num_plants is None or labour is None:
            return {
                "explanation": "Insufficient data. Please provide number of plants and labour availability."
            }

        explanation = "Labour Planning Recommendation:\n\n"

        # ------------------------------
        # Basic Labour Requirement Logic
        # ------------------------------

        if num_plants <= 50:
            base_need = "low"
        elif 50 < num_plants <= 200:
            base_need = "medium"
        else:
            base_need = "high"

        explanation += f"Estimated Labour Requirement: {base_need}\n"

        # ------------------------------
        # Compare With Available Labour
        # ------------------------------

        if labour == "low" and base_need in ["medium", "high"]:
            explanation += "\n⚠ Labour shortage risk detected.\n"
            explanation += "- Consider temporary workers during peak season.\n"

        elif labour == "medium" and base_need == "high":
            explanation += "\nModerate labour pressure expected.\n"
            explanation += "- Plan task scheduling carefully.\n"

        else:
            explanation += "\nLabour availability is adequate.\n"

        # ------------------------------
        # Growth Stage Impact
        # ------------------------------

        if growth_stage == "flowering":
            explanation += "\nFlowering stage requires close monitoring and skilled labour.\n"

        elif growth_stage == "harvest":
            explanation += "\nHarvest stage is labour-intensive.\n"

        # ------------------------------
        # Terrain Impact
        # ------------------------------

        if terrain == "steep":
            explanation += "\nSteep terrain increases manual labour demand.\n"

        # ------------------------------
        # Budget Consideration
        # ------------------------------

        if budget == "low" and labour == "low":
            explanation += "\nLow budget + low labour may reduce productivity.\n"

        explanation += "\nDecision based on farm size and labour availability."

        return {"explanation": explanation}