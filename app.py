from src.airbnbproject.logger import get_logger
from src.airbnbproject.exception import CustomException
import sys


logger = get_logger("airbnb-logger")

if __name__ == "__main__":
    try:
        logger.info("Starting the Airbnb project application.")

        # Application logic
        a = 1 / 0

    except Exception as e:
        logger.exception("Custom Exception occurred")
        #raise CustomException(e, sys) from e

    finally:
        logger.info("Airbnb project application finished execution.")
