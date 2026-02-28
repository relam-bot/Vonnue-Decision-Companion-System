from conversation_manager import ConversationManager

def main():
    manager = ConversationManager()

    print("🌿 Welcome to Cardamom Farmer Assistant")
    print("Type 'reset' to clear saved farm data.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye 🌿")
            break

        response = manager.process_input(user_input)
        print("Assistant:", response)


if __name__ == "__main__":
    main()