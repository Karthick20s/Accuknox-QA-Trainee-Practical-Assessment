import requests
from datetime import datetime
import time

def check_application_status(url):
    try:
        # Send a GET request to the application
        response = requests.get(url, timeout=5)
        
        # Check if status code indicates the application is "up"
        if response.status_code == 200:
            return "UP", response.status_code
        else:
            return "DOWN", response.status_code
    except requests.exceptions.RequestException as e:
        # Any exception means the application is likely down
        return "DOWN", str(e)

def generate_report(status, status_code):
    # Log the status to a file with a timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_message = f"{timestamp} - Application is {status} (Status Code: {status_code})"
    with open("application_health_report.log", "a") as log_file:
        log_file.write(report_message + "\n")
    print(report_message)

def main():
    # Application configuration
    application_url = "https://www.facebook.com/"
  # Replace with your application URL
    check_interval = 5  # Time between checks, in seconds

    print(f"Starting health check for {application_url}")
    while True:
        # Check the application's status
        status, status_code = check_application_status(application_url)
        
        # Generate a report based on the check
        generate_report(status, status_code)
        
        # Wait before checking again
        time.sleep(check_interval)

if __name__ == "__main__":
    main()
