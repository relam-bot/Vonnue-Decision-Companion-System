from src.modules.base_module import BaseModule


class LabourModule(BaseModule):

    def required_fields(self):
        return ["num_plants"]

    def field_prompt(self, field):
        if field == "num_plants":
            return "Enter number of plants (example: 100):"

    def parse_and_store(self, field, user_input, context_manager):
        if field == "num_plants":
            try:
                context_manager.update({"num_plants": int(user_input)})
            except:
                pass

    def run(self):

        plants = self.context.get("num_plants")

        workers_needed = max(1, plants // 75)

        summary = "Labour Requirement Analysis\n\n"
        summary += f"Total Plants: {plants}\n"
        summary += f"Recommended Workers: {workers_needed}\n\n"

        if plants <= 20:
            summary += "Small farm. 1 worker sufficient.\n"
        elif plants <= 200:
            summary += "Moderate farm size. Plan structured work schedule.\n"
        else:
            summary += "Large farm. Consider permanent labour team.\n"

        return {
            "summary": summary
        }
