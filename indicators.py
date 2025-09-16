import pandas as pd
import pandas_ta as ta

def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates key technical indicators and adds them to the DataFrame."""
    if df.empty:
        return df

    # Moving Averages
    df.ta.sma(length=20, append=True)
    df.ta.sma(length=50, append=True)

    # Relative Strength Index (RSI)
    df.ta.rsi(append=True)

    # Bollinger Bands for Volatility
    df.ta.bbands(length=20, append=True)

    # Daily Returns
    df['daily_return'] = df['Close'].pct_change()

    df.dropna(inplace=True)
    return df