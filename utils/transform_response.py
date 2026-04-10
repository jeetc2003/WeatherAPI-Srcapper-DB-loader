import pandas as pd
import numpy as np
from datetime import datetime


def transform_api_data(raw_json, location, date, st_date, end_date):
    """

    First of all, lets chech what the API response looks like.
    The API response is a JSON object that contains weather information on a particular date for a particular location.

    But the user wants the data in csv format and that too for a range of dates.

    Therefore, we need to call the api multiple times for each date in the date range
    Then extract the required information from the JSON response and then store it in a dataframe

    For this, we create a list called rows which stores the data for each date in the date range. Each element of the list is a dictionary that contains the required information for that date.

    Then make it a datrame.
    Then finally convert it to csv format.


    NOTE!!!!
    The above docs was written while building the project.

    ---> Now it just reads the JSON response and transforms it into a dictionary that can be easily converted to a dataframe.

    ARGS: raw_json (dict): The JSON response from the API.
          location (str): The location for which the data is fetched.
          date (datetime): The date for which the data is fetched.

    RETURNS: dict: A dictionary that contains the required information for that date.

    """

    df = pd.json_normalize(raw_json["forecast"]["forecastday"][0]["day"])

    row = {
        "date": date.strftime("%Y-%m-%d"),
        "maxtemp_c": df["maxtemp_c"].values[0],
        "mintemp_c": df["mintemp_c"].values[0],
        "avgtemp_c": df["avgtemp_c"].values[0],
        "maxwind_kph": df["maxwind_kph"].values[0],
        "totalprecip_mm": df["totalprecip_mm"].values[0],
        "totalsnow_cm": df["totalsnow_cm"].values[0],
        "avgvis_km": df["avgvis_km"].values[0],
        "avghumidity": df["avghumidity"].values[0],
        "location": location,
        "start_date": st_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
    }

    return row
