import random
import time

class JavaLogGenerator:
    def __init__(self, log_file):
        self.log_file = log_file

    def generate_log(self, severity, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} [{severity}] - {message}\n"
        with open(self.log_file, "a") as file:
            file.write(log_entry)

    def simulate_logs(self, num_logs):
        severities = ["INFO", "WARNING", "ERROR"]
        messages = [
            "Application started",
            "Processing request",
            "Database connection failed",
            "Invalid input",
            "User authentication successful",
            "File not found",
            "Server overloaded",
            "Request timeout",
            "Configuration file updated",
            "Security alert: unauthorized access attempt",
            "Email sent successfully",
            "Memory allocation error",
            "Task completed",
            "System reboot initiated",
            "Network connection lost"
        ]
        for _ in range(num_logs):
            severity = random.choice(severities)
            message = random.choice(messages)
            self.generate_log(severity, message)

if __name__ == "__main__":
    log_generator = JavaLogGenerator("./java_logs.txt")
    log_generator.simulate_logs(1000)