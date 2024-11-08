import psutil
import logging
from datetime import datetime
import time

# Set up logging configuration
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Thresholds
CPU_THRESHOLD = 80  # CPU usage percentage
MEMORY_THRESHOLD = 80  # Memory usage percentage
DISK_THRESHOLD = 80  # Disk usage percentage
PROCESS_THRESHOLD = 200  # Number of processes

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"ALERT: CPU usage is at {cpu_usage}%")

def check_memory():
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
        print(f"ALERT: Memory usage is at {memory_usage}%")

def check_disk():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        logging.warning(f"Low Disk Space detected: {disk_usage.percent}% used")
        print(f"ALERT: Disk space usage is at {disk_usage.percent}%")

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        logging.warning(f"High Number of Processes detected: {process_count} processes running")
        print(f"ALERT: Process count is at {process_count}")

def monitor_system():
    print("Starting system health monitoring...")
    while True:
        check_cpu()
        check_memory()
        check_disk()
        check_processes()
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    try:
        monitor_system()
    except KeyboardInterrupt:
        print("Monitoring stopped.")
