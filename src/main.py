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
    filtered_datetime_list = kp.set_subtr_to_nan_where_kp_over(datetime_list, kp_mask)
    #
    #
    # plt.plot(filtered_subtr_list)
    # plt.show()

# Todo: take std dev hourly, daily
# Todo: plot std dev like we had in scratch4


    # Hour_stddev1 is our original data, 2 is the data with the kp mask applied
    hour_stddev1 = kp.calc_hourly_stddev(datetime_list, subtr_list)
    hour_stddev2 = kp.calc_hourly_stddev(filtered_datetime_list,filtered_subtr_list)

    daily_stddev1 = kp.calc_daily_stddev(datetime_list, subtr_list)
    daily_stddev2 = kp.calc_daily_stddev(filtered_datetime_list, filtered_subtr_list)



    fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1, figsize=(12, 8))

    ax1.plot(filtered_subtr_list)
    ax1.set_ylim(0, 100)
    ax1.set_ylabel('filtered\nsubtraction data')

    ax2.plot(hour_stddev2.index, hour_stddev2)
    ax2.set_ylabel('std dev\nhourly\nfiltered')
    ax2.set_ylim(0, 20)

    ax3.plot(hour_stddev1.index, hour_stddev1)
    ax3.set_ylabel('std dev\nhourly')
    ax3.set_ylim(0,20)

    ax4.plot(subtr_list)
    ax4.set_ylim(0, 100)
    ax4.set_ylabel('subtraction data')

    ax5.plot(dfkp['Kp'])
    ax5.set_ylabel('kp')

    ax6.plot(daily_stddev1.index, daily_stddev1)
    ax6.set_ylabel('daily stddev')

    ax7.plot(daily_stddev2.index, daily_stddev2)
    ax7.set_ylabel('D stddev\nfiltered')

    plt.show()

    mean_data_before = kp.mean_std_dev(hour_stddev1)
    mean_data_after = kp.mean_std_dev(hour_stddev2)

    mean_D_before = kp.mean_std_dev(daily_stddev1)
    mean_D_after = kp.mean_std_dev(daily_stddev2)

    print(f'Mean hourly stddev before filter {mean_data_before}')
    print(f'Mean hourly stddev after filter {mean_data_after}')


    print(f'Mean daily stddev before filter {mean_D_before}')
    print(f'Mean daily stddev after filter {mean_D_after}')