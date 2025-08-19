
import yfinance as yf
import pandas as pd
from typing import Dict, Optional, List
from datetime import datetime, timedelta


class StockDataProvider:
    """Handles stock data fetching using yfinance"""
    
    @staticmethod
    def get_stock_info(symbol: str) -> Dict:
        """
        Get stock information
        
        Args:
            symbol: Stock symbol (e.g., 'AAPL', 'GOOGL', 'MSFT')
            
        Returns:
            Dict with stock data or error message
        """
        try:
            ticker = yf.Ticker(symbol)
            
            # Get historical data for last 2 days to get yesterday's data
            hist = ticker.history(period="2d")
            
            if hist.empty:
                return {"error": f"No data found for symbol: {symbol}"}
            
            # Get basic info
            info = ticker.info
            
            # Today's data 
            today = hist.iloc[-1] if len(hist) > 0 else None
            # Yesterday's data 
            yesterday = hist.iloc[-2] if len(hist) > 1 else today
            
            result = {
                "symbol": symbol.upper(),
                "company_name": info.get('longName', 'N/A'),
                "current_price": round(today['Close'], 2) if today is not None else None,
                "opening_price": round(today['Open'], 2) if today is not None else None,
                "yesterday_high": round(yesterday['High'], 2) if yesterday is not None else None,
                "yesterday_low": round(yesterday['Low'], 2) if yesterday is not None else None,
                "yesterday_close": round(yesterday['Close'], 2) if yesterday is not None else None,
                "volume": int(today['Volume']) if today is not None else None,
                "market_cap": info.get('marketCap'),
                "currency": info.get('currency', 'USD'),
                "exchange": info.get('exchange', 'N/A'),
                "sector": info.get('sector', 'N/A'),
                "last_updated": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            return result
            
        except Exception as e:
            return {"error": f"Failed to fetch data for {symbol}: {str(e)}"}



def get_opening_price(symbol: str) -> str:
    """
    Tool: Get the opening price of a stock for today
    
    Args:
        symbol: Stock ticker symbol (e.g., AAPL, GOOGL)
        
    Returns:
        String with opening price information
    """
    data = StockDataProvider.get_stock_info(symbol)
    
    if 'error' in data:
        return f"Error: {data['error']}"
    
    if data['opening_price'] is None:
        return f"Opening price not available for {data['symbol']}"
    
    return f"Opening price for {data['company_name']} ({data['symbol']}): ${data['opening_price']} {data['currency']}"


def get_yesterday_high_low(symbol: str) -> str:
    """
    Tool: Get yesterday's high and low prices for a stock
    
    Args:
        symbol: Stock ticker symbol (e.g., AAPL, GOOGL)
        
    Returns:
        String with yesterday's high and low prices
    """
    data = StockDataProvider.get_stock_info(symbol)
    
    if 'error' in data:
        return f"Error: {data['error']}"
    
    if data['yesterday_high'] is None or data['yesterday_low'] is None:
        return f"Yesterday's price data not available for {data['symbol']}"
    
    return f"Yesterday's prices for {data['company_name']} ({data['symbol']}): High ${data['yesterday_high']}, Low ${data['yesterday_low']} {data['currency']}"


def get_full_stock_info(symbol: str) -> str:
    """
    Tool: Get stock information
    
    Args:
        symbol: Stock ticker symbol (e.g., AAPL, GOOGL)
        
    Returns:
        String with complete stock information
    """
    data = StockDataProvider.get_stock_info(symbol)
    
    if 'error' in data:
        return f"Error: {data['error']}"
    
    # Format market cap
    market_cap_str = "N/A"
    if data['market_cap']:
        if data['market_cap'] >= 1e12:
            market_cap_str = f"${data['market_cap']/1e12:.2f}T"
        elif data['market_cap'] >= 1e9:
            market_cap_str = f"${data['market_cap']/1e9:.2f}B"
        elif data['market_cap'] >= 1e6:
            market_cap_str = f"${data['market_cap']/1e6:.2f}M"
        else:
            market_cap_str = f"${data['market_cap']:,.0f}"
    
    # Format volume
    volume_str = f"{data['volume']:,}" if data['volume'] else "N/A"
    
    info = f"""Stock Information for {data['company_name']} ({data['symbol']}):

Current Stock Data:
- Current Price: ${data['current_price']} {data['currency']}
- Opening Price: ${data['opening_price']} {data['currency']}
- Volume: {volume_str}

Yesterday's Data:
- High: ${data['yesterday_high']} {data['currency']}
- Low: ${data['yesterday_low']} {data['currency']}
- Close: ${data['yesterday_close']} {data['currency']}

Company Information:
- Exchange: {data['exchange']}
- Sector: {data['sector']}
- Market Cap: {market_cap_str}
- Currency: {data['currency']}

Last Updated: {data['last_updated']}"""
    
    return info


