import requests
import json
import datetime
from random import randint

# Taking day input and verifying that it's correct
while True:
    try:
        date = input("Enter a day(DD/MM) : ")
        datetime.date(2000, int(date[3:]), int(date[0:2]))
        break
    except ValueError:
        print("Wrong day of the year. Try again")


months = {"01": "January",
          "02": "February",
          "03": "March",
          "04": "April",
          "05": "May",
          "06": "June",
          "07": "July",
          "08": "August",
          "09": "September",
          "10": "October",
          "11": "November",
          "12": "December"}

#query to get all the facts
url = f"https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/{date[3:]}/{date[0:2]}"

#getting access token and other details from the secret_info.json file
with open("secret_info.json") as f:
    data = json.load(f)
    ACCESS_TOKEN = data["Access token"]
    APP_NAME = data["App name"]
    EMAIL = data["Email"]


headers = {
    'Authorization': f"Bearer {ACCESS_TOKEN}",
    'User-Agent': f"{APP_NAME} ({EMAIL})"
}

data = requests.get(url, headers=headers).json()


#extracting the event, the year it happened in, and the link to relevant wikipedia article for further reading
facts = []
for i in data["selected"]:
    title_article = (i['pages'][0]['displaytitle'])
    link_article = (i['pages'][0]['content_urls']['desktop']['page'])
    facts.append((i["text"], i["year"], (title_article, link_article)))

#generating a random number as index
rand_i = randint(1, len(facts)) - 1

#output
print(f"""\nOn {date[0:2]} {months[date[3:]]}, {facts[rand_i][1]} \n{facts[rand_i][0]} \n""")
print(f"Read more about {facts[rand_i][2][0]} here - {facts[rand_i][2][1]} \n")
