# learning-python
Projects to learn python

1. Project Youtube Audio Downloader:

#Extract Audio from Youtube Videos and Playlists
#To run on Windows or Mac you need to create an executable file with the help of PyInstaller
#To install PyInstaller run: pip install pyinstaller
#To create an executable: pyinstaller name.py --onefile
#For MacOS create exec with pyinstaller on mac and for Windows on Windows

2. Project Telegram Movies bot:

The idea was to create a bot on telegram that can join a group chat of friends, accept various movies from users,
show the list of accepted movies, remove movies from the list, vote and show vote results.
You need to create a bot with @botfather on telegram to obtain bot API

3. Higher vs Lower game:

As part of my studies, I created a simple yet frustratingly addictive game called “Higher or Lower.” The goal is to guess who has more Instagram followers. The game can be easily extended by adding new entries to the data list. The follower counts are based on Instagram data from 2023.

4. Coffee Machine Simulator
   
The goal of this project was to create a coffee machine simulator that allows users to select a drink, insert coins, receive change, and enjoy their beverage. The simulator also includes a hidden command, report, which provides a detailed summary of the remaining resources (water, milk, coffee, and money collected). This program ensures efficient resource management by checking if enough ingredients are available for the selected drink before proceeding. If resources are insufficient or the inserted money is inadequate, the user is informed and prompted to try again.

5. Turtle Racing Simulator with bets

It is an interactive racing game created using Python’s turtle module with OOP. Players place a bet on which colored turtle (red, orange, yellow, green, blue, or purple) will win the race. The turtles start at the same position and race across the screen toward a finish line, drawn on the track for added realism. Each turtle’s progress is randomized, making the game unpredictable and exciting. The first turtle to cross the finish line is declared the winner, and players are notified whether their bet was correct. 

6. Snake Game

This is a classic Snake Game built with Python’s turtle module. The game features two modes:
	•	Simple Mode (1): Standard gameplay with a steady speed.
	•	Advanced Mode (2): Gameplay speeds up as the snake grows!
   •	Smooth animations with collision detection for walls, food, and the snake’s own body.
	•	Dynamic scoreboard to track your progress.
	•	Fully interactive controls (Arrow keys to move the snake).
	•	Customizable speed variations for a challenging experience.
 
 7. Pomodoro Timer

A simple Pomodoro Timer built with Python and Tkinter to enhance productivity using the Pomodoro Technique. It alternates between work and break sessions while tracking progress with checkmarks. This tool helps maintain focus and improve time management.

8. LinkedIn Job Search Automation with Selenium

This Python script uses Selenium to automate job searches on LinkedIn. It prompts users for their desired job title, location, and LinkedIn credentials, then logs into LinkedIn and navigates to the Jobs section to perform a search based on the given criteria. A great starting point for building automated job application tools or learning Selenium web scraping techniques.

Features

- Secure credential input using `getpass`
- Multi-language support (defaults to `en-GB`)
- Automates login and job search steps
- Fully browser-based using Firefox and Selenium

Notes
	•	This script currently uses hardcoded sleep delays (time.sleep()); for more reliable behavior, you might want to improve it using explicit waits (e.g., WebDriverWait).
	•	LinkedIn may change its HTML structure, which could break the script. Always check for updates.
	•	Use this tool responsibly and respect LinkedIn’s terms of service.

License

This project is open-source and available under the MIT License.

⸻

Disclaimer: This project is for educational purposes only. Automated interactions with LinkedIn may violate their terms of service.

Requirements

- Python 3.6+
- Firefox browser
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases) installed and added to your system PATH
- Selenium Python package
You can install Selenium via pip:

```bash
pip install selenium
```

9. OLX.pt Web Scraper with BeautifulSoup

This Python script scrapes classified listings from [OLX.pt](https://www.olx.pt) based on a user-provided search query. It collects and displays product titles, prices, and links across all available pages for that query.

Features

- User-defined search term
- Automatically detects and loops through all result pages
- Extracts and prints:
  - Item name
  - Price
  - Direct link to the listing

Requirements

- Python 3.6+
- `requests` and `beautifulsoup4` libraries

Install dependencies via pip:

```bash
pip install requests beautifulsoup4 lxml
```
