# DirectoryDownloader


![GitHub top language](https://img.shields.io/github/languages/top/VirusZzHkP/DirectoryDownloader?color=red&style=for-the-badge)
[![GitHub license](https://img.shields.io/github/license/VirusZzHkP/DirectoryDownloader?color=yellow&style=for-the-badge)](https://github.com/VirusZzHkP/DirectoryDownloader/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/VirusZzHkP/DirectoryDownloader?color=green&style=for-the-badge)](https://github.com/VirusZzHkP/DirectoryDownloader/stargazers)



**DirectoryDownloader** is a Python-based utility tool that automates downloading of files from web-accessible directories (like `https://example.com/folder/`). It parses HTML directory listings, detects downloadable files, and saves them in a structured local folder — all with **parallel downloads** for high performance.

---

## 🚀 Features

- 🔗 Accepts any URL that points to a file listing (Apache/nginx-style indexes)
- 📁 Automatically creates local folder based on the URL path
- 📂 User-defined top-level output folder
- ⏱️ **Parallel downloading** using Python threads (boosts speed) <i>( To be implemented soon )</i>
- 🔄 Skips invalid or non-file links
- 📜 Beautiful terminal interface with ASCII art
- ✅ Simple, fast, and reliable
- 🧾 Generates a log file of all downloads

---

## 📦 How It Works

1. User enters a web URL like: https://example.com/files/movies/
2. Tool parses the page, finds all downloadable links (e.g. `.mp4`, `.zip`)
3. Asks user for a custom folder name like: `MyMovies`
4. Downloads all files from that URL to: ~/Downloads/DirDownloader/MyMovies/movies/
5. Confirmation shown upon success.

---

## 🧰 Tech Stack

- Python 3.x
- `urllib` for downloading
- `BeautifulSoup` for HTML parsing
- `ThreadPoolExecutor` for concurrency
- `logging` for download logs

---

## 📥 Example Usage

```bash
$ python3 DirDownld.py

Enter the link to download from: https://example.com/assets/
Enter a folder name to save into (e.g. MyProject): SiteAssets

Downloading into folder: /home/user/Downloads/DirDownloader/SiteAssets/assets/
Found 18 links in https://example.com/assets/
Downloaded image1.png to /assets/image1.png
...
Download complete. Download again? (y/n): n

```
## 📌 Ideal Use Cases
- Backing up open web file directories
- Downloading training datasets
- Offline storage of video/audio folders
- Educational resource mirroring

## 🧾 Logs
All download activity is saved to: `~/Downloads/DirDownloader/download_log.txt`


## 👤 Credits & License

---

**DirectoryDownloader** is developed and maintained by [Hrisikesh (VirusZzWarning)](https://github.com/VirusZzHkP) — [@hrisikesh_pal on Twitter](https://twitter.com/hrisikesh_pal).

This project is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](LICENSE) file for full license details.


