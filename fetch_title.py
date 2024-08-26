import os
import logging
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def fetch_titles():
    try:
        # Connect to the PostgreSQL database using environment variables
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dbname=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )

        cursor = connection.cursor()
        cursor.execute("SELECT title FROM training_table")

        # Fetch and log all titles teste
        titles = cursor.fetchall()
        if titles:
            logger.info("\n" + "="*40)
            logger.info("Fetched Titles:")
            logger.info("-"*40)
            for title in titles:
                logger.info(f"• {title[0]}")
            logger.info("="*40)
        else:
            logger.info("No titles found in the database.")

    except psycopg2.Error as err:
        logger.error(f"Error: {err}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            logger.info("PostgreSQL connection is closed")

if __name__ == "__main__":
    fetch_titles()
