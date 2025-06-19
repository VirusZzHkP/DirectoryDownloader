from os import makedirs
from os.path import basename, join
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time
import logging
import sys

# Setup Logging
log_path = Path.home() / "Downloads" / "DirDownloader" / "download_log.txt"
makedirs(log_path.parent, exist_ok=True)
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

graphicart = """" 
-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------
______ ___________ _____ _____ _____ _____________   __ ______ _____  _    _ _   _  _     _____  ___ ______ ___________
|  _  \_   _| ___ \  ___/  __ \_   _|  _  | ___ \ \ / / |  _  \  _  || |  | | \ | || |   |  _  |/ _ \|  _  \  ___| ___ |
| | | | | | | |_/ / |__ | /  \/ | | | | | | |_/ /\ V /  | | | | | | || |  | |  \| || |   | | | / /_\ \ | | | |__ | |_/ /
| | | | | | |    /|  __|| |     | | | | | |    /  \ /   | | | | | | || |/\| | . ` || |   | | | |  _  | | | |  __||    /
| |/ / _| |_| |\ \| |___| \__/\ | | \ \_/ / |\ \  | |   | |/ /\ \_/ /\  /\  / |\  || |___\ \_/ / | | | |/ /| |___| |\ \ 
|___/  \___/\_| \_\____/ \____/ \_/  \___/\_| \_| \_/   |___/  \___/  \/  \/\_| \_/\_____/\___/\_| |_/___/ \____/\_| \_|

-------------------------------------------------------------------------------------------------------------------------

                                        M@d3 With ♥ -- VirusZzWarning
                                Read My Blogs : https://viruszzwarning.medium.com/
                                
-------------------------------------------------------------------------------------------------------------------------
                ||  This tool will crawl through the link and download any types of files found  ||
-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------
"""

for x in graphicart.splitlines():
    print(x)
    time.sleep(0.3)

def download_url(urlpath):
    try:
        with urlopen(urlpath) as connection:
            return connection.read()
    except Exception as e:
        logging.error(f"Error downloading {urlpath}: {e}")
        print(f"Error: Unable to download {urlpath}")
        return None

def get_urls_from_html(content):
    try:
        html = content.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        atags = soup.find_all('a')
        return [t.get('href', None) for t in atags]
    except Exception as e:
        logging.error(f"Error parsing HTML: {e}")
        print("Error: Failed to parse webpage.")
        return []

def save_file(path, data):
    try:
        with open(path, 'wb') as file:
            file.write(data)
    except Exception as e:
        logging.error(f"Error saving file {path}: {e}")
        print(f"Error: Couldn't save file {path}")

def download_url_to_file(url, link, path):
    if link is None or link == '../':
        return (link, None)
    if not (link[-4] == '.' or link[-3] == '.' ):
        return (link, None)
    absurl = urljoin(url, link)
    data = download_url(absurl)
    if data is None:
        return (link, None)
    filename = basename(absurl)
    outpath = join(path, filename)
    save_file(outpath, data)
    return (link, outpath)

def extract_folder_name(url):
    parsed_url = urlparse(url)
    parts = [part for part in parsed_url.path.split('/') if part]
    return parts[-1] if parts else "webfiles"

def download_all_files(url, path):
    data = download_url(url)
    if data is None:
        return
    makedirs(path, exist_ok=True)
    links = get_urls_from_html(data)
    print(f'Found {len(links)} links in {url}')
    logging.info(f"Found {len(links)} links in {url}")
    for link in links:
        link, outpath = download_url_to_file(url, link, path)
        if outpath is None:
            print(f'> Skipped {link}')
            logging.warning(f"Skipped {link}")
        else:
            print(f'Downloaded {link} to {outpath}')
            logging.info(f"Downloaded {link} to {outpath}")

# ------------------- Looping Interface -------------------

while True:
    try:
        URL = input("\nEnter the link to download from: ").strip()
        user_folder = input("Enter a folder name to save into (e.g. Website_name): ").strip()
        
        if not URL or not user_folder:
            print("Error: URL and folder name cannot be empty.")
            continue

        extracted_folder = extract_folder_name(URL)
        final_path = Path.home() / "Downloads" / "DirDownloader" / user_folder / extracted_folder
        
        print(f"\nDownloading into folder: {final_path}")
        download_all_files(URL, str(final_path))

        again = input("\nDownload complete. Download again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for using my tool. With ♥ -- VirusZzWarning")
            break
    except KeyboardInterrupt:
        print("\nDownload cancelled by user.")
        logging.warning("Download cancelled by user via KeyboardInterrupt.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        logging.critical(f"Unexpected crash: {e}")
