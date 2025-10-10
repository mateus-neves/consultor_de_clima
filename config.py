import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY', 'sua_api_key_aqui')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
