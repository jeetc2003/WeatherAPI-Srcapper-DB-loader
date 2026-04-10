from pathlib import Path
import pandas as pd


def clean_docs_folder(docs_csv_file_path, archive_csv_file_path):
    """
    This function moves the CSV file from the docs folder to the archive folder after uploading to the database.

    Arguments:
    docs_csv_file_path (str): The path of the CSV file in the docs folder.
    archive_csv_file_path (str): The path of the CSV file in the archive folder.

    Returns: NULL
    """

    docs_csv_file = Path(docs_csv_file_path)
    archive_csv_file = Path(archive_csv_file_path)

    # to read the csv data
    df = pd.read_csv(docs_csv_file)

    # to move the csv file from docs folder to archive folder
    df.to_csv(
        archive_csv_file, mode="a", header=not archive_csv_file.exists(), index=False
    )

    # Delete source file
    docs_csv_file.unlink()
