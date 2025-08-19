Atlas Back-End API

Overview

This repository contains Python scripts to gather data from an API and export it in multiple formats (CSV, JSON, or Python dictionary). It was built as part of my work on the Atlas back-end project to handle structured data efficiently.

Features

Fetch data from a remote API

Export data to CSV and JSON formats

Convert API data into Python dictionaries for further processing

Includes error handling and proper resource management

Tech Stack
<p> <img alt="Python" src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" /> <img alt="VS Code" src="https://img.shields.io/badge/-VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" /> <img alt="Prettier" src="https://img.shields.io/badge/-Prettier-F7B93E?style=flat-square&logo=prettier&logoColor=white" /> <img alt="Postman" src="https://img.shields.io/badge/-Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" /> <img alt="MySQL" src="https://img.shields.io/badge/-MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" /> <img alt="PostgreSQL" src="https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" /> </p>
Usage

Clone the repo:

git clone https://github.com/SpaceDandy15/atlas-back-end.git
cd atlas-back-end/api


Install dependencies (if any):

pip install -r requirements.txt


Run scripts:

python 0-gather_data_from_an_API.py
python 1-export_to_CSV.py
python 2-export_to_JSON.py
python 3-dictionary_of_list_of_dictionaries.py

Challenges & Lessons Learned

Handling API rate limits and errors

Properly closing files and resources to avoid memory leaks

Structuring data for multiple export formats

Writing reusable Python scripts for data processing

About Me

Hi, I’m Malik Vance, a Fullstack Software Engineer passionate about bridging the gap between hardware and software.

LinkedIn

Portfolio

Support Me
<a href="https://www.buymeacoffee.com/SpaceDandy15" target="_blank"> <img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" > </a>
