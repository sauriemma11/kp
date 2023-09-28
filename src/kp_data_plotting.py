import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle
import kp_data_processing as kp


def plotKpData(df, max_kp=None, title=None):
    """

    :param df: dataframe containing kp data
    :return:
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df['Time'], df['Kp'], linestyle='-')
    if title:
        plt.title(title)
    else:
        plt.title('Kp over Time')
    plt.xlabel('Time')
    plt.ylabel('Kp Value')
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)
    # Adjust y-axis based on kp input data (for nicer looking filtered data plots)

    if max_kp == None:
        ylim = max(df['Kp'][:]) + 0.2

        plt.axhline(y=2.0, color='red', linestyle='--')

    else:
        ylim = float(max_kp + 1.0)


    # Delete this line
    ylim = 5
    # print(max_kp)

    plt.ylim(0, ylim)
    # print(max_kp, type(max_kp))
    plt.show()


def load_subtr_data(file_path):
    """
    Load subtraction data from a pickle file.

    Args:
        file_path (str): The path to the pickle file containing the data.

    Returns:
        tuple: A tuple containing datetime values and subtraction data.
               - datetime_list (list): List of datetime values.
               - subtr_list (list): List of subtraction data.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
        Exception: If there's an issue with loading the data from the file.
    """
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
            # print(file)
            # Assuming data is a dictionary with keys 'datetime' and 'subtraction'
            datetime_list = data.get('datetime', [])
            subtr_list = data.get('subtration', [])

            # You can perform additional data validation or manipulation here if needed

            return datetime_list, subtr_list

    except FileNotFoundError:
        raise FileNotFoundError(f"File not found at {file_path}")

    except Exception as e:
        raise Exception(f"Error loading data from {file_path}: {str(e)}")
