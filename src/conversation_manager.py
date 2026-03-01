from src.context_manager import ContextManager

from src.modules.irrigation import IrrigationModule
from src.modules.fertilizer import FertilizerModule
from src.modules.pesticide import PesticideModule
from src.modules.soil import SoilModule
from src.modules.shade import ShadeModule
from src.modules.variety import VarietyModule
from src.modules.labour import LabourModule


class ConversationManager:

    def __init__(self):
        self.context_manager = ContextManager()
        self.active_module = None

        self.module_map = {
            "irrigation": IrrigationModule,
            "fertilizer": FertilizerModule,
            "pesticide": PesticideModule,
            "soil": SoilModule,
            "shade": ShadeModule,
            "variety": VarietyModule,
            "labour": LabourModule
        }

    # =========================================================

    def process_input(self, user_input: str):

        user_input = user_input.strip().lower()

        if user_input == "exit":
            return "Goodbye 🌿"

        if user_input == "reset":
            self.context_manager.clear()
            self.active_module = None
            return "All module data cleared."

        # ---------------- MODULE SELECTION ----------------

        if user_input in self.module_map:
            self.context_manager.clear()
            self.active_module = user_input
            return f"Switched to {user_input} module.\n" + self.ask_for_next_field()

        # ---------------- NO MODULE SELECTED ----------------

        if not self.active_module:
            return self.module_menu()

        # ---------------- HANDLE ACTIVE MODULE ----------------

        return self.handle_module_input(user_input)

    # =========================================================

    def module_menu(self):

        return (
            "Which topic would you like to explore next?\n"
            "- irrigation\n"
            "- fertilizer\n"
            "- pesticide\n"
            "- soil\n"
            "- shade\n"
            "- variety\n"
            "- labour\n"
            "(Type 'exit' to quit)\n"
        )

    # =========================================================

    def ask_for_next_field(self):

        module = self.module_map[self.active_module](self.context_manager.context)

        for field in module.required_fields():
            if field not in self.context_manager.context:
                return module.field_prompt(field)

        return self.execute_module()

    # =========================================================

    def handle_module_input(self, user_input):

        module = self.module_map[self.active_module](self.context_manager.context)

        for field in module.required_fields():
            if field not in self.context_manager.context:
                module.parse_and_store(field, user_input, self.context_manager)
                return self.ask_for_next_field()

        return self.execute_module()

    # =========================================================

    def execute_module(self):

        module = self.module_map[self.active_module](self.context_manager.context)
        result = module.run()

        # Clear after execution
        self.context_manager.clear()
        self.active_module = None

        return result["summary"] + "\n" + self.module_menu()
