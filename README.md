# 🖼️ Meme Image & Metadata Scraper
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) <br>
A Python script that scrapes memes, titles, and authors from [Imgflip.com](https://imgflip.com/), downloads the images, and saves the metadata to CSV and JSON files.

---

## 🚀 Features
- Scrapes meme title, author, and image URL
- Downloads `.jpg` and `.gif` image formats
- Saves metadata into:
  - `meme.csv` — structured tabular data
  - `meme.json` — readable JSON array
- Cleans filenames to avoid special character issues
- Automatically handles folders and file overwriting

---

## 🛠️ Technologies Used
- Python
- Requests
- BeautifulSoup
- JSON
- CSV
- Regex

---

## 🚀 How It Works
1. Run the script
2. It will:
  - Scrape memes from multiple pages of Imgflip.com
  - Save memes in the images/ folder
  - Export metadata to meme.csv and meme.json

---

## 👤 Author
Written with passion by – @FaresSaleemGHub

---

## 📜 License
This project is open-source and available under the MIT License.
