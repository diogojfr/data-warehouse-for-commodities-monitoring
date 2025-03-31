# imports
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# environment variables imports

# get the asset quotations

commodities = ['CL=F', 'GC=F', 'SI=F']

def get_commodities_data(ticker_name, period='5d', interval='1d'):
    """
    This function gets the commodities data from Yahoo Finance and returns it as a pandas DataFrame.
    """
    ticker = yf.Ticker(ticker_name)
    data = ticker.history(period=period, interval=interval)[['Close']] 
    data['ticker_name'] = ticker_name

    return data


# concatenate the asset quotations
def concat_asset_quotations(commodities_list):
    """
    This function concatenates the asset quotations of the commodities and returns it as a pandas DataFrame.
    """
    asset_data_list = []
    for tick in commodities_list:
        asset_data = get_commodities_data(tick)
        asset_data_list.append(asset_data)

    return pd.concat(asset_data_list)


if __name__ == "__main__":
    df = concat_asset_quotations(commodities)
    print(df)