# 🐢 Turtle Families Web Scraping Project

## 📌 Project Overview
This project demonstrates a **web scraping implementation using Python** to extract data from the **Frames & iFrames** section of the *Scrape This Site* website.

The main goal of this project is to:
- Understand how **iframes** work in web pages
- Perform scraping from iframe-based content
- Navigate from a list page to detail pages
- Store scraped data into a structured CSV file

---

## 🌐 Data Source
Website used in this project:

https://www.scrapethissite.com/pages/frames/

Iframe source:
https://www.scrapethissite.com/pages/frames/?frame=i


---

## 📊 Extracted Data
For each Turtle Family, the following data is collected:
- **Name** — Turtle family name
- **Description** — Detailed description of the turtle family

The final output is saved as:
turtle_details.csv


---

## 🛠️ Tech Stack
This project is built using:
- **Python 3**
- **requests** — for HTTP requests
- **BeautifulSoup (bs4)** — for HTML parsing
- **pandas** — for data manipulation and CSV export

---

## 📁 Project Structure
├── turtle_scraper.py
├── turtle_details.csv
└── README.md


---

## ⚙️ How the Scraper Works
1. Access the iframe source page to retrieve Turtle Family cards
2. Extract turtle family names from the iframe page
3. Build new URLs using family names to access detail pages
4. Extract detailed descriptions from each family page
5. Store results as a list of dictionaries
6. Convert data into a pandas DataFrame
7. Export the final dataset to a CSV file

---
