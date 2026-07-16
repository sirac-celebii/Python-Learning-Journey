import logging

logger = logging.getLogger("crypto_etl")
logging.basicConfig(filename= "etl.log",
                    encoding= "utf-8",
                    level= logging.DEBUG,
                    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S"
                    )