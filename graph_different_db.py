import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to fetch data from a database for a specific cc_algorithm
def fetch_transfer_times(database, cc_algorithm):
    connection = sqlite3.connect(database)
    query = """
    SELECT median_time
    FROM median_transfer_time
    WHERE cc_algorithm = ?
    """
    data = pd.read_sql_query(query, connection, params=(cc_algorithm,))
    connection.close()
    return data['median_time'].values

# List of algorithms to fetch and compare
cc_algorithms = ['reno', 'cubic', 'bbr', 'bbr2']

# Paths to the two databases
db1 = '/home/bolong/data_quiche/1106_send_diff_wrote_10mB/experiment_data.db'
db2 = '/home/bolong/data_quiche/1030 multipath_ack_default/experiment_data.db'

# Plot CDF for each congestion control algorithm
plt.figure(figsize=(12, 8))
for cc_algorithm in cc_algorithms:
    # if cc_algorithm == "cubic":
        # Fetch data from both databases
        transfer_times_db1 = fetch_transfer_times(db1, cc_algorithm)
        transfer_times_db2 = fetch_transfer_times(db2, cc_algorithm)
        
        # Sort times and calculate CDF for db1
        sorted_times_db1 = np.sort(transfer_times_db1)
        cdf_db1 = np.arange(1, len(sorted_times_db1) + 1) / len(sorted_times_db1)
        
        # Sort times and calculate CDF for db2
        sorted_times_db2 = np.sort(transfer_times_db2)
        cdf_db2 = np.arange(1, len(sorted_times_db2) + 1) / len(sorted_times_db2)
        
        # Plot the CDF curves from both databases
        plt.plot(sorted_times_db1, cdf_db1, label=f'{cc_algorithm} (Send_differnt_multi)')
        plt.plot(sorted_times_db2, cdf_db2, label=f'{cc_algorithm} (Send_default)', linestyle='--')

# Set plot labels and title
plt.xlabel('Transfer Time')
plt.ylabel('CDF')
plt.yscale('log')
plt.title('CDF of Transfer Time for Different Congestion Control Algorithms from Two ACK Strategies - 10MB')
plt.legend()
plt.grid(True)
plt.show()