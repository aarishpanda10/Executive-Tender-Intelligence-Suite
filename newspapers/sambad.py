from datetime import datetime
from core.downloader import Downloader


class SambadDownloader:

    def __init__(self):
        self.downloader = Downloader()

    def image_url(self, scan_date, page):

        day = scan_date.strftime("%d")
        month = scan_date.strftime("%m")
        year = scan_date.strftime("%Y")

        return (
            f"https://sambadepaper.com/epaperimages/"
            f"{day}{month}{year}/"
            f"{day}{month}{year}-md-hr-{page}ss.jpg"
        )

    def download_page(self, scan_date, page):

        url = self.image_url(scan_date, page)

        filename = f"sambad_page_{page}.jpg"

        return self.downloader.download(url, filename)

    def download_all(self, scan_date=None):

        if scan_date is None:
            scan_date = datetime.today()

        pages = []

        for page in range(4, 21):

            file = self.download_page(scan_date, page)

            if file:
                pages.append(file)
            else:
                break

        return pages
