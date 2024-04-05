import os
from dotenv import load_dotenv

load_dotenv()

# Bot
BOT_TOKEN = os.environ.get("BOT_TOKEN","7109933749:AAECk_lZQ5T7D76s3owaRORtGeM7KDFPKG4")
API_ID = int(os.environ.get("API_ID","24903318"))
API_HASH = os.environ.get("API_HASH","266a897e11f3872392f16a43e226c902")

# Authorisation
AUTH = bool(os.environ.get("AUTH", False))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

# Database (MongoDB)
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb+srv://mrnoobx:DAZCdTczVWyECi04@cluster0.sedgwxy.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Gemini-Bot")
