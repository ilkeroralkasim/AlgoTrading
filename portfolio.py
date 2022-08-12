import numpy as np
import pandas as pd


def returns(prices: pd.DataFrame):
    return prices.pct_change()