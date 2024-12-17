from dotenv import load_dotenv
import requests
import os

load_dotenv()

API_KEY = os.getenv('ASTRO_PIC_API_KEY')


class APIDataManager:

    def __init__(self):
        self.api_key = os.getenv('ASTRO_PIC_API_KEY')

    def get_picture_of_the_day(self):
        endpoint = 'https://api.nasa.gov/planetary/apod'

        parameters = {
            'api_key': self.api_key
        }

        response = requests.get(url=endpoint, params=parameters)

        data = response.json()

        title = data.get("title", "No Title")
        explanation = data.get("explanation", "No Description")
        image_url = data.get("url", None)
        media_type = data.get("media_type", None)

        # print(f"Title: {title}")
        # print(f"Explanation: {explanation}")
        # print(f"Media Type: {media_type}")
        # print(f"URL: {image_url}")

        return title, explanation, media_type, image_url

    def get_mars_weather(self):
        endpoint = 'https://api.nasa.gov/insight_weather/'

        parameters = {
            'api_key': self.api_key,
            'ver': 1.0,
            'feedtype': 'json'
        }

        response = requests.get(url=endpoint, params=parameters)

        data = response.json()

        print(data)

        average_temp = {data['675']['AT']['av']}
        min_temp = {data['675']['AT']['mn']}
        max_temp = {data['675']['AT']['mx']}
        first_utc_date_collection = {data['675']['First_UTC']}

        return average_temp, min_temp, max_temp, first_utc_date_collection



