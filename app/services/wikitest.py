import requests

def get_wiki(topic):
    topic = topic.lower()
    #use the string below for properly formatted wikipedia api access (https://www.mediawiki.org/wiki/API:Main_page)
    to_send = "https://en.wikipedia.org/w/api.php?titles={}&action=query&prop=extracts&redirects=1&format=json".format(topic)
    r = requests.get(to_send)#sends the get request, gets response, sets to r
    data = r.json()#converts to json (prettifying)
    p_dict = data["query"]["pages"]
    return p_dict[list(p_dict.keys())[0]]['extract']

print(get_wiki("cats"))