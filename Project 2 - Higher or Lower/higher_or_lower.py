import random
import requests
import json
import os
import getting_data


files = set([f for f in os.listdir('.') if os.path.isfile(f)]) 


file_not_found_message = """It looks like you are playing the game for the first time
Please wait for a bit while we get the data for a game
The process can take upto a minute so please be patient
This is just a one-time process"""


#verifying that data.json file is present
if 'data.json' not in files:
    print(file_not_found_message)
    getting_data.generatingLocalData()


with open("data.json", encoding="utf8") as f:
    game_data = json.load(f)


def get_random_value():
    """
    Function to get a random value fron the data.json file
    along with a description of it
    """

    item = random.choice(game_data)
    title = item["itemLabel"]["value"]
    entity = item["item"]["value"].split("/")[-1]

    endpointUrl = 'https://query.wikidata.org/sparql'

    query = """
    SELECT ?item ?itemLabel ?descriptionLabel
    WHERE
    {
    wd:%s schema:description ?description.
    filter (lang(?description) = "en")
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    """ % (entity)

    r = requests.get(endpointUrl, params={'query': query}, headers={
                     'Accept': 'application/sparql-results+json'})

    description = (r.json())[
        'results']['bindings'][0]['descriptionLabel']['value']

    return (f"{title} - {description}")





def get_views(title):
    """
    Function which gives all the views a page has recieved within the past 2 months
    """

    url = "https://en.wikipedia.org/w/api.php"

    param = {
        "action": "query",
        "prop": "pageviews",
        "format": "json",
        "titles": f"{title}"
    }

    data = (requests.get(url, params=param)).json()
    temp = list(data['query']['pages'].keys())[0]
    views = (data['query']['pages'][temp]["pageviews"])

    views_list = (list(views.values()))
    views_list = [x if x else 0 for x in views_list]
    r_val = sum(views_list)
    return r_val

vs = """
 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)
"""


def main_loop():
    """Main game loop"""
    with open("texts.txt") as f:
        print(f.read())

    score = 0
    val1 = get_random_value() # First item
    while True:
        val2 = get_random_value() # Second item to compare with the first item

        val1_copy = val1.split(" - ")
        val2_copy = val2.split(" - ")

        val1_views = get_views(val1_copy[0])
        val2_views = get_views(val2_copy[0])

        print(f"Compare A : {val1}, which has {val1_views} views")
        print(vs)
        print(f"Against B : {val2}")
        
        #input validation
        options = {"A", "B"}
        while True:
            attempt = input("Which page gets more views? Type 'A' or 'B' : ")

            if attempt.upper() in options:
                break
            else:
                print("Invalid input. Try again. ")
                

        if val1_views > val2_views:
            answer = "A"
        else:
            answer = "B"

        if answer == attempt.upper():
            score += 1
            print(f"Correct! {val2_copy[0]} gets {val2_views} views")
            print(f"Current Score - {score}")
            val1 = val2

        else:
            print("Incorrect! \nGAME OVER \n")
            print(f"{val2_copy[0]} gets {val2_views} views")
            print(f"Final Score - {score}")
            print()
            break
        print()


main_loop()
