# 📅 Git Commit Generator

A Python utility that automatically generates multiple Git commits for each day within a selected 3-month period of a given year.

✨ Features

🗓️ Generate commits for a selected 3-month period

🎲 Generate 4–11 random commits per day

📅 Set custom commit dates

📝 Automatically update info.txt

🔀 Automatically create Git commits

🚀 Automatically push commits to the remote repository

🎨 Includes terminal credit banners

❌ Validates year and period input

# 📁 Project Structure

.
├── main.py
├── info.txt
└── README.md


🛠️ Requirements

Before running the project, make sure you have:

Python 3.8+

Git

A GitHub repository

Git authentication configured

Check your Python version:

python --version


Check your Git version:

git --version

🚀 Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY

2. Create info.txt

The script requires a file named info.txt.

Linux/macOS:

touch info.txt


Windows PowerShell:

New-Item info.txt

3. Add the Python script

Save the Python code as:

main.py


Your project should look like:

.
├── main.py
├── info.txt
└── README.md

# ▶️ Usage

Run the script:

python main.py


The program will ask for a year:

👉 Enter year (YYYY) ➤ 2025


Then select a 3-month period:

👉 Choose 3 months
(1 = Jan-Mar, 2 = Apr-Jun, 3 = Jul-Sep, 4 = Oct-Dec)➤ 1

📅 Available Periods
Option	Period
1	January – March
2	April – June
3	July – September
4	October – December

Only one period is processed per execution.

🎲 Commit Generation

For every day in the selected period, the script generates a random number of commits between 4 and 11.

commit_count = random.randint(4, 11)


Example:

2025-01-01 → 6 commits
2025-01-02 → 9 commits
2025-01-03 → 4 commits


The exact number of commits will vary because the value is randomly generated.

📝 Commit Messages

Commit messages are generated using this format:

YYYY-MM-DD random commit N


Example:

2025-01-15 random commit 1
2025-01-15 random commit 2
2025-01-15 random commit 3


The info.txt file is updated before every commit.

📅 Commit Dates

The script sets the Git author and committer dates:

env["GIT_AUTHOR_DATE"] = date_str
env["GIT_COMMITTER_DATE"] = date_str


It also uses:

git commit --date DATE


This allows commits to be created with the selected dates.

Note: GitHub may apply its own rules when displaying contribution activity. Setting a commit date does not guarantee that a commit will appear on the contribution graph.

🚀 Git Push

After all commits have been created, the script automatically runs:

git push


Make sure your repository has a configured remote:

git remote -v


Example:

origin  https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git


Test your Git authentication before running the script:

git push

⚙️ Customization
Change the number of commits

Find:

commit_count = random.randint(4, 11)


For example:

commit_count = random.randint(1, 5)


This will generate between 1 and 5 commits per day.

Change the commit message

Find:

msg = f"{commit_date.date()} random commit {i}"


You can change it to:

msg = f"Update - {commit_date.date()} #{i}"

Change the file

At the top of the script:

FILE_PATH = "info.txt"


You can change it to another tracked file:

FILE_PATH = "data.txt"

📊 Approximate Commit Count

A 3-month period contains approximately 90 days.

With 4–11 commits per day, one execution can generate approximately:

360–990 commits


The actual number depends on the randomly generated value for each day.

⚠️ Important

This script can create hundreds of commits in a single execution.

Before running it:

Make sure you are inside the correct repository.

Check that the Git remote is correct.

Make sure you have permission to push.

Make sure info.txt is the file you want to modify.

Consider testing the script in a temporary repository first.

🐛 Troubleshooting
fatal: not a git repository

Make sure you are inside a Git repository.

You can initialize one with:

git init


Or clone an existing repository:

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

git push fails

Check your remote:

git remote -v


Then try:

git push


Make sure your GitHub authentication is configured correctly.

nothing to commit

Make sure:

info.txt exists

info.txt is tracked by Git

The script is modifying the correct file

You are running the script inside the correct repository

🤝 Contributing

Contributions are welcome!

Create a new branch:

git checkout -b feature/your-feature


Make your changes, then:

git add .
git commit -m "Add your feature"
git push origin feature/your-feature


Then open a pull request.

📜 License

This project is provided for educational and Git automation purposes.

You can add your preferred open-source license to the repository.

⭐ Support

If you find this project useful, consider giving the repository a ⭐.

Made with 🐍 Python and ❤️ Git
