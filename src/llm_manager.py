import google.generativeai as genai
from src.config import Config, logger
from src.prompts import Prompts

class GeminiLLM:
    def __init__(self):
        Config.validate()
        genai.configure(api_key=Config.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel(
            model_name=Config.MODEL_NAME,
            system_instruction=Prompts.SYSTEM_PROMPT
        )
        self.chat_session = None

    def start_chat(self, history=None):
        """Initializes or restores a chat session."""
        if history is None:
            history = []
        self.chat_session = self.model.start_chat(history=history)
        logger.info("Chat session initialized.")

    def get_response(self, user_input):
        """Sends message to Gemini and handles exceptions."""
        try:
            logger.info(f"Sending request: {user_input[:50]}...")
            response = self.chat_session.send_message(user_input)
            
            logger.info("Response received successfully.")
            return response.text
        except Exception as e:
            logger.error(f"API Error: {str(e)}")
            return "I'm encountering a technical issue connecting to my brain. Please try again in a moment."