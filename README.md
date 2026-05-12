<p align="center">
  <img src="./banner.png" alt="ShadowHunter banner">
</p>

# ShadowHunter

<p align="center">
  <img src="https://img.shields.io/github/languages/top/MrThivina/ShadowHunter?style=for-the-badge" alt="Top language">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/github/repo-size/MrThivina/ShadowHunter?style=for-the-badge" alt="Repository size">
</p>

ShadowHunter is a terminal-based OSINT toolkit for checking publicly available profiles across usernames, domains, and online platforms.

## Features

- Search for usernames across supported platforms
- Uses a simple `sites.json` platform list
- Runs from the terminal with Python
- Lightweight setup for Termux, Linux, macOS, and Windows

## Requirements

- Python 3
- Git
- `requests` Python package

## Installation

### Termux

```bash
pkg update
pkg upgrade
pkg install python git
pip install requests
git clone https://github.com/MrThivina/ShadowHunter
cd ShadowHunter
```

### Windows, Linux, or macOS

```bash
git clone https://github.com/MrThivina/ShadowHunter
cd ShadowHunter
pip install requests
```

## Usage

Run the tool from the project folder:

```bash
py ShadowHunter.py
```

If your system uses `python3` instead of `python`, run:

```bash
py -3 ShadowHunter.py
```

## Project Files

- `ShadowHunter.py` - main terminal application
- `sites.json` - supported platform URL templates
- `banner.png` - README banner image

## Supported Platforms

The default `sites.json` includes:

- Instagram
- GitHub
- Twitter
- TikTok
- Reddit

You can add more platforms by editing `sites.json` and adding URL templates that contain `{}` where the username should be inserted.

## Disclaimer

ShadowHunter is intended for educational and authorized research use only. Use it responsibly and only with publicly available information.
