
import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
querystring = {"deck_count": "6"}
headers = {
'Cache-Control': "no-cache",
'Postman-Token': "5c03050b-7cee-42d0-87de-4da1c3469570"
}
response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)

1232504

5124638322
