import requests
import pandas as pd

from Logs.logger import logger

RAW_DATA_PARAMS = {
        "vs_currency" : "usd",
        "order" : "market_cap_desc",
        "per_page" : 250,
        "page" : 1
    }

BASE_URL = "https://api.coingecko.com/api/v3"
MARKET_URL = "https://api.coingecko.com/api/v3/coins/markets"
GLOBAL_URL = "https://api.coingecko.com/api/v3/global"

def extract():
    try:
        data = _get_data(MARKET_URL, RAW_DATA_PARAMS)
        return data
    except Exception as e:
        logger.critical(f"Extracting has Failed : {e}")
        raise 


def _get_response(url, params = None):
    try:
        response  = requests.get(url, headers= {"User-Agent" : "Mozilla/5.0"}, params= params, timeout= 15 )
    except requests.exceptions.TooManyRedirects:
        logger.error("The request limit has reached !")
        raise 
    except requests.exceptions.ConnectionError:
        logger.error("Connection failed !")
        raise
    except requests.exceptions.Timeout:
        logger.error("Request timed out.")
        raise

    logger.info(f"Response Status Code = {response.status_code}")
    
    try:
        response.raise_for_status()
        logger.info("Connection succeeded")
    except requests.exceptions.HTTPError as e:
        logger.error(f"Connection has Failed : {e}")
        raise

    return response

def _get_data(url, params) -> pd.DataFrame:
    logger.info("Fetching Market Data")
    response = _get_response(url, params)

    return pd.DataFrame(response.json())

def get_total_market_cap() -> float:
    logger.info("Fetching Total Market Capitalization")
    response = _get_response(GLOBAL_URL)

    data = response.json()

    return data["data"]["total_market_cap"]["usd"]


