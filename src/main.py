import pickle
import matplotlib.pyplot as plt
import os
import kp_data_plotting as kpplt
import kp_data_processing as kp

if __name__ == '__main__':
    csv_file_location = 'C:/Users/sarah.auriemma/Desktop/Data_new/kp_2019.txt'
    dfkp = kp.readKpData(csv_file_location)
    print(dfkp)
    # kpplt.plotKpData(dfkp)

    # Plot filtered kp:
    filtered_data = kp.filterKpData(dfkp, max_kp=2)

    # loading subtr data:
    pickle_dir = 'Z:/Data/sos-89-goes-89/g17/subtr_pickles/'  # Change to your directory path
    datetime_list = []
    subtr_list = []

    for filename in os.listdir(pickle_dir):
        if filename.endswith('.pickle'):
            file_path = os.path.join(pickle_dir, filename)
            datetime, subtr = kpplt.load_subtr_data(file_path)
            datetime_list.extend(datetime)
            subtr_list.extend(subtr)

    kp_mask = kp.createkpMask(dfkp, datetime_list)
    filtered_subtr_list = kp.set_subtr_to_nan_where_kp_over(subtr_list, kp_mask)

# Todo: take std dev hourly, daily
# Todo: plot std dev like we had in scratch4


    hour_stddev = kp.calc_hourly_stddev(datetime_list, subtr_list)
    plt.plot(hour_stddev)
    plt.show()