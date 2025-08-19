from anthropic
import os
from dotenv import load_dotenv

load_dotenv()

class Agent:
    def __init__(self, api_key: str = None, model: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model,
        self.prompts = AgentPrompts()
        self.templates = AgentTemplates()
        
    def run(self, user_query: str) -> str:
        messages = [{"role": "user", "content": user_query}]
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            system=self.prompts.INITIAL_SYSTEM,
        )