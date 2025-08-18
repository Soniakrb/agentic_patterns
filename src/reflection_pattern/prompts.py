"""
Prompts for the Reflection Pattern Agent
"""

class ReflectionPrompts:
    """System prompts for each stage of the reflection pattern"""
    
    # Stage 1: Initial Generation
    GENERATOR_SYSTEM = """
    You are a Python programmer. Generate high-quality Python code based on the user's request.
    """
    
    # Stage 2: Self-Reflection/Critique
    REFLECTOR_SYSTEM = """
    You are a code reviewer. Analyze the provided Python code and identify areas for improvement, bugs, or optimizations.
    """
    
    # Stage 3: Refinement
    REFINER_SYSTEM = """
    You are a Python programmer focused on improvement. Improve the provided code based on the critique given.
    """

class ReflectionTemplates:
    """Message templates for user prompts"""
    
    GENERATE_TASK = "Generate Python code for: {task}"
    
    REFLECT_ON_CODE = """
    Review and critique this code:
    
    ```python
    {code}
    ```
    
    Provide specific feedback on improvements needed.
    """
    
    REFINE_CODE = """
    Improve this code based on the feedback:
    
    Original Code:
    ```python
    {code}
    ```
    
    Feedback:
    {critique}
    
    Provide the improved version.
    """

# Optional: Configuration
class ReflectionConfig:
    MAX_ITERATIONS = 3
    MODEL = "claude-3-5-sonnet-20241022"