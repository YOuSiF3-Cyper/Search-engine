import requests
from bs4 import BeautifulSoup

def downloadUrl(url):
    r = requests.get(url)
    if r.status_code != 200 :
        raise Exception('Not OK{}'.format(r.status_code))
    return r.text


def parseText(html):
    # Added 'html.parser' to avoid warnings
    bs = BeautifulSoup(html, 'html.parser')
    
    elements = bs.select('p.mt-4.max-w-prose.text-lg.text-muted')
    
    # Safely check if at least 2 elements exist before grabbing index 1
    if len(elements) > 1:
        return elements[1].text.strip()
    elif len(elements) > 0:
        return elements[0].text.strip() # Fallback to the first one if there isn't a second
    else:
        return "Element not found"        

