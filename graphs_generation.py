import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import os


exp_type = "1106-send-diff-only-20mB"
exp_type_name = "Different-path ACK Strategy Two-Bidi 20MB Transfer"
db_path = os.path.join('/home/bolong/data_quiche', exp_type, 'experiment_data.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch transfer times for each congestion control algorithm
query = "SELECT cc_algorithm, median_time FROM median_transfer_time"
cursor.execute(query)
data = cursor.fetchall()
conn.close()


algorithms = {}
for cc_algorithm, median_time in data:
    if cc_algorithm not in algorithms:
        algorithms[cc_algorithm] = []
    algorithms[cc_algorithm].append(median_time)

# Plot CDF for each congestion control algorithm
plt.figure(figsize=(8, 6))

for cc_algorithm, times in algorithms.items():
    sorted_times = np.sort(times)
    cdf = np.arange(1, len(sorted_times) + 1) / len(sorted_times)
    plt.plot(sorted_times, cdf, label=cc_algorithm)


plt.xlabel("Transfer Time (seconds)", fontsize=20)
plt.ylabel("CDF", fontsize = 20)
plt.title(f"{exp_type_name}", fontsize = 16)
plt.legend(title="Congestion Control Algorithm", title_fontsize=18, fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
plt.yscale('linear')


plt.show()
filename = f"/home/bolong/data_quiche/graphs/{exp_type}.svg"
# plt.savefig(filename, format="svg", bbox_inches="tight")
