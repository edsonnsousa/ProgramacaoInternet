
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = '7262a97c'
app_key = '3f1cfbb08e1a01492a46bbe447bd9722'
language = 'es'
word_id = 'rojo'
url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
# url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/' + language + '/?corpus=nmc&lemma=' + word_id.lower()
r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})
print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))