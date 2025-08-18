#!/usr/bin/env python3
"""
Testing Reflection Pattern Agent
"""

from src.reflection_pattern.reflection_agent import ReflectionAgent

def main():
    agent = ReflectionAgent()
   
    task = "Create a function to calculate the factorial of a number"
    
    print(f"Testing reflection agent with task: {task}")
    
    try:
        # Run the reflection cycle
        result = agent.run(task)
        
        # Display results
        print(f"\n📝 INITIAL CODE:")
        print(result['initial_code'])
        
        print(f"\n🔍 CRITIQUE:")
        print(result['critique'])
        
        print(f"\n✨ REFINED CODE:")
        print(result['refined_code'])
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
