from datetime import datetime  # to take input for the dates
import pandas as pd  # to work with dataframes


from utils.extract_weather import fetch_api_data  # to fetch the data from the API
from utils.transform_response import (
    transform_api_data,
)  # to transform the data into a dictionary
from utils.create_csv import (
    gen_csv,
)  # to create a csv file from the list of dictionaries
from utils.connect_db import (
    connect_upload_db,
)  # to connect & upload the csv file to the SQL database
from utils.clean_docs import (
    clean_docs_folder,
)  # to move the csv file from docs folder to archive folder after uploading to the database

import config  # to get the API key and the API URL


def main():
    """
    This is used to perform all the steps from one place
    Step 0: Get the user input for the location and the date range

    Now since the date range is given but the api can give a json result for a paticular date
        we will run a loop for each date, and step 1 and 2 will be inside the loop
    Step 1: Extract the data from the API -> JSON values
    Step 2: Feed the data to transform_response.py to transform the data into a dictionary
        From the above step, we get a row of the data
        in step 3 we collect those rows and make a list of such dictories
    Step 3: Feed the list of dictionaries to a function which converts it into a CSV file and saves it in teh docs folder but with a catch
    Step 4: Upload the CSV file in the docs folder to table in the SQL database
        THEN MOVE THE CSV FILE TO THE ARCHIVE FOLDER


    """

    # STEP 0: Get the user input for the location and the date range
    location = input("Enter the location: ")
    start_date = datetime.strptime(
        input("Enter the start date (YYYY-MM-DD): "), "%Y-%m-%d"
    )
    end_date = datetime.strptime(input("Enter the end date (YYYY-MM-DD): "), "%Y-%m-%d")

    rows = []
    for date in pd.date_range(start=start_date, end=end_date):
        # Step 1: Extract the data from the API -> JSON values
        raw_json = fetch_api_data(location, date)

        # Step 2: Feed the data to transform_response.py to transform the data into a dictionary
        row = transform_api_data(raw_json, location, date, start_date, end_date)

        # Create a list of such dictionaries
        rows.append(row)

    # Step 3: Feed the list of dictionaries to a function which converts it into a CSV file
    try:
        gen_csv(config.CSV_FILE_PATH, rows)
    except Exception as e:
        print(f"Error occurred while generating CSV: {e}")

    ask = input("Do you want to upload the CSV file to the SQL database? (yes/no): ")
    if ask.lower() == "yes":
        # Step 4: Upload the CSV file in the docs folder to table in the SQL database
        # THEN MOVE THE CSV FILE TO THE ARCHIVE FOLDER
        try:
            if connect_upload_db(
                config.DB_SERVER, config.DB_DATABASE, pd.read_csv(config.CSV_FILE_PATH)
            ):
                print("Data uploaded successfully!")
        except Exception as e:
            print(f"Error occurred while uploading to database: {e}")
        finally:
            clean_docs_folder(config.CSV_FILE_PATH, config.ARCHIVE_CSV_FILE_PATH)


if __name__ == "__main__":
    main()


""" The table was created in the database with proper attributes and the data types. The table name is weather_data and it is created in the python_23467 schema."""
