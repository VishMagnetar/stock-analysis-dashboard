# Stock Market Analytics Dashboard

**A web-based platform for visualizing stock data and technical indicators to gain market insights.**
__________________________________________________________________________________________________________________________________________________________________________

###  [Live Demo]      https://stock-analysis-dashboard-vishmagnetor.streamlit.app/

__________________________________________________________________________________________________________________________________________________________________________

### ## Overview

This project is an end-to-end stock market analysis tool built with Python and Streamlit. It fetches real-time and historical stock data from the Alpha Vantage API, 
calculates key technical indicators, and presents the information in an interactive and user-friendly web dashboard. 
The goal is to provide actionable insights for traders and investors through clear data visualization.

__________________________________________________________________________________________________________________________________________________________________________

### ## Key Features

* **Interactive Charts**: Candlestick charts with moving averages and trading volume visualization.
* **Technical Indicators**: Calculates and displays key indicators like Moving Averages (MA) and Relative Strength Index (RSI).
* **Dynamic Data Fetching**: Pulls the latest daily stock data using the Alpha Vantage API.
* **Data Export**: Allows users to download the raw data and calculated indicators as a CSV file.
* **Secure API Key Management**: Uses environment variables and Streamlit's secrets management for secure API key handling.

__________________________________________________________________________________________________________________________________________________________________________


### ## Technologies Used

* **Backend**: Python
* **Frontend**: Streamlit
* **Data Analysis**: Pandas, Pandas TA
* **Data Fetching**: Alpha Vantage API, Requests
* **Charting**: Plotly
* **Deployment**: Streamlit Community Cloud

__________________________________________________________________________________________________________________________________________________________________________

### ## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your API Key:**
    * Create a file named `.env` in the root of the project directory.
    * Add your Alpha Vantage API key to the file in the following format:
        ```
        ALPHA_VANTAGE_API_KEY="YOUR_API_KEY_HERE"
        ```

5.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

__________________________________________________________________________________________________________________________________________________________________________

### ## Usage

Once the application is running, enter a valid stock symbol (e.g., AAPL, GOOGL, MSFT) in the sidebar and the dashboard will 
automatically update with the latest data and analysis for that stock.
__________________________________________________________________________________________________________________________________________________________________________



© 2025 Vishal. All Rights Reserved




__________________________________________________________________________________________________________________________________________________________________________
