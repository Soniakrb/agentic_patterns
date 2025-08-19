
from anthropic import Anthropic
import os
from dotenv import load_dotenv
from .planingPrompts import PlaningPrompts
from .planingTemplates import PlaningTemplates, PlaningConfig

load_dotenv()


class PlaningAgent:
   
    
    def __init__(self, api_key: str = None, model: str = None):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model or PlaningConfig.MODEL
        self.prompts = PlaningPrompts()
        self.templates = PlaningTemplates()
        self.config = PlaningConfig()
    
    def plan(self, task: str, project_type: str = "web_app", complexity: str = "medium") -> str:
        # Initial plan
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1500,
            system=self.prompts.PLANNER_SYSTEM,
            messages=[
                {"role": "user", "content": self.templates.PLAN_TASK.format(
                    task=task,
                    project_type=self.config.PROJECT_TYPES.get(project_type, project_type),
                    complexity=self.config.COMPLEXITY_LEVELS.get(complexity, complexity)
                )}
            ]
        )
        return response.content[0].text
    
    def validate(self, task: str, plan: str) -> str:
        # Validate and improve the plan
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1500,
            system=self.prompts.VALIDATOR_SYSTEM,
            messages=[
                {"role": "user", "content": self.templates.VALIDATE_PLAN.format(
                    task=task,
                    plan=plan
                )}
            ]
        )
        return response.content[0].text
    
    def organize(self, task: str, validated_plan: str) -> str:
        # Organize plan for execution
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1500,
            system=self.prompts.EXECUTOR_SYSTEM,
            messages=[
                {"role": "user", "content": self.templates.ORGANIZE_EXECUTION.format(
                    task=task,
                    validated_plan=validated_plan
                )}
            ]
        )
        return response.content[0].text
    
    def simple_plan(self, task: str) -> str:
        # Create a simple plan without validation steps
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            system=self.prompts.PLANNER_SYSTEM,
            messages=[
                {"role": "user", "content": self.templates.SIMPLE_PLAN.format(task=task)}
            ]
        )
        return response.content[0].text
    
    def run(self, task: str, project_type: str = "web_app", complexity: str = "medium", detailed: bool = True) -> dict:
        # Run the complete planning cycle
        print(f"Creating development plan for: {task}")
        
        if not detailed:
            # Simple planning mode
            print("Generating simple plan...")
            plan = self.simple_plan(task)
            return {
                "task": task,
                "final_plan": plan,
                "mode": "simple"
            }
        
        # Detailed planning mode
        print("Generating initial plan...")
        initial_plan = self.plan(task, project_type, complexity)
        
        print("Validating and improving plan...")
        validated_plan = self.validate(task, initial_plan)
        
        print("Organizing for execution...")
        execution_plan = self.organize(task, validated_plan)
        
        print("Planning complete!")
        
        return {
            "task": task,
            "project_type": project_type,
            "complexity": complexity,
            "initial_plan": initial_plan,
            "validated_plan": validated_plan,
            "execution_plan": execution_plan,
            "mode": "detailed"
        }

# Test
if __name__ == "__main__":
    agent = PlaningAgent()
    
    # Test with different types of applications
    test_cases = [
        {
            "task": "Build a fitness tracking app for teenagers",
            "project_type": "fitness",
            "complexity": "medium"
        },
        {
            "task": "Create an educational math game for kids aged 6-10",
            "project_type": "kids_app", 
            "complexity": "simple"
        },
        {
            "task": "Develop a social recipe sharing platform",
            "project_type": "social_app",
            "complexity": "complex"
        }
    ]
    
    for test_case in test_cases:
        task = test_case["task"]
        print(f"\n{'='*60}")
        print(f"PLANNING: {task}")
        print(f"Type: {test_case['project_type']} | Complexity: {test_case['complexity']}")
        print(f"{'='*60}")
        
        try:
            result = agent.run(
                task=task,
                project_type=test_case["project_type"],
                complexity=test_case["complexity"],
                detailed=False  # Simple mode for testing
            )
            print(result['final_plan'])
        except Exception as e:
            print(f"Error: {e}")
        
        print()
        