from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

print("=== Hiba AI Assistant ===")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "You are Hiba's helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        print("\nAssistant:", response.choices[0].message.content)
        print()

    except Exception as e:
        print("Error:", e)