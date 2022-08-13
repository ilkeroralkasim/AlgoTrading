import numpy as np
import pandas as pd


def returns(prices: pd.DataFrame):
    '''
    Returns the returns of the input seriers
    '''
    return prices.pct_change()