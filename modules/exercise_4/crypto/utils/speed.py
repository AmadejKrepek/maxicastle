import time


# Function to measure encryption speed
def measure_speed(start_time, data):
    end_time = time.time()
    elapsed_time = end_time - start_time
    speed = (len(data) / (1024 * 1024)) / elapsed_time  # MB/s
    print(f"Encryption Speed: {speed:.2f} MB/s")
