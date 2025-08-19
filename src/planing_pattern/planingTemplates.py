"""
Message Templates for the Planning Pattern Agent (Software Development)
"""

class PlaningTemplates:
    """Message templates for different planning stages"""
    
    PLAN_TASK = """
    Create a detailed development plan for: {task}
    
    Requirements:
    - Break down into specific, actionable steps
    - Consider technical architecture and tools needed for this specific application
    - Include setup, development, testing, and deployment phases
    - Suggest realistic timeframes for each step
    - Identify potential challenges and solutions specific to this type of application
    - Consider the target audience and use case
    
    Project Type: {project_type}
    Complexity Level: {complexity}
    """
    
    VALIDATE_PLAN = """
    Review and improve this development plan:
    
    Original Task: {task}
    
    Current Plan:
    {plan}
    
    Please provide:
    1. Missing steps or considerations
    2. Potential issues or improvements
    3. Better ordering of tasks if needed
    4. Technical recommendations
    5. Risk assessment
    """
    
    ORGANIZE_EXECUTION = """
    Organize this development plan for team execution:
    
    Project: {task}
    
    Validated Plan:
    {validated_plan}
    
    Please provide:
    1. Organized phases/milestones
    2. Time estimates for each phase
    3. Required skills/team roles
    4. Dependencies and critical path
    5. Recommended tools and setup
    6. Success criteria for each phase
    """
    
    SIMPLE_PLAN = """
    Create a development plan for: {task}
    
    Focus on:
    - Clear, actionable steps 
    - Logical order of implementation
    - Key technical decisions
    - Basic timeline estimation
    - Consider the specific features and requirements 
    """

class PlaningConfig:
    """Configuration for the planning agent"""
    
    MAX_ITERATIONS = 3
    MODEL = "claude-3-5-sonnet-20241022"
    
    # Project complexity levels
    COMPLEXITY_LEVELS = {
        "simple": "Basic functionality, single developer, 1-2 weeks",
        "medium": "Multiple features, small team, 1-2 months", 
        "complex": "Full application, multiple developers, 2-6 months"
    }
    
    # Common project types
    PROJECT_TYPES = {
        "web_app": "Full-stack web application",
        "mobile_app": "Mobile application", 
        "api": "REST/GraphQL API service",
        "desktop_app": "Desktop application",
        "game": "Video game or mobile game",
        "ecommerce": "E-commerce platform",
        "social_app": "Social media application",
        "productivity": "Productivity/utility application",
        "educational": "Educational/learning application",
        "healthcare": "Healthcare/medical application",
        "fitness": "Fitness/wellness application",
        "finance": "Financial/banking application",
        "entertainment": "Entertainment/media application",
        "kids_app": "Application designed for children",
        "business": "Business management application",
        "iot": "IoT/smart device application"
    }
    

