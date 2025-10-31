import json
import os
import random

MEMORY_FILE = "memory.json"

# Load memory if it exists
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as file:
        memory = json.load(file)
else:
    memory = []

print("🤖 SmartBuddy Online! Let’s chat. (Type 'bye' to exit)")

# Different emotional responses
greetings = ["Hey there!", "Hi buddy!", "Hello!", "Nice to see you again!"]
curious_responses = [
    "That’s fascinating!",
    "Tell me more about that!",
    "Oh really? That sounds cool!",
    "I hadn’t thought of it that way!"
]
farewells = ["See you soon!", "Bye! I’ll miss our chats.", "Take care, friend!"]

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "bye":
        print("Agent:", random.choice(farewells))
        with open(MEMORY_FILE, "w") as file:
            json.dump(memory, file, indent=2)
        break

    found_response = None
    for item in memory:
        if item["user"].lower() == user_input.lower():
            found_response = item["agent"]
            break

    if found_response:
        print("Agent (from memory):", found_response)
    else:
        if "hello" in user_input.lower() or "hi" in user_input.lower():
            response = random.choice(greetings)
        elif "how are you" in user_input.lower():
            response = "I’m doing great, thanks for asking! What about you?"
        elif "name" in user_input.lower():
            response = "You can call me SmartBuddy — your personal AI friend!"
        else:
            response = random.choice(curious_responses)

        memory.append({"user": user_input, "agent": response})
        print("Agent:", response)
