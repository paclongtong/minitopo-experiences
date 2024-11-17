import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILE_SIZE = "20MB"
OBJECT1 = "Send_different"
OBJECT2 = "Send_same"
# Function to fetch data from a database for a specific cc_algorithm
def fetch_transfer_times(database, cc_algorithm, db_name):
    connection = sqlite3.connect(database)
    # Define query based on the db_name value
    if db_name == "diffall":
        query = """
        SELECT median_time
        FROM median_transfer_time
        WHERE cc_algorithm = ? AND topology_id BETWEEN 21 AND 40
        """
    elif db_name == 'highbdpnoloss':
        query = """
        SELECT median_time
        FROM median_transfer_time
        WHERE cc_algorithm = ?
        """
    else:
        raise ValueError("Invalid db_name provided. Expected 'diffall' or 'highbdpnoloss'.")

    # Execute query with the specified parameter
    data = pd.read_sql_query(query, connection, params=(cc_algorithm,))
    connection.close()
    return data['median_time'].values

# List of algorithms to fetch and compare
cc_algorithms = ['reno', 'cubic', 'bbr', 'bbr2']

# Paths to the two databases
db1 = '/home/bolong/data_quiche/20MB-2bidi-http09-80topos-highlow-withwithoutloss/experiment_data_diff2.db'
db2 = '/home/bolong/data_quiche/20MB-2bidi-http09-80topos-highlow-withwithoutloss/experiment_data_same_highbdpnoloss.db'

# Plot CDF for each congestion control algorithm
plt.figure(figsize=(12, 8))
for cc_algorithm in cc_algorithms:
    if cc_algorithm == "cubic":
        # Fetch data from both databases
        transfer_times_db1 = fetch_transfer_times(db1, cc_algorithm, "diffall")
        transfer_times_db2 = fetch_transfer_times(db2, cc_algorithm, 'highbdpnoloss')

        # Sort times and calculate CDF for db1
        sorted_times_db1 = np.sort(transfer_times_db1)
        cdf_db1 = np.arange(1, len(sorted_times_db1) + 1) / len(sorted_times_db1)
        plt.plot(sorted_times_db1, cdf_db1, label=f'{cc_algorithm} (Different path)')

        # Sort times and calculate CDF for db2
        sorted_times_db2 = np.sort(transfer_times_db2)
        cdf_db2 = np.arange(1, len(sorted_times_db2) + 1) / len(sorted_times_db2)
        plt.plot(sorted_times_db2, cdf_db2, label=f'{cc_algorithm} (Same path)', linestyle='--')

# Set plot labels and title
plt.xlabel('Transfer Time')
plt.ylabel('CDF')
# plt.yscale('log')
plt.title(f'CDF of Transfer Time from {OBJECT1} and {OBJECT2} - {FILE_SIZE}')
plt.legend()
plt.grid(True)
plt.show()
