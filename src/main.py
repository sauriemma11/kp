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
            # print(file_path)
            datetime, subtr = kpplt.load_subtr_data(file_path)
            datetime_list.extend(datetime)
            subtr_list.extend(subtr)
    # print(subtr_list)

    kp_mask = kp.createkpMask(dfkp, datetime_list)

    # print(len(kp_mask))
    # print(len(datetime_list))

    filtered_subtr_list = kp.set_subtr_to_nan_where_kp_over(subtr_list, kp_mask)

    print(len(filtered_subtr_list))
    print(filtered_subtr_list[180:181])
    print(datetime[180])

    # print(subtr_list)