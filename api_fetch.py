import os
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_alpha_vantage_data(symbol: str) -> pd.DataFrame:
    """Fetches daily stock data from Alpha Vantage API."""
    try:
        ts = TimeSeries(key=API_KEY, output_format='pandas')
        # Get daily adjusted data, which includes splits and dividends 
        data, meta_data = ts.get_daily(symbol=symbol, outputsize='full')
        
        # The data columns have names like '1. open', '2. high'. Let's rename them.
        data.rename(columns={
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        }, inplace=True)
        
        # The index is datetime
        data.sort_index(inplace=True)
        
        df = data[['Open', 'High', 'Low', 'Close', 'Volume']]
        return df

  
    except Exception as e:
     print("----------- DETAILED ERROR FROM ALPHA VANTAGE -----------")
     print(e)
     print("---------------------------------------------------------")
     return pd.DataFrame()