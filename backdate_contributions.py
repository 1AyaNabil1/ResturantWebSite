import datetime
import subprocess
import time

# GitHub personal access token (replace with your own)
TOKEN = "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"
REPO_PATH = "D:/Aya/Github/ResturantWebSite"


# Function to commit a file with a specific date
def commit_with_date(date_str, message):
    with open(f"{REPO_PATH}/contributions.txt", "a") as f:
        f.write(f"Contribution on {date_str}\n")
    cmd = ["git", "-C", REPO_PATH, "commit", "-m", message, "--date", date_str]
    subprocess.run(cmd, check=True)


# Generate commits for past dates
start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 12, 31)
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() in [0, 2, 4]:  # Monday, Wednesday, Friday
        date_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
        commit_with_date(date_str, f"Add contribution for {date_str}")
    current_date += datetime.timedelta(days=1)

# Push to GitHub
subprocess.run(["git", "-C", REPO_PATH, "push"], check=True)
