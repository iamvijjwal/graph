import os
import json
import subprocess
import random
from datetime import datetime, timedelta

FILE_PATH = "info.txt"

# -------------------------------
# Credit Banner (Start)
# -------------------------------
def show_start_credit():
    print(r"""       
┏┓• ┓┏  ┓   ┏┓        •   ┓   ┓ 
┃┓┓╋┣┫┓┏┣┓  ┃ ┏┓┏┳┓┏┳┓┓╋  ┃ ┏┓┣┓
┗┛┗┗┛┗┗┻┗┛  ┗┛┗┛┛┗┗┛┗┗┗┗  ┗┛┗┻┗┛                       
""")
# -------------------------------
# Credit Banner (End)
# -------------------------------
def show_end_credit():
    print(r"""
┳┳┓┳┏┓┏┓┳┏┓┳┓  ┏┓┏┓┏┓┏┓┏┓┳┓  ╻
┃┃┃┃┗┓┗┓┃┃┃┃┃  ┃┃┣┫┗┓┗┓┣ ┃┃  ┃
┛ ┗┻┗┛┗┛┻┗┛┛┗  ┣┛┛┗┗┛┗┛┗┛┻┛  •
""")

# -------------------------------
# Git Commit (FIXED)
# -------------------------------
def git_commit(message, commit_date):
    subprocess.run(["git", "add", FILE_PATH], check=True)

    env = os.environ.copy()
    date_str = commit_date.strftime("%Y-%m-%dT12:00:00")

    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str

    subprocess.run(
        [
            "git",
            "commit",
            "-m",
            message,
            "--date",
            date_str
        ],
        env=env,
        check=True
    )

    print(f"{message} successful ✔️")


def git_push():
    subprocess.run(["git", "push"], check=True)


def first_sunday(year):
    d = datetime(year, 1, 1)
    while d.weekday() != 6:  # Sunday
        d += timedelta(days=1)
    return d


def make_commits_for_year():
    year_input = input("👉 Enter year (YYYY) ➤ ")

    try:
        year = int(year_input)
        if year < 1:
            raise ValueError
    except ValueError:
        print("❌ Invalid year. Please use YYYY.")
        return

    part = input("👉 Choose 3 months"
                 "(1 = Jan-Mar, 2 = Apr-Jun, 3 = Jul-Sep, 4 = Oct-Dec)➤ ").strip()

    if part == "1":
        start_month = 1
        end_month = 3
        period_name = "January-March"

    elif part == "2":
        start_month = 4
        end_month = 6
        period_name = "April-June"

    elif part == "3":
        start_month = 7
        end_month = 9
        period_name = "July-September"

    elif part == "4":
        start_month = 10
        end_month = 12
        period_name = "October-December"

    else:
        print("❌ Invalid choice. Enter 1, 2, 3, or 4.")
        return


    total_commits = 0

    print(f"\n📅 Year: {year}\n")

    for month in range(start_month, end_month + 1):

        # Find number of days in this month
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)

        days_in_month = (next_month - timedelta(days=1)).day

        print(f"🗓️ {datetime(year, month, 1).strftime('%B %Y')}")

        for day in range(1, days_in_month + 1):
            commit_date = datetime(year, month, day)

            # Random number of commits between 4 and 11
            commit_count = random.randint(4, 11)

            print(
                f"📅 {commit_date.strftime('%Y-%m-%d')} "
                f"→ {commit_count} commits"
            )

            for i in range(1, commit_count + 1):
                msg = f"{commit_date.date()} random commit {i}"

                with open(FILE_PATH, "w") as f:
                    f.write(msg)

                git_commit(msg, commit_date)
                total_commits += 1

    git_push()

    print(
        f"\n☑️ Finished! Created {total_commits} commits "
        f"for {year} from {period_name}"
    )

# -------------------------------
# Entry Point
# -------------------------------
if __name__ == "__main__":
    show_start_credit()

    make_commits_for_year()

    show_end_credit()