from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def streaming_chatbot_with_helpers_sync():
    green = '\033[32m'
    reset = '\033[0m'

    user_prompt = []
    total_input_tokens = 0
    total_output_tokens = 0
    last_usage = None

    while True:
        user_input = input("Enter a message: ")
        if user_input.lower() == "quit":
            print("\n\nSTREAMING IS DONE.  HERE IS THE FINAL ACCUMULATED MESSAGE: ")
            print(last_usage.to_json)
            print(f"total_input_tokens: {total_input_tokens}")
            print(f"total_output_tokens: {total_output_tokens}")
            break

        print("\n\n" + green + f"user_prompt: {user_input}" + reset)
        user_prompt.append({"role": "user", "content": user_input})

        stream = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            messages=user_prompt,
            stream=True
        )

        assistant_response = ""

        for chunk in stream:
            if chunk.type == "content_block_delta":
                content = chunk.delta.text
                print(content, end="", flush=True)
                user_prompt.append({"role": "assistant", "content": content})
                assistant_response += content
            elif chunk.type == "message_delta":
                print("\n")
                last_usage = chunk.usage
                total_input_tokens += last_usage.input_tokens
                total_output_tokens += last_usage.output_tokens

        user_prompt.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    streaming_chatbot_with_helpers_sync()