from conversation_manager import ConversationManager


def main():
    manager = ConversationManager()

    print("🌿 Welcome to Cardamom Farmer Assistant")
    print(manager.module_menu())

    while True:
        user_input = input("You: ")

        response = manager.process_input(user_input)
        print("Assistant:", response)

        if user_input.lower() == "exit":
            break


if __name__ == "__main__":
    main()
