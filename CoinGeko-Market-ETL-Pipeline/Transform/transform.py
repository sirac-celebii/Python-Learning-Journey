import pandas as pd

from Logs.logger import logger 
from Extract.extract import get_total_market_cap
from config import LARGE_CAP_LIMIT, SMALL_CAP_LIMIT, HIGH_RISK_LIMIT, LOW_RISK_LIMIT

pd.set_option("display.max_columns", None)
pd.set_option("display.float_format", "{:,.3f}".format)


def transform(data : pd.DataFrame):
    drop_unwanted_columns(data)
    create_features(data)
    clean_data(data)
    transformed_data = get_transformed_data(data)

    return transformed_data

def drop_unwanted_columns(df : pd.DataFrame):
    logger.info("Dropping unnecessary columns.")
    unnecessary_columns = ["image", "roi", "ath_date", "atl_date"]

    df.drop(unnecessary_columns, axis= 1, inplace= True)

def create_features(df : pd.DataFrame): 
    logger.info("Creating new features.")
    df["source_coin_id"] = df["id"]
    df.drop("id", axis = 1, inplace = True)

    total_market_cap = get_total_market_cap()

    df["market_dominance_pct"] = (df["market_cap"] / total_market_cap) * 100
    df["price_change_direction"] = df["price_change_24h"].map(lambda x: "Rise" if x > 0 else "Fall" if x < 0 else "Stable")
    # df["market_cap_category"] = [x for x in df["market_cap"]"Small Cap" if df["market_cap"] < 10**9 else "Large Cap" if df["market_cap"] > 10**10 else "Mid Cap"]
    df["market_cap_category"] = df["market_cap"].map(lambda x: "Small Cap" if x < SMALL_CAP_LIMIT else "Large Cap" if x > LARGE_CAP_LIMIT else "Mid Cap")

    ratio = (df["market_cap"] / df["fully_diluted_valuation"]) 
    # df["diluation_risk"] = ["High Risk" if ratio < 0.3 else "Low Risk" if ratio >= 0.5 else "Medium Risk"]
    df["dilution_risk"] = ratio.apply(lambda x: "High Risk" if x < HIGH_RISK_LIMIT else "Low Risk" if x >= LOW_RISK_LIMIT else "Medium Risk")

    df["circulation_ratio"] = (df["circulating_supply"] / df["max_supply"]) * 100

    df["daily_price_range"] = df["high_24h"] - df["low_24h"]

    df["last_updated"] = pd.to_datetime(df["last_updated"]).dt.tz_localize(None).astype("str")

def clean_data(df : pd.DataFrame):
    logger.info("Cleaning the data.")
    for column in df.select_dtypes("O").columns:
        df.fillna({column : "Unknown"}, inplace= True)

    df["source_coin_id"] = df["source_coin_id"].str.replace("-", " ", regex= False)


def get_transformed_data(df : pd.DataFrame):
    return df

