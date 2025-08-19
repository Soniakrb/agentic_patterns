

from anthropic import Anthropic
import os
import json
from typing import Dict, List
from dotenv import load_dotenv
from .tools import get_opening_price, get_yesterday_high_low, get_full_stock_info

load_dotenv()


class ToolAgent:
    
    def __init__(self, api_key: str = None, model: str = "claude-3-5-sonnet-20241022"):
        self.client = Anthropic(api_key=api_key or os.getenv("ANTHROPIC_API_KEY"))
        self.model = model
        
        self.tools = [
            {
                "name": "get_opening_price",
                "description": "Get the opening price of a stock for today",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL, GOOGL, MSFT)"
                        }
                    },
                    "required": ["symbol"]
                }
            },
            {
                "name": "get_yesterday_high_low",
                "description": "Get yesterday's high and low prices for a stock",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL, GOOGL, MSFT)"
                        }
                    },
                    "required": ["symbol"]
                }
            },
            {
                "name": "get_full_stock_info",
                "description": "Get stock information including opening price, yesterday's high/low, current price, market cap, and company details",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "symbol": {
                            "type": "string",
                            "description": "Stock symbol (e.g., AAPL, GOOGL, MSFT)"
                        }
                    },
                    "required": ["symbol"]
                }
            },

        ]
        
        self.tool_functions = {
            "get_opening_price": get_opening_price,
            "get_yesterday_high_low": get_yesterday_high_low,
            "get_full_stock_info": get_full_stock_info
        }
    
    def run(self, user_query: str) -> str:
       
        print(f"Processing query: {user_query}")
       
        messages = [{"role": "user", "content": user_query}]
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            system="You are a finance assistant. You have access to stock market tools to get real-time data using Yahoo Finance. Use the tools when users ask about specific stock information. Always use the most appropriate tool for the user's question.",
            messages=messages,
            tools=self.tools
        )
        
        if response.stop_reason == "tool_use":
            tool_result = self._execute_tool(response.content[-1])
            
            messages.append({"role": "assistant", "content": response.content})
            messages.append({
                "role": "user", 
                "content": [tool_result]
            })
            
            final_response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                system="You are a finance assistant. Present the tool results in a clear, user-friendly way. Format numbers nicely and provide helpful context.",
                messages=messages,
                tools=self.tools
            )
            
            return final_response.content[0].text
        else:
            return response.content[0].text
    
    def _execute_tool(self, tool_use_block):
        tool_name = tool_use_block.name
        tool_input = tool_use_block.input
        
        print(f"Executing tool: {tool_name} with input: {tool_input}")
        
        if tool_name in self.tool_functions:
            result = self.tool_functions[tool_name](**tool_input)
            
            return {
                "type": "tool_result",
                "tool_use_id": tool_use_block.id,
                "content": result
            }
        else:
            return {
                "type": "tool_result", 
                "tool_use_id": tool_use_block.id,
                "content": f"Error: Unknown tool {tool_name}"
            }