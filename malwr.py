# Author: Akbar Qureshi						

import requests
from bs4 import *
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36'
}

try:
	r = requests.get('https://malwr.com/', headers=headers)
except requests.exceptions.RequestException as e:
	print e
	sys.exit(1)

soup = BeautifulSoup(r.text,'html.parser')
for recent_domains in soup.findAll('span')[13:]:
	print recent_domains.text
