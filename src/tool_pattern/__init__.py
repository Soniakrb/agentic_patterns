"""
Usage:
    from tool_pattern import ToolAgent
    
    agent = ToolAgent()
    result = agent.run("What is the opening price of Apple stock?")
"""

from .tool_agent import ToolAgent

__all__ = [
    'ToolAgent'
]
