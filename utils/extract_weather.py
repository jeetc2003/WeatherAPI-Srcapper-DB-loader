import http
import requests

import config  # ----> check the comment below

"""
Since the file is in the utils folder and the config file is in the root directory, we can not just use 'import config' to import the config file
Therefore while running the script we must do->
--- python -m utils.extract_weather --- 

coz using just python utils.extract_weather will give an error->
ModuleNotFoundError: No module named 'config'


"""


def fetch_api_data(location, date):
    """
    Fetches weather data from the API based on location and time period.

    aruments:
    location (str): The location for which to fetch weather data.
    date (str): The date for which to fetch weather data.

    returns:
    dict: The JSON response from the API.
    """
    querystring = {"q": location, "dt": date}

    API_URL = f"{config.API_URL}?key={config.API_KEY}&q={location}&dt={date}"

    response = requests.get(API_URL)
    return response.json()
