# Project 1 - On This Day
This project asks user for a day of the year, and then gives them a random 'On This Day' fact

The project uses wikimedia api to get these facts<br>
It requires presence of a `secret_info.json` file which has the following structure

```
{"Client ID":
    "<CLIENT_ID>",

"Client secret":
    "<CLIENT_SECRET>",

"Access token":
    "<ACCESS_TOKEN>"

"App name":
    "<APP_NAME>",

"Email":
    "<EMAIL_ID>"
}
```
A sample json file has been provided for your reference.<br>
<br>

## Setup
1) Getting your API keys . Documentation for getting your API keys can be found [here](https://api.wikimedia.org/wiki/Documentation/Getting_started) <br>
NOTE: Make sure you select Personal API token when making your API key.

2) Copy the API key info into the sample `secret_info.json` file, replacing the dummy values with your actual credentials
3) Replace the name of your app and the email id in `secret_info.json` with the App Name and Registered Email ID. 
4) Run `On This Day.py`
