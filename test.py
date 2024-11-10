import re
import sqlite3
import time
def extract_times_from_log(file_path):
    time_pattern = re.compile(r'response\(s\) received in (\d+\.\d+)(ms|s)')
    times = []
    
    with open(file_path, 'r') as file:
        for line in file:
            match = time_pattern.search(line)
            if match:
                time_value, unit = match.groups()
                time_value = float(time_value)
                if unit == 'ms':  # Convert milliseconds to seconds
                    time_value /= 1000
                times.append(time_value)
    
    # print(f"time: {times}")
    return times

def save_times_to_file(times, output_file):
    with open(output_file, 'a') as f:
        for time in times:
            f.write(f'{time}\n')

# Function to store time values in a SQLite database
def store_times_in_db(times, db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS response_times (id INTEGER PRIMARY KEY, time_value REAL)''')
    
    for time in times:
        c.execute("INSERT INTO response_times (time_value) VALUES (?)", (time,))
    
    conn.commit()
    conn.close()
    
# Adpoted
def extract_transfer_time(file_path):
    # Updated regex to prioritize seconds (s) over milliseconds (ms)
    transfer_time_pattern = r"response\(s\) received in (\d+\.\d+)(s|ms)"

    # Open and read the log file content
    with open(file_path, 'r') as log_file:
        for line in log_file:
            # Try to match the regex pattern in the current line
            match = re.search(transfer_time_pattern, line)
            if match:
                time_value = float(match.group(1))
                unit = match.group(2)

                # Convert seconds to milliseconds, prioritize seconds
                if unit == 'ms':
                    time_value /= 1000  # Convert seconds to seconds
                return time_value
    return None

if __name__ == "__main__":
    # start_time = time.time()
    # # for i in range (10000):   
    # times = extract_times_from_log("/dev/shm/quiche_client.log")
    # save_times_to_file(times, output_file="/dev/shm/time_storage")
    #     # times = extract_times_from_log("/home/bolong/minitopo-experiences/quiche_20241021_172735_quic/0_d84.1qs0.954b51.83_1_d106.1qs1.269b45.38_nt_0_0_loss_1.56%_nt_1_0_loss_1.19%/quic/1/quiche_client.log")
    #     # save_times_to_file(times, output_file="/home/bolong/minitopo-experiences/quiche_20241021_172735_quic/0_d84.1qs0.954b51.83_1_d106.1qs1.269b45.38_nt_0_0_loss_1.56%_nt_1_0_loss_1.19%/quic/1/time_storage")
        
    # end_time = time.time()
    # execution_time = end_time - start_time
    # print(f"Time: {execution_time}")
    extract_transfer_time("/home/bolong/minitopo-experiences/quiche_20241021_171218_quic/0_d84.1qs0.954b51.83_1_d106.1qs1.269b45.38_nt_0_0_loss_1.56%_nt_1_0_loss_1.19%/quic/1/quiche_client.log")