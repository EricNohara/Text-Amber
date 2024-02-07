from urllib.request import urlopen
from urllib.error import URLError

def detect_internet_connection():
    """Return if url can be opened, else keep waiting"""
    while True:
        try:
            response = urlopen('http://74.125.113.99', timeout=1)
            return
        except URLError:
            pass