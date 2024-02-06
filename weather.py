## The program takes an input from the user and outputs the weather 
## from a website in json format

import requests
import os
from dotenv import load_dotenv
import pprint

load_dotenv()

def cityweather():
    city = input("Please enter the city name:\n")
    request_url=f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    #print(request_url)
    output = requests.get(request_url).json()
    pprint(output)

cityweather()