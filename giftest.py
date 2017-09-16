import requests

def despace(input_string):
    return input_string.replace(' ','+')

def get_gif (input_string):
    our_key = "23v41Ke9qoYYpQo7OcoUWd9bI6IlNBL2"
    phrase = despace(input_string)
    to_send = "http://api.giphy.com/v1/gifs/translate?api_key={0}&s={1}".format(our_key, phrase)
    r = requests.get(to_send)
    gifs = r.json()
    gif_url = gifs["data"]["images"]["fixed_height"]["url"]
    print(gif_url)

get_gif("ice cream")


