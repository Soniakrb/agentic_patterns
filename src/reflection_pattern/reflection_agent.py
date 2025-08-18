from anthropic import Anthropic
import os

from dotenv import load_dotenv

load_dotenv()

anthropic = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))



class ReflectionAgent:
    def generate(self, task: str) -> str:
        response = anthropic.messages.create(
            model="claude-3-5-sonnet-20240620",
            messages=[
                {"role": "user", "content": task}
            ]
        )
        return response.content[0].text
    
    def reflect(self, task: str, response: str) -> str:
        response = anthropic.messages.create(
            model="claude-3-5-sonnet-20240620",
            messages=[
                {"role": "user", "content": task}
            ]
        )
        return response.content[0].text
    
    def refine(self, task: str, response: str) -> str:  
        response = anthropic.messages.create(
            model="claude-3-5-sonnet-20240620",
            messages=[
                {"role": "user", "content": task}
            ]
        )
        return response.content[0].text
    
    def run(self, task: str) -> str:
        response = self.generate(task)
        response = self.reflect(task, response)
        response = self.refine(task, response)
        return response
    
    