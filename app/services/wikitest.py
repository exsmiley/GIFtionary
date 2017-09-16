from bs4 import BeautifulSoup
import requests
import re

def get_wiki(topic):
    topic = topic.lower()
    #use the string below for properly formatted wikipedia api access (https://www.mediawiki.org/wiki/API:Main_page)
    to_send = "https://en.wikipedia.org/w/api.php?titles={}&action=query&prop=extracts&redirects=1&format=json".format(topic)
    r = requests.get(to_send)#sends the get request, gets response, sets to r
    data = r.json()#converts to json (prettifying)
    p_dict = data["query"]["pages"]
    return p_dict[list(p_dict.keys())[0]]['extract']


def get_paragraphs_from_wiki(topic):
    # soup = BeautifulSoup(get_wiki(topic), 'html.parser')
    # groups = map(unicode, soup.find_all('p'))
    text = get_wiki(topic)
    meta_info_index = text.find('<h2><span id="See_also">')
    initial_groups = text[:meta_info_index].split('<h2>')
    groups2 = []
    for g in initial_groups:
        next_groups = g.split('<h3>')
        for n in next_groups:
            if len(n) > 0:
                groups2.append(n)
    groups = map(lambda x: re.sub("<.*?>", " ", x).strip(), groups2)
    return map(lambda x: re.sub("\n", "", x), groups)
