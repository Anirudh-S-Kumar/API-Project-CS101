import requests
import json

endpointUrl = 'https://query.wikidata.org/sparql'

query = """
SELECT ?item ?itemLabel  WHERE {
  ?item wikibase:sitelinks ?sitelinks. hint:Prior hint:rangeSafe true.
#   ?item wdt:P279 wd:Q4167836.
  FILTER(?sitelinks >= 90 )

  MINUS { ?item wdt:P31 ?subclass.
          ?subclass wdt:P279 wd:Q4167836}.

  MINUS { ?item wdt:P31 ?subclass.
          ?subclass wdt:P279 wd:Q15647814}.

  MINUS {?item wdt:P31 ?subclass.
        ?subclass wdt:P279 wd:Q14296}.

  MINUS { ?item wdt:P31 ?subclass.
          ?subclass wdt:P279* wd:Q186081}.

  MINUS {?item wdt:P31 ?subclass.
        ?subclass wdt:P279* wd:Q186408}.

  MINUS {?item wdt:P31 ?subclass.
        ?subclass wdt:P279* wd:Q17442446}.

  MINUS {?item wdt:P31 ?subclass.
        ?subclass wdt:P279 wd:Q1190554}.

  MINUS { ?item wdt:P31 wd:Q21199}.
  MINUS { ?item wdt:P31 wd:Q4167836.}.
  MINUS { ?item wdt:P31 wd:Q11266439.}.
  MINUS { ?item wdt:P31 wd:Q19842659.}.
  MINUS { ?item wdt:P31 wd:Q14204246.}.
  MINUS { ?item wdt:P31 wd:Q20010800.}.
  MINUS { ?item wdt:P31 wd:Q20010800.}.
  MINUS { ?item wdt:P31 wd:Q15184295.}.

  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }

}

ORDER BY DESC (?sitelinks)
"""


def generatingLocalData():
  """
  Function to dump the data locally for faster access and processing
  """
  r = requests.get(endpointUrl, params={'query': query}, headers={
                   'Accept': 'application/sparql-results+json'})
  data = (r.json())['results']['bindings']
  counter = 0
  write_val = list()
  for i in (data):
    temp = set(i["itemLabel"]["value"])
    if ":" not in temp:
      write_val.append(i)
      counter += 1

  with open("data.json", "w") as f:
    json.dump(write_val, f)
