from context_manager import ContextManager
from validation import validate_data
from gemini_service import extract_intent_and_entities

from modules.irrigation import IrrigationModule
from modules.fertilizer import FertilizerModule
from modules.pesticide import PesticideModule
from modules.soil import SoilModule
from modules.shade import ShadeModule
from modules.variety import VarietyModule
from modules.labour import LabourModule


class ConversationManager:

    def __init__(self):
        self.context_manager = ContextManager()
        self.active_module = None
        self.last_result = None

        self.module_map = {
            "irrigation": IrrigationModule,
            "fertilizer": FertilizerModule,
            "pesticide": PesticideModule,
            "soil": SoilModule,
            "shade": ShadeModule,
            "variety": VarietyModule,
            "labour": LabourModule
        }

    # ----------------------------------------
    # MAIN INPUT PROCESSOR
    # ----------------------------------------

    def process_input(self, user_input: str):

        user_input = user_input.strip().lower()

        if user_input == "exit":
            return "Goodbye 🌿"

        if user_input in ["why", "why?", "explain"]:
            return self.handle_explanation()

        # ----------------------------------------
        # If user selects module directly
        # ----------------------------------------

        if user_input in self.module_map:
            self.active_module = user_input
            return self.check_required_fields()

        # ----------------------------------------
        # Use Gemini Extraction
        # ----------------------------------------

        extracted = extract_intent_and_entities(user_input)

        if not extracted:
            return "Please specify what you want help with (irrigation, soil, fertilizer, etc.)."

        validated = validate_data(extracted)
        self.context_manager.update(validated)

        module_name = extracted.get("module")

        if module_name and module_name in self.module_map:
            self.active_module = module_name

        if not self.active_module:
            return "Please specify what you want help with (irrigation, soil, fertilizer, etc.)."

        return self.check_required_fields()

    # ----------------------------------------
    # CHECK REQUIRED FIELDS BEFORE EXECUTION
    # ----------------------------------------

    def check_required_fields(self):

        module_class = self.module_map[self.active_module]
        module_instance = module_class(self.context_manager.context)

        for field in module_instance.required_fields():
            if field not in self.context_manager.context:
                return f"Please provide {field.replace('_', ' ')}."

        return self.execute_module()

    # ----------------------------------------
    # EXECUTE MODULE
    # ----------------------------------------

    def execute_module(self):

        module_class = self.module_map[self.active_module]
        module_instance = module_class(self.context_manager.context)

        result = module_instance.run()
        self.last_result = result

        return result.get("summary") or result.get("explanation")

    # ----------------------------------------
    # EXPLANATION LAYER
    # ----------------------------------------

    def handle_explanation(self):

        if not self.last_result:
            return "No decision available to explain."

        explanation = "\nDETAILED DECISION EXPLANATION\n\n"

        if "top_choice" in self.last_result:
            explanation += f"Top Recommendation: {self.last_result['top_choice']}\n\n"

        if "positive_factors" in self.last_result:
            explanation += "Positive Factors:\n"
            for item in self.last_result["positive_factors"]:
                explanation += f"- {item}\n"

        if "negative_factors" in self.last_result:
            explanation += "\nNegative Factors:\n"
            for item in self.last_result["negative_factors"]:
                explanation += f"- {item}\n"

        if "context_used" in self.last_result:
            explanation += "\nContext Used:\n"
            for k, v in self.last_result["context_used"].items():
                explanation += f"- {k}: {v}\n"

        return explanation