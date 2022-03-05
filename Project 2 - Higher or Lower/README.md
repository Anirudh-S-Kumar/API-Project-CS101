# Project 2 - Higher or Lower Game

This is a spinoff of the popular higher or lower game (https://www.higherlowergame.com/) using wikidata queries instead of using Google Trends data.
No API keys are required to run this project<br>
The project uses two APIs
- Wikidata API : Used to get the list of items to compare within the game
- Wikipedia API : Used to get the pageviews on a site in the last 2 months. 

NOTE: Only English Wikipedia (https://en.wikipedia.org/) pageviews have been used as part of the project.

## Criteria for items to be used in the game
- Main filter used was the article should have more than 90 `sitelinks` (https://www.wikidata.org/wiki/Help:Sitelinks) .
- Other filters included removing wikidata specific links and categories of things inside wikidata.
- Exclusion of time periods, days/dates, numbers. 

The query to get all the items is a computationally intensive task, and can take upto a minute to get all of them. 
Therefore, they are cached into the `data.json` file to avoid doing this task everytime the user plays the game. 

## Definitions of views
The main definition of "views" used to compare two wikipedia articles is the number of views it gets in the last two months.
Some other definitions could also have been used, such as average daily views within the last 2 months, but were not chosen to avoid floating point arithmetic. 

## Installation instruction
1) Download/Clone this repository
2) Run `higher_or_lower.py`
