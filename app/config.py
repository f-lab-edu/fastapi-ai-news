import os
import openai

OPENAI_API_KEY = os.getenv("open_api_key")

openai.api_key = OPENAI_API_KEY

OPENAI_MODEL = "gpt-3.5-turbo"
