from .agent import Agent

class Crew:
    def __init__(self, agents: list[Agent]):
        self.agents = agents
    
    def run(self, user_query: str) -> str:
        for agent in self.agents:
            agent.run(user_query)   
            
