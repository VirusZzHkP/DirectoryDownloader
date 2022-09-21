from os import makedirs
from os.path import basename
from os.path import join
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time


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
    time.sleep(0.5)


 
# load a file from a URL, returns content of downloaded file
def download_url(urlpath):
    # open a connection to the server
    with urlopen(urlpath) as connection:
        # read the contents of the url as bytes and return it
        return connection.read()
 
# decode downloaded html and extract all <a href=""> links
def get_urls_from_html(content):
    # decode the provided content as ascii text
    html = content.decode('utf-8')
    # parse the document as best we can
    soup = BeautifulSoup(html, 'html.parser')
    # find all all of the <a href=""> tags in the document
    atags = soup.find_all('a')
    # get all href values (links) or None if not present (unlikely)
    return [t.get('href', None) for t in atags]
 
# save provided content to the local path
def save_file(path, data):
    # open the local file for writing
    with open(path, 'wb') as file:
        # write all provided data to the file
        file.write(data)
 
# download one file to a local directory
def download_url_to_file(url, link, path):
    # skip bad urls or bad filenames
    if link is None or link == '../':
        return (link, None)
    # check for no file extension
    if not (link[-4] == '.' or link[-3] == '.' ):
        return (link, None)
    # convert relative link to absolute link
    absurl = urljoin(url, link)
    # download the content of the file
    data = download_url(absurl)
    # get the filename
    filename = basename(absurl)
    # construct the output path
    outpath = join(path, filename)
    # save to file
    save_file(outpath, data)
    # return results
    return (link, outpath)
 
# download all files on the provided webpage to the provided path
def download_all_files(url, path):
    # download the html webpage
    data = download_url(url)
    # create a local directory to save files
    makedirs(path, exist_ok=True)
    # parse html and retrieve all href urls listed
    links = get_urls_from_html(data)
    # report progress
    print(f'Found {len(links)} links in {url}')
    # download each file on the webpage
    for link in links:
        # download the url to a local file
        link, outpath = download_url_to_file(url, link, path)
        # check for a link that was skipped
        if outpath is None:
            print(f'>skipped {link}')
        else:
            print(f'Downloaded {link} to {outpath}')
 
# url of html page that lists all files to download

URL = input("Enter link")
# local directory to save all files on the html page
PATH = str(Path.home() / "Downloads" /"DirDownloader")
# download all files on the html webpage
download_all_files(URL, PATH)
