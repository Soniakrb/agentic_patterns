#!/usr/bin/env python3
"""
Test script for the Tool Pattern Agent (Stock Market)
"""

from src.tool_pattern import ToolAgent

def main():
    print("Testing Tool Pattern Agent - Stock Market")
    print("=" * 50)
    
    # Initialize the tool agent
    agent = ToolAgent()
    
    # Test queries
    test_queries = [
        "What is the opening price of Apple stock?",
        "Show me yesterday's high and low for Microsoft",
        "Give me full information about Tesla stock",
        "What about Google stock prices?",
        "Can you compare Apple and Microsoft opening prices?"
    ]
    
    for i, query in enumerate(test_queries, 1):
        print(f"\nTEST {i}: {query}")
        print("-" * 40)
        
        try:
            response = agent.run(query)
            print(response)
        except Exception as e:
            print(f"Error: {e}")
        
        if i < len(test_queries):
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
