"""src/scoring.py"""

import pandas as pd

def calculate_sma(series: pd.Series, window: int) -> pd.Series:
    """Calculate the simple moving average (SMA)"""
    return series.rolling(window=window).mean()

def calculate_3mo_return(prices: pd.Series) -> float:
    """Calculate the 3-month return (approx. 63 trading days)"""
    return (prices.iloc[-1] / prices.iloc[-63]) - 1

def apply_momentum_strategy(price_df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply momentum strategy to a DataFrame of adjusted close prices.
    Columns are tickers, rows are dates.
    Returns a DataFrame of selected ETFs with their scores.
    """
    results = []

    for ticker in price_df.columns:
        series = price_df[ticker].dropna()

        if len(series) < 100:
            continue  # Not enough data to calculate SMA

        sma_100 = calculate_sma(series, 100)
        price_today = series.iloc[-1]
        sma_today = sma_100.iloc[-1]

        # Check trend filter
        if price_today <= sma_today:
            continue

        # Calculate 3-month return
        try:
            score = calculate_3mo_return(series)
            results.append((ticker, price_today, sma_today, score))
        except IndexError:
            continue  # Not enough data for 3-month return

    ranked = pd.DataFrame(results, columns=["Ticker", "Price", "SMA_100", "MomentumScore"])
    ranked = ranked.sort_values(by="MomentumScore", ascending=False).reset_index(drop=True)

    return ranked
