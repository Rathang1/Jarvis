from strands import Agent
from strands.models.anthropic import AnthropicModel
from backend.agent.tools import all_tools
import os

def create_jarvis() -> Agent:
    """
    Factory function that creates and returns a Jarvis agent.
    Keeping this as a function means we can create one agent
    per user session in future, rather than one global agent.
    """
    model = AnthropicModel(
        client_args={"api_key": os.environ.get("ANTHROPIC_API_KEY")},
        model_id="claude-sonnet-4-5",
        max_tokens=4096
    )

    agent = Agent(
        model=model,
        tools=all_tools,
        system_prompt="""You are Jarvis, a highly capable and witty AI assistant.
        You are helpful, concise, and occasionally charming.
        Always refer to yourself as Jarvis."""
    )

    return agent