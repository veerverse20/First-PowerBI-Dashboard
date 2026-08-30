from datetime import datetime

# Append current timestamp to a log file
with open("activity_log.txt", "a") as f:
    f.write(f"Commit logged at: {datetime.now()}\n")
