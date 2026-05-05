"""
Mini-project: Simple web page title scraper using stdlib

Usage:
  python 12_web_title_scraper.py https://example.com
"""
import sys
from urllib.request import urlopen


def fetch_title(url):
    try:
        with urlopen(url, timeout=10) as r:
            html = r.read(4096).decode(errors="ignore")
            start = html.find("<title>")
            end = html.find("</title>")
            if start != -1 and end != -1:
                return html[start + 7:end].strip()
            return "(no title found)"
    except Exception as e:
        return f"Error: {e}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python 12_web_title_scraper.py <url>")
        return
    url = sys.argv[1]
    print(fetch_title(url))


if __name__ == "__main__":
    main()
