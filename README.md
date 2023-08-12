# Iteractive Discord bot with python

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Examples](#examples)
- [License](#license)
- [Contact](#contact)

## Description

Monkey is a bot built using Python that provides funny responsive way of interaction to certain triggers: words, patterns, jokes, etc...

## Installation
1. Clone this repository: `git clone https://github.com/ohmma0tokita/discord-bot-project.git`
2. Navigate to the project directory: `cd discord-bot`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Run the bot: `python bot.py`
2. Invite your bot to your Discord server using the provided OAuth2 link.
3. Use bot commands to interact with the bot in your server.

## Features
- Create GIFs from individual frames, add music if you want.
- Adjust frame duration and order for custom animations.
- Support for various image formats (PNG, JPEG, etc.).
- Lightweight and easy-to-understand codebase.

## Examples
**Creating a GIF:**
```python
# Import the necessary modules
from gif_utils import create_gif

# Create a GIF
# you can use the anime or neon frames folders provided in the repo
create_gif("frames-folder-name", music_file="music-file",speed="transition-speed")
```

## Licence
This project is licensed under the MIT License

## Contact
Feel free to contact me at f.sghiri01@email.com.
