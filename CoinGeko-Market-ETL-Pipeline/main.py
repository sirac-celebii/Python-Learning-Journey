from Extract.extract import extract
from Logs.logger import logger
from Transform.transform import transform
from Load.load import load

import pandas as pd
import time

def start_etl():
    start_time = time.time()

    logger.info("ETL Started.")
    logger.info("Extracting the Data.")
    try:
        data = get_crpyto_data()
        transformed_data = get_transformed_data(data)
        create_db(transformed_data)
    except Exception as e:
        logger.critical(f"ETL Failed : {e}.")
        raise
    finally:
            run_time = calculate_run_time(start_time)
            logger.info(f"Time elapsed : {run_time}")

    logger.info("ETL completed successfully !")
    logger.info("Program has ended.")

def calculate_run_time(start_time):
    logger.info("Calculating elapsed time")
    run_time = time.time() - start_time

    return run_time

def get_crpyto_data():
    data = extract()

    logger.info("Extracting succeeded.")
    return data
    

def get_transformed_data(data : pd.DataFrame):
    logger.info("Transforming the Data.")
    transformed_data = transform(data)

    logger.info("Transforming succeeded.")
    return transformed_data

def create_db(transformed_data : pd.DataFrame):
    logger.info("Creating Database")
    load(transformed_data)
    logger.info("Database created successfully !")



if __name__ == "__main__":
    start_etl()
