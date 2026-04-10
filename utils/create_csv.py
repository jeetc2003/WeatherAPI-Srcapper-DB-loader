import pandas as pd
from pathlib import Path

def gen_csv(path,rows):
    """
    This function takes a list of dictionaries as input and converts it into a CSV file.

    Arguments:
    rows (list): A list of dictionaries where each dictionary represents a row of data.
    Returns: NULL

    Store the CSV file in the docs folder
            
    """
    csv_file_path = Path(path)
    df = pd.DataFrame(rows)

    


    df.to_csv(csv_file_path,mode='a', header=not csv_file_path.exists(), index=False)
