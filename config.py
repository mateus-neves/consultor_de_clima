import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY', 'd2b1c7fcbfe5bb5ecb94f21560642390')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
