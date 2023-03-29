# Python-Launch-Page

> Personal launch page written in Python that scrapes websites for weather and junk yard data, and displays links.

## Table of Contents

- [General Information](#general-information)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Screenshots](#screenshots)
  - [Setup](#setup)
  - [Usage](#usage)
  - [Current Status](#current-status)
- [Room For Improvement](#room-for-improvement)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
- [License](#license)

## General Information

> This was a personal launch page born from my need to practice Python, practice web scraping, and still make something useful. It can replace the browser's default start page or new tab page if so desired and tweaked to the user's needs.

## Technologies Used

> Python, HTML5, CSS3

## Features

- Weather Data scraped from https://weather.com
- Junk Yard Data scraped from https://upullandpay.com
- Links compiled from file

## Screenshot(s)

> ![ScreenShot](/images/screenshot.png)

## Setup

- Download repository
- Adjust data/links.txt for the links you need/want
- Adjust utils/get_WeatherReport.py for your city's weather page
- Adjust utils/get_PullAndPayInventory.py with your vehicle selections and junkyard location.

## Usage

- Type the following in your terminal/command prompt from the folder you downloaded the project to
  - python3 create_NewTabPage
- Open the created index.html in your browser

## Current Status

> Not working on

## Room For Improvement

- Ideas:
  - Make it easier for a different user to adjust for their needs.
  - Run index.html automatically after completing page creation.
  - Remove index.html at end instead of beginning so that there is no time that index.html does not exist.
- Todo:
  - N/A

## Acknowledgements

- Inspired By:
  - I didn't like the browser's default start page and I wanted to practice web scraping within Python.
- Based On:
  - My personal needs/desires at the time.
- Contributors:
  - None

## Contact

> [amoramas1984@gmail.com](mailto:amoramas1984@gmail.com)

## License

> None
