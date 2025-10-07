import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY', 'INSIRA_SUA_API_KEY_AQUI')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
