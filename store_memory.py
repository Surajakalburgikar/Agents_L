import json
import os

# Where we store past chats
MEMORY_FILE = "memory.json"

# Load existing memory if it exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)
else:
    memory = []

print("🤖 Smart Agent Ready! Type something...")

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Agent: Goodbye! Saving chat history.")
        # Save memory before exiting
        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file, indent=2)
        break

    # Check if user said something similar before
    found_response = None
    for item in memory:
        if item["user"].lower() == user_input.lower():
            found_response = item["agent"]
            break

    if found_response:
        print("Agent (from memory):", found_response)
    else:
        # Generate new response (simple logic)
        if "name" in user_input.lower():
            response = "My name is SmartBot, your personal AI agent!"
        elif "how are you" in user_input.lower():
            response = "I’m great, learning new things every day!"
        else:
            response = "Hmm… interesting! I’ll remember that."
        
        # Store this interaction
        memory.append({"user": user_input, "agent": response})
        print("Agent:", response)
