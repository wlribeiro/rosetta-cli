import os
from dotenv import load_dotenv


load_dotenv()


URL = "https://text-translator2.p.rapidapi.com/translate"
HEADERS = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": os.getenv("API_KEY"),
    "X-RapidAPI-Host": "text-translator2.p.rapidapi.com",
}
