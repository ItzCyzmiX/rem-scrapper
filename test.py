from rem_scraper import Scraper

scraper = Scraper()
html = scraper.get("https://www.example.com")
print(html.select('p')[0].text)
