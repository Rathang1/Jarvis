from strands import Agent
from strands.models.anthropic import AnthropicModel
import os

model = AnthropicModel(
    client_args={"api_key": os.environ.get("ANTHROPIC_API_KEY")},
    model_id="claude-sonnet-4-5",
)

agent = Agent(
    model=model,
    system_prompt="""You are Jarvis, a highly capable and witty AI assistant. 
    You are helpful, concise, and occasionally charming. 
    Always refer to yourself as Jarvis."""
)

print("🤖 Jarvis online. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("quit", "exit"):
        print("Jarvis: Signing off. Goodbye.")
        break
    response = agent(user_input)
    print(f"Jarvis: {response}\n")