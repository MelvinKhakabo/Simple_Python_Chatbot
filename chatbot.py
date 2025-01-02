import json

# File to store chatbot knowledge
KNOWLEDGE_FILE = "chatbot_knowledge.json"

# Load chatbot knowledge from file
def load_knowledge():
    try:
        with open(KNOWLEDGE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save chatbot knowledge to file
def save_knowledge(knowledge):
    with open(KNOWLEDGE_FILE, "w") as file:
        json.dump(knowledge, file, indent=4)

# Chatbot function to handle interaction
def chatbot():
    print("Simple Chatbot")
    print("Type 'exit' to end the chat.\n")
    knowledge = load_knowledge()

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("Chatbot: Goodbye!")
            break
        if user_input in knowledge:
            print(f"Chatbot: {knowledge[user_input]}")
        else:
            print("Chatbot: I don't know the answer to that.")
            new_response = input("Can you teach me how to respond to this? (yes/no): ").strip().lower()
            if new_response == "yes":
                response = input("What should I say? ").strip()
                knowledge[user_input] = response
                save_knowledge(knowledge)
                print("Chatbot: Thank you! I've learned something new.")

# Main entry point
if __name__ == "__main__":
    chatbot()
