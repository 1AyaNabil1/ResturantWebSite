import datetime
import subprocess
import os

# GitHub personal access token (replace with your own, or remove if not needed)
TOKEN = "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"
REPO_PATH = "D:/Aya/Github/ResturantWebSite"


# Function to commit a file with a specific date and varying contribution levels
def commit_with_date(date_str, message, lines=1):
    with open(f"{REPO_PATH}/contributions.txt", "a") as f:
        for _ in range(lines):
            f.write(f"Contribution on {date_str}\n")
    cmd_add = ["git", "-C", REPO_PATH, "add", "contributions.txt"]
    subprocess.run(cmd_add, check=True)
    cmd_commit = ["git", "-C", REPO_PATH, "commit", "-m", message, "--date", date_str]
    subprocess.run(cmd_commit, check=True)


# Generate commits for past dates with varying contribution levels
start_date = datetime.datetime(2025, 1, 1)
end_date = datetime.datetime(2025, 7, 6)
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() in [0, 2, 4]:  # Monday, Wednesday, Friday
        date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
        # Vary the number of lines based on month for color gradient
        if current_date.month in [1, 2, 3]:  # Jan-Mar: 1 line (light green)
            commit_with_date(date_str, f"Add contribution for {date_str}", lines=1)
        elif current_date.month in [4, 5, 6]:  # Apr-Jun: 5 lines (medium green)
            commit_with_date(date_str, f"Add contribution for {date_str}", lines=5)
        else:  # Jul-Dec: 10 lines (dark green)
            commit_with_date(date_str, f"Add contribution for {date_str}", lines=10)
    current_date += datetime.timedelta(days=1)

# Push to GitHub
subprocess.run(["git", "-C", REPO_PATH, "push"], check=True)
