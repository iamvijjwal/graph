📅 GitHub Commit Generator

A simple Python utility that automatically creates multiple Git commits for each day across a selected 3-month period of a given year.

You can choose one of four quarters:

January – March

April – June

July – September

October – December

The script generates a random 4–11 commits per day, updates info.txt for every commit, creates commits with the selected date, and finally pushes everything to the configured Git remote.

⚠️ Important: This tool is intended for testing, Git experimentation, contribution-graph experimentation, and learning Git automation. Do not use it to misrepresent professional activity, project history, or contributions.

✨ Features

🗓️ Generate commits for an entire 3-month period

🎲 Randomly generate 4–11 commits per day

📅 Assign commits to specific historical dates

📝 Automatically update info.txt

🔀 Automatically stage and commit changes

🚀 Push all commits to the remote repository

🎨 Includes customizable terminal credit banners

❌ Basic validation for year and quarter selection

📁 Project Structure
.
├── main.py
├── info.txt
└── README.md


You can name the Python file whatever you prefer. In the examples below, it is assumed to be main.py.

🛠️ Requirements

Make sure you have:

Python 3.8+

Git

A GitHub repository

Git configured with your username and email

A configured Git remote

Check your installations:

python --version
git --version


Configure Git if you haven't already:

git config --global user.name "Your Name"
git config --global user.email "you@example.com"

🚀 Installation
1. Clone your repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY

2. Create the required file

The script expects a file named:

info.txt


You can create it with:

touch info.txt


On Windows PowerShell:

New-Item info.txt

3. Add the Python script

Save the provided Python code as:

main.py


Your repository should now look like:

.
├── main.py
├── info.txt
└── README.md

▶️ Usage

Run the script:

python main.py


The program will ask you to enter a year:

👉 Enter year (YYYY) ➤ 2025


Then select a 3-month period:

👉 Choose 3 months
(1 = Jan-Mar, 2 = Apr-Jun, 3 = Jul-Sep, 4 = Oct-Dec)➤ 1


The script will then process every day in the selected period.

Example:

📅 Year: 2025

🗓️ January 2025
📅 2025-01-01 → 7 commits
📅 2025-01-02 → 5 commits
📅 2025-01-03 → 9 commits
...


For each commit, the script:

Writes a message to info.txt

Stages info.txt

Creates a Git commit

Assigns the selected date to the commit

Continues until the entire period is complete

At the end, it runs:

git push

📊 Commit Generation

Each day receives a random number of commits between:

4 → 11 commits


For example:

2025-01-01 → 6 commits
2025-01-02 → 11 commits
2025-01-03 → 4 commits


Because the number is generated using Python's random module, the exact number of commits will differ each time.

📝 Commit Messages

Generated commit messages follow this format:

YYYY-MM-DD random commit N


For example:

2025-01-15 random commit 1
2025-01-15 random commit 2
2025-01-15 random commit 3


The corresponding info.txt file is updated before every commit.

📅 Supported Periods
Choice	Period
1	January – March
2	April – June
3	July – September
4	October – December

Only one period is processed per execution.

If you want to process the entire year, run the program four times and select each period.

🔐 Git Authentication

The script uses your existing Git configuration and executes:

git push


Therefore, your repository must already have a working remote and authentication method.

Check your remote with:

git remote -v


Example:

origin  https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git (fetch)
origin  https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git (push)


If Git authentication is not configured, the final push will fail.

⚠️ Important Notes
Historical commit dates

The script sets:

GIT_AUTHOR_DATE
GIT_COMMITTER_DATE


and also uses Git's:

--date


option to assign the generated commits to the selected dates.

Large number of commits

A 3-month period can create thousands of commits.

There are approximately 90 days in a quarter, and at 4–11 commits per day this can result in roughly:

360–990 commits


The exact number depends on the random values generated.

Creating and pushing hundreds of commits can take some time.

GitHub contribution graph

GitHub's contribution graph has its own rules for determining whether commits count toward contributions. Simply creating commits with historical dates does not guarantee that they will appear as expected.

Backup your repository

Always make sure you are running this against the intended repository.

The script modifies:

info.txt


and creates many Git commits automatically.

🧪 Example

Suppose you run:

Year: 2025
Period: 1


The script processes:

January 2025
February 2025
March 2025


A day might produce:

📅 2025-01-01 → 5 commits

2025-01-01 random commit 1
2025-01-01 random commit 2
2025-01-01 random commit 3
2025-01-01 random commit 4
2025-01-01 random commit 5


After all days have been processed, the script automatically pushes the commits:

git push

🧩 Customization

You can easily modify the script.

Change the number of commits per day

Find:

commit_count = random.randint(4, 11)


For example:

commit_count = random.randint(1, 5)

Change the commit message

Find:

msg = f"{commit_date.date()} random commit {i}"


You could change it to:

msg = f"Update documentation - {commit_date.date()} #{i}"

Change the file being modified

At the top of the script:

FILE_PATH = "info.txt"


Change it to another tracked file:

FILE_PATH = "data.txt"

🐛 Troubleshooting
fatal: not a git repository

Make sure you run the script inside a Git repository:

git init


or clone an existing repository:

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

nothing to commit

Git only creates a commit when there is a change to commit. Make sure the file specified by FILE_PATH is tracked and actually changes between commits.

git push fails

Check your remote:

git remote -v


Then test:

git push


manually.

Permission denied

Make sure your GitHub authentication is configured correctly and that you have write access to the repository.

📜 License

This project is provided for educational and experimentation purposes. Add your preferred license to the repository if you plan to distribute the project.

⭐ Contributing

Contributions, improvements, and bug fixes are welcome.

To contribute:

git fork


Create a branch:

git checkout -b feature/improvement


Make your changes, commit them, and open a pull request.

👨‍💻 Author

Created as a Python/Git automation project for experimenting with automated Git workflows.

If you find the project useful, consider giving the repository a ⭐.
