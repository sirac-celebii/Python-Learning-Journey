import sqlite3
import pandas as pd

from Logs.logger import logger

def load(data : pd.DataFrame):
    logger.info("Connecting to Database.")

    connection = sqlite3.connect("Crypto.db")
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    logger.info("Connection succeeded.")

    create_tables(cursor)
    
    coin_table_exists = check_coin_table(cursor)
    if not coin_table_exists:
        insert_coin(cursor, data)
    else:
        update_coin_table(cursor, data)
        
    insert_market_history(cursor, data)
    close_db(connection)

def check_coin_table(cursor : sqlite3.Cursor):
    cursor.execute("""
        SELECT 1 FROM Coin LIMIT 1
    """)
    result = cursor.fetchone()
    
    if result is None:
        return False
    else:
        return True
    

def create_tables(cursor : sqlite3.Cursor):
    logger.info("Ensuring database tables exist.")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Coin(
            coin_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            source_coin_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            symbol TEXT NOT NULL,
            current_price REAL,
            price_change_direction TEXT,
            high_24h REAL,
            low_24h REAL,
            daily_price_range REAL,
            price_change_24h REAL,
            price_change_percentage_24h,
            dilution_risk TEXT NOT NULL,
            ath REAL NOT NULL,
            ath_change_percentage REAL NOT NULL,
            atl REAL NOT NULL,
            atl_change_percentage REAL NOT NULL,
            fully_diluted_valuation REAL NOT NULL,
            market_cap INTEGER NOT NULL,
            market_cap_rank INTEGER NOT NULL,
            market_cap_category TEXT NOT NULL,
            market_dominance_pct REAL NOT NULL,
            market_cap_change_24h REAL,
            market_cap_change_percentage_24h REAL,
            total_volume REAL NOT NULL,
            circulating_supply REAL NOT NULL,
            circulation_ratio REAL,
            total_supply REAL NOT NULL,
            max_supply REAL,
            last_updated TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS MarketHistory(
        coin_id INTEGER NOT NULL,
        current_price REAL,
        price_change_direction TEXT,
        high_24h REAL,
        low_24h REAL,
        daily_price_range REAL,
        price_change_24h REAL,
        price_change_percentage_24h,
        dilution_risk TEXT NOT NULL,
        ath REAL NOT NULL,
        ath_change_percentage REAL NOT NULL,
        atl REAL NOT NULL,
        atl_change_percentage REAL NOT NULL,
        fully_diluted_valuation REAL NOT NULL,
        market_cap INTEGER NOT NULL,
        market_cap_rank INTEGER NOT NULL,
        market_cap_category TEXT NOT NULL,
        market_dominance_pct REAL NOT NULL,
        market_cap_change_24h REAL,
        market_cap_change_percentage_24h REAL,
        total_volume REAL NOT NULL,
        circulating_supply REAL NOT NULL,
        circulation_ratio REAL,
        total_supply REAL NOT NULL,
        max_supply REAL,
        last_updated TEXT NOT NULL,
                   
        PRIMARY KEY (coin_id, last_updated),
        FOREIGN KEY (coin_id) REFERENCES Coin(coin_id)
        )
    """)

    logger.info("Database scheme is ready.")            

def insert_coin(cursor : sqlite3.Cursor, data : pd.DataFrame):
    logger.info("Inserting coins.")
    for index, row in data.iterrows():
        cursor.execute("""
            INSERT INTO Coin (source_coin_id, name, symbol, current_price, price_change_direction, high_24h, low_24h, daily_price_range,
                                        price_change_24h, price_change_percentage_24h, dilution_risk, ath, ath_change_percentage, atl,
                                        atl_change_percentage, fully_diluted_valuation, market_cap, market_cap_rank, market_cap_category,
                                        market_dominance_pct, market_cap_change_24h, market_cap_change_percentage_24h, total_volume,
                                        circulating_supply, circulation_ratio, total_supply, max_supply, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            row["source_coin_id"],
            row["name"],
            row["symbol"],
            row["current_price"],
            row["price_change_direction"],
            row["high_24h"],
            row["low_24h"],
            row["daily_price_range"],
            row["price_change_24h"],
            row["price_change_percentage_24h"],
            row["dilution_risk"],
            row["ath"],
            row["ath_change_percentage"],
            row["atl"],
            row["atl_change_percentage"],
            row["fully_diluted_valuation"],
            row["market_cap"],
            row["market_cap_rank"],
            row["market_cap_category"],
            row["market_dominance_pct"],
            row["market_cap_change_24h"],
            row["market_cap_change_percentage_24h"],
            row["total_volume"],
            row["circulating_supply"],
            row["circulation_ratio"],
            row["total_supply"],
            row["max_supply"],
            row["last_updated"],
        ))

    logger.info("Coins has inserted.")

def update_coin_table(cursor : sqlite3.Cursor, data : pd.DataFrame):
    logger.info("Uptading Coin table.")
    for index, row in data.iterrows():
        cursor.execute("""
            UPDATE Coin
            SET current_price = ?,
                price_change_direction = ?,
                high_24h  = ?,
                low_24h  = ?,
                daily_price_range = ?, 
                price_change_24h  = ?,
                price_change_percentage_24h = ?,
                dilution_risk  = ?,
                ath = ?,
                ath_change_percentage = ?, 
                atl = ?,  
                atl_change_percentage = ?,  
                fully_diluted_valuation = ?,  
                market_cap = ?,  
                market_cap_rank = ?,  
                market_cap_category = ?,  
                market_dominance_pct = ?,  
                market_cap_change_24h = ?,  
                market_cap_change_percentage_24h = ?,  
                total_volume = ?,  
                circulating_supply = ?,  
                circulation_ratio = ?, 
                total_supply = ?,  
                max_supply = ?,  
                last_updated = ?

            WHERE source_coin_id = ?
        """, (
            row["current_price"],
            row["price_change_direction"],
            row["high_24h"],
            row["low_24h"],
            row["daily_price_range"],
            row["price_change_24h"],
            row["price_change_percentage_24h"],
            row["dilution_risk"],
            row["ath"],
            row["ath_change_percentage"],
            row["atl"],
            row["atl_change_percentage"],
            row["fully_diluted_valuation"],
            row["market_cap"],
            row["market_cap_rank"],
            row["market_cap_category"],
            row["market_dominance_pct"],
            row["market_cap_change_24h"],
            row["market_cap_change_percentage_24h"],
            row["total_volume"],
            row["circulating_supply"],
            row["circulation_ratio"],
            row["total_supply"],
            row["max_supply"],
            row["last_updated"],
            row["source_coin_id"]
        ))

    logger.info("Coin table updated.")


def insert_market_history(cursor : sqlite3.Cursor, data : pd.DataFrame):
    logger.info("Inserting market history.")
    for index, row in data.iterrows():

        cursor.execute("""
            SELECT coin_id FROM Coin
            WHERE source_coin_id = ?
        """, (row["source_coin_id"],))
        
        result = cursor.fetchone()

        if result == None:
            return
        else:
            coin_id = result[0]

        cursor.execute("""
            INSERT INTO MarketHistory (coin_id, current_price, price_change_direction, high_24h, low_24h, daily_price_range,
                                       price_change_24h, price_change_percentage_24h, dilution_risk, ath, ath_change_percentage, atl,
                                       atl_change_percentage, fully_diluted_valuation, market_cap, market_cap_rank, market_cap_category,
                                       market_dominance_pct, market_cap_change_24h, market_cap_change_percentage_24h, total_volume,
                                       circulating_supply, circulation_ratio, total_supply, max_supply, last_updated)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            coin_id,
            row["current_price"],
            row["price_change_direction"],
            row["high_24h"],
            row["low_24h"],
            row["daily_price_range"],
            row["price_change_24h"],
            row["price_change_percentage_24h"],
            row["dilution_risk"],
            row["ath"],
            row["ath_change_percentage"],
            row["atl"],
            row["atl_change_percentage"],
            row["fully_diluted_valuation"],
            row["market_cap"],
            row["market_cap_rank"],
            row["market_cap_category"],
            row["market_dominance_pct"],
            row["market_cap_change_24h"],
            row["market_cap_change_percentage_24h"],
            row["total_volume"],
            row["circulating_supply"],
            row["circulation_ratio"],
            row["total_supply"],
            row["max_supply"],
            row["last_updated"],
        ))

    logger.info("Market history inserted.")


def close_db(connection : sqlite3.Connection):
    logger.info("Closing database.")
    connection.commit()
    connection.close()
    logger.info("Database closed.")

