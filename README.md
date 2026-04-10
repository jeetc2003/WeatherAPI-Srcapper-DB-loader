# Weather Data Pipeline Project

This project is a simple and structured weather data pipeline that integrates with a weather API to fetch, process, and store historical weather data based on user input.

## Overview

The application allows a user to enter a location along with a start date and end date, fetch weather data for each date in that range, store the processed data in a CSV file, and optionally upload the data to a SQL database. The overall design follows a clean ETL (Extract → Transform → Load) approach with clear separation of responsibilities.

## How It Works

The system starts by taking user input for location and date range. Since the API provides data for one date at a time, the application iterates over each date in the range and makes individual API calls.

The raw JSON response from the API is not stored directly. Instead, it is transformed to extract only the required fields such as temperature (max, min, average), wind speed, precipitation, snowfall, humidity, visibility, and relevant metadata like location and date range. This ensures the data is clean, structured, and ready for storage.

All processed records are collected and written into a CSV file stored in the `docs/` folder. This file acts as a staging layer for the current dataset. The user is then prompted to decide whether to upload the data to the database.

If the user chooses to proceed, the data is inserted into a SQL Server table using batch operations for better performance. Once the upload is complete, the CSV file is moved from the `docs/` folder to the `archive/` folder, ensuring that historical data is preserved while keeping the working directory clean.

## Project Structure

```
.
├── main.py
├── config.py
├── utils/
│   ├── extract_weather.py
│   ├── transform_response.py
│   ├── create_csv.py
│   ├── connect_db.py
│   └── clean_docs.py
├── docs/
│   └── weather_data.csv
├── archive/
│   └── historical_data.csv
```

## Key Design Choices

The project uses a modular architecture where each step in the pipeline is handled in a separate module. CSV is used as a staging layer to keep the workflow simple and transparent. The upload step is user-controlled to avoid unnecessary database operations. An archiving mechanism is implemented to maintain historical records while keeping the active dataset clean. Batch insertion is used during database upload to improve performance.

## Tech Stack

Python is used as the core language, along with Pandas for data handling, Requests for API calls, and PyODBC for SQL Server integration.

## Notes

The database table is pre-created with the required schema and data types. Authentication is handled using ActiveDirectoryInteractive mode. The implementation assumes that the API response structure remains consistent.

## Limitations

The system makes one API call per date, which can become slow for larger date ranges. There is no retry mechanism or robust error handling for API failures. User input is taken as-is without validation.

## Summary

This project demonstrates a clean and practical implementation of a basic data pipeline. It focuses on simplicity, modular design, and clarity while covering the essential steps of extracting, transforming, and loading data.
