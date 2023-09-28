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

def plot_subtr_and_kp(data, dfkp):
    """
    Plot combined data with multiple subplots.

    Args:
        data (dict): Dictionary containing data.
        dfkp (pd.DataFrame): Pandas DataFrame containing Kp data.
    """
    # Extract the data from the dictionary
    datetime = pd.to_datetime(data['datetime'])
    subtraction = data['subtraction']
    std_dev_1hour = data['std_dev_1hour']
    std_dev_daily = data['std_dev_daily']
    kp_3hr = data['kp']

    # Create a Pandas DataFrame with datetime as the index
    df = pd.DataFrame({'subtraction': subtraction, 'std_dev_1hour': std_dev_1hour, 'std_dev_daily': std_dev_daily, 'kp': kp_3hr}, index=datetime)

    # Create separate plots for Subtraction Data, 1-Hour Std Deviation, and Daily Std Deviation
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 8))

    # Plot for Subtraction Data (Minute-by-Minute)
    ax1.plot(df.index, df['subtraction'], color='blue')
    ax1.set_ylabel('Subtraction [nT]')
    ax1.set_title('(GK2A - T89) - (G17 - T89) |B|')

    # Plot for 1-Hour Standard Deviation
    ax2.plot(std_dev_1hour.index, std_dev_1hour, color='green')
    ax2.set_ylabel('Std Deviation')
    ax2.set_title('1-Hour Standard Deviation')

    # Plot for Daily Standard Deviation
    ax3.plot(std_dev_daily.index, std_dev_daily, color='red')
    ax3.set_ylabel('Std Deviation')
    ax3.set_title('Daily Standard Deviation')

    # Plot Kp Value (3 hr)
    ax4.plot(dfkp['Time'], dfkp['Kp'])
    ax4.set_ylabel('Kp Value')
    ax4.set_xlabel('Time')
    ax4.set_title('Kp Value (3 hr)')

    # Adjust subplot spacing
    plt.tight_layout()

    # Show the plots
    plt.show()

# Example usage of the function
# You can call plot_combined_data(data, dfkp) with your data and Kp DataFrame as arguments.
