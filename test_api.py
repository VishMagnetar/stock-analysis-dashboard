import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries

print("--- Starting API Test ---")

#  Load the .env file
load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# Check API keyloaded
if API_KEY is None:
    print("Error: ALPHA_VANTAGE_API_KEY not found in .env file.")
else:
    print("API Key successfully loaded from .env file.")
    
    # to connect to Alpha Vantage
    try:
        print("Attempting to fetch data from Alpha Vantage for AAPL...")
        ts = TimeSeries(key=API_KEY, output_format='pandas')
        data, meta_data = ts.get_daily_adjusted(symbol='AAPL', outputsize='compact')
        
        print("\n✅ SUCCESS! Data fetched successfully.")
        print("Here is the most recent data point:")
        print(data.head(1))

    except Exception as e:
        print("\n FAILED! An error occurred.")
        print("Here is the specific error message from the API:")
        print(e)

print("\n--- Test Finished ---")