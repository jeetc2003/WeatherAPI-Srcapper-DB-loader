import pyodbc
import pandas as pd



def connect_upload_db(DB_SERVER, DB_DATABASE, df):
    """
    This function connects to the SQL database and uploads the data from the CSV file to the table in the database.
    Arguments:
    DB_SERVER (str): The server name of the SQL database.
    DB_DATABASE (str): The database name of the SQL database.
    df (pandas.DataFrame): The dataframe that contains the data to be uploaded to the SQL database.
    
    Returns: 1 if the data is uploaded successfully, else returns 0.
    """

    server = DB_SERVER
    database = DB_DATABASE

    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        "Authentication=ActiveDirectoryInteractive;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )

    cursor = conn.cursor()
    cursor.fast_executemany = True

    # gives list of values_list
    data = df.values.tolist()

    cursor.executemany(
        """
        INSERT INTO python_23467.weather_data (
            date, maxtemp_c, mintemp_c, avgtemp_c,
            maxwind_kph, totalprecip_mm, totalsnow_cm,
            avgvis_km, avghumidity, location,
            start_date, end_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        data,
    )

    conn.commit()

    return 1
