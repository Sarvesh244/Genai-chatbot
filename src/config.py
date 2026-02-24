import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("CareerBot")

class Config:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = "gemini-3-flash-preview" 
    
    @staticmethod
    def validate():
        if not Config.GOOGLE_API_KEY:
            logger.critical("GOOGLE_API_KEY is missing!")
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")