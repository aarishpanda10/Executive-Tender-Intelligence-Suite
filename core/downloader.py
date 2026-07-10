import requests
from pathlib import Path


class Downloader:

    def __init__(self):
        self.cache = Path("cache")
        self.cache.mkdir(exist_ok=True)

    def download(self, url, filename):

        file = self.cache / filename

        try:
            r = requests.get(url, timeout=30)

            if r.status_code == 200:
                file.write_bytes(r.content)
                return file

        except Exception as e:
            print(e)

        return None
