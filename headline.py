import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_headlines():
    try:
        # Fetch the page with requests
        response = requests.get(URL, headers=headers, timeout=10)
        
        # Check the status code before parsing
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch the webpage: {e}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # BBC news headlines are typically found within h2 or h3 heading tags
    candidate_tags = soup.find_all(["h2", "h3"])
    
    headlines = []
    seen = set()

    for tag in candidate_tags:
        # Strip whitespace
        text = tag.get_text(strip=True)
        
        # Skip empty entries, very short UI snippets, and duplicates
        if text and len(text) > 10 and text not in seen:
            seen.add(text)
            headlines.append(text)
            
        # Stop once we have enough candidates
        if len(headlines) >= 5:
            break

    # Handle the case where fewer than 5 headlines are found
    if not headlines:
        print("No headlines could be extracted.")
        return

    # Print exactly the collected headlines (up to 5) numbered 1 to 5
    for i, headline in enumerate(headlines[:5], 1):
        print(f"{i}. {headline}")

if __name__ == "__main__":
    fetch_headlines()