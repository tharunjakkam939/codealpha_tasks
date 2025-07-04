import requests
import re

def scrape_title(url):
    response = requests.get(url)
    title = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
    if title:
        with open("title.txt", "w") as f:
            f.write(title.group(1))
        print("Page title saved to title.txt")
    else:
        print("Title not found.")

# Example usage
scrape_title("https://www.example.com")
