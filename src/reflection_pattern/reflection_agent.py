from anthropic import Anthropic
import os
from dotenv import load_dotenv
from .prompts import ReflectionPrompts, ReflectionTemplates, ReflectionConfig

load_dotenv()

class ReflectionAgent:
    def __init__(self, api_key: str = None, model: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model or ReflectionConfig.MODEL
        self.prompts = ReflectionPrompts()
        self.templates = ReflectionTemplates()
    
    def generate(self, task: str) -> str:
        """Generate initial code based on the task"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            system=self.prompts.GENERATOR_SYSTEM,
            messages=[
                {"role": "user", "content": self.templates.GENERATE_TASK.format(task=task)}
            ]
        )
        return response.content[0].text
    
    def reflect(self, task: str, code: str) -> str:
        """Critique and analyze the generated code"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            system=self.prompts.REFLECTOR_SYSTEM,
            messages=[
                {"role": "user", "content": self.templates.REFLECT_ON_CODE.format(code=code)}
            ]
        )
        return response.content[0].text
    
    def refine(self, task: str, code: str, critique: str) -> str:
        """Improve the code based on reflection feedback"""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            system=self.prompts.REFINER_SYSTEM,
            messages=[
                {"role": "user", "content": self.templates.REFINE_CODE.format(
                    code=code, critique=critique
                )}
            ]
        )
        return response.content[0].text
    
    def run(self, task: str) -> dict:
        """Run the complete reflection cycle and return all outputs"""
        print(f"Starting reflection cycle for: {task}")
        
        # Generate initial code
        print("Generating initial code...")
        initial_code = self.generate(task)
        
        # Reflect on the code
        print("Reflecting on code...")
        critique = self.reflect(task, initial_code)
        
        # Refine based on reflection
        print("Refining code...")
        refined_code = self.refine(task, initial_code, critique)
        
        print("Reflection cycle complete!")
        
        return {
            "task": task,
            "initial_code": initial_code,
            "critique": critique,
            "refined_code": refined_code
        }
    
    