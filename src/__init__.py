"""
Usage:
    from src.reflection_pattern import ReflectionAgent
    from src.multiagent_pattern import Agent, Crew
    from src.planing_pattern import PlaningAgent  
    from src.tool_pattern import ToolAgent
"""



# Import patterns when they're ready
from . import reflection_pattern
# from . import multiagent_pattern
# from . import planing_pattern  
# from . import tool_pattern

__all__ = [
    'reflection_pattern',
    # 'multiagent_pattern',
    # 'planing_pattern',
    # 'tool_pattern'
]
