# BBC News Headline Scraper

A lightweight Python script that fetches and extracts the top 5 trending news headlines from [BBC News](https://www.bbc.com/news) using `requests` and `BeautifulSoup`.

---

## 📌 Features

* **HTTP Response Validation:** Verifies page status before parsing.
* **Custom Headers:** Employs a browser `User-Agent` header to prevent request blocking.
* **Data Cleaning:** Automatically strips trailing whitespace, filters duplicate headlines, and excludes empty/short UI text.
* **Graceful Fallbacks:** Handles scenarios where fewer than 5 headlines are returned or requests fail.

---

## 🛠️ Project Structure

```text
headlines/
├── headlines.py       # Main Python script
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/bbc-headline-scraper.git
cd bbc-headline-scraper
```

### 2. Set Up a Virtual Environment

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Script
```bash
python headlines.py
```

---

## 📊 Example Output

```text
$ python headlines.py
1. UN issues urgent call for aid in flood-affected regions
2. Tech giants reveal new AI guidelines at global summit
3. Markets react to central bank rate decision
4. Record-breaking temperatures recorded across Europe
5. Scientists uncover new deep-sea species off Pacific coast
```

---

## ⚙️ How It Works & Edge Case Handling

* **JavaScript Rendering:** Webpages that rely on dynamic JS rendering won't serve full HTML directly via `requests`. For standard HTML headlines on BBC, `requests` + `BeautifulSoup` target the top heading tags (`<h2>`, `<h3>`).
* **Rate Limits / Headers:** Adding standard desktop headers ensures access is permitted by basic anti-scraping filters.