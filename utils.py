# Import statements
import yfinance as yf
import pandas as pd

# import os
import numpy as np
import datetime as dt
from datetime import *

# from pathlib import Path
# import pandas_ta as ta
# from price_data_pull_yfinance import gethistoricalOHLC, saveHistStockData, loadHistDataFromDisk
from datetime import date

today = date.today()


def pullData(ticker, timeframe=4, interval="1m"):
    """function to pull a certain time frame of mintue date from yahoo finance as they only allow 1 week per request on that level of granularity.
    Inputs:
        - ticker: a yfinance ticker object
        - timeframe: (int) in weeks
    Output:
        - df: a pandas dataframe with the requested data"""

    # generate a list of datetime tuples that have the requested intervals
    # df = ticker.history(start=start,  end="2021-11-09", interval = "1m")

    today = datetime.today()
    weeks = timeframe
    days = timedelta(7 * weeks)
    startDate = today - days
    startDate = startDate.date()
    dfs = []
    currDate = today.date()
    while currDate > startDate:
        endIntervall = currDate
        startIntervall = currDate - timedelta(7)

        df = ticker.history(start=startIntervall, end=endIntervall, interval=interval)

        currDate = startIntervall

        dfs.append(df)
    if len(dfs) == 1:
        return dfs[0]
    else:
        concatDF = pd.concat(dfs)
        return concatDF