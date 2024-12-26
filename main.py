import time
import requests
from bs4 import BeautifulSoup

class Scraper: 
    def __init__(self, params={
        "proxies": {},
        "headers": {},
        "rate_limit": 1000,
    }):
        self.params = params
        self.last_request_time = self.params["rate_limit"]+1

    def get(self, url, params={}):
        try:
            current_time = int(time.time() * 1000)
            if hasattr(self, 'last_request_time'):
                time_diff = current_time - self.last_request_time
                if time_diff < self.params["rate_limit"]:
                    print(f"Rate limit exceeded. Sleeping for {self.params['rate_limit'] - time_diff} seconds")
                    time.sleep((self.params["rate_limit"] - time_diff) / 1000)
                    
            response = requests.get(url)
            
            self.last_request_time = current_time
            if response.status_code == 200:
                return BeautifulSoup(response.text, 'lxml')
            else:
                print(f"Failed to fetch {url}: Status code {response.status_code}")
                return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
