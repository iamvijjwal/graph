# 📅 Git Commit Generator

A Python tool that automatically creates random Git commits for a selected 3-month period.

## ✨ Features

•🗓️ Select a 3-month period

•🎲 Generate 4–11 commits per day

•📅 Set custom commit dates

•📝 Update info.txt automatically

•🔀 Create Git commits automatically

•🚀 Push commits to GitHub

•✅ Validate year and period

## 🛠️ Requirements

•Python 3.8+

•Git

•GitHub repository

•Git authentication

### Check versions:

python --version
git --version

🚀 Setup
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY


Create info.txt:

touch info.txt


Project structure:

.
main.py
info.txt
README.md

## ▶️ Usage
python main.py


Choose a year and period:

1 = Jan–Mar
2 = Apr–Jun
3 = Jul–Sep
4 = Oct–Dec


The script generates 4–11 random commits per day, updates info.txt, sets the commit date, and pushes everything to the remote repository.

## ⚠️ Note

A 3-month period can create 360–990 commits. Make sure you're in the correct repository and have Git authentication configured.

GitHub may not always display backdated commits on the contribution graph.

## 🤝 Contributing

Pull requests are welcome.

📜 License

For educational and Git automation purposes.

Made with 🐍 Python and ❤️ Git
