from bs4 import BeautifulSoup
import requests
from subprocess import call


# import urllib.request

def get_items(search_term):
    """
    searches YTS and gets the search result
    :param search_term: String that contains the search terms
    :return: formatted data consisting of Torrent name , URL and number of search results
    """
    search_term = search_term.replace(" ", "+")
    url = "https://zooqle.com/search?q={}".format(search_term)
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    try:
        all_results = soup.find_all('table', {'class': 'table table-condensed table-torrents vmiddle'})[0]
    except:
        return {}
    soup = BeautifulSoup(str(all_results), 'lxml')
    rows = soup.find_all('tr')
    data = {}
    for row in rows:
        link_soup = BeautifulSoup(str(row), "lxml")
        try:
            magnet_link = link_soup.find_all('a', {'title': "Magnet link"})[0].get('href')
            data[row.get_text()] = magnet_link
        except:
            pass
    return data


def process_results(results):
    """
    Gets user choice that needs to be played
    :param results: stores the results which we got from get_items
    :return: user choice
    """
    if len(results) >= 1:
        temp_data = {}
        count = 1
        print("Here are the top {} results for your query, which one would you like to stream".format(
            "4" if len(results) > 4 else str(len(results))))
        for label in results.keys():
            temp_data[count] = label
            count = count + 1
            print(label)
            if count == 5:
                print("Enter your choice:")
                break
        try:
            choice = int(input())
            if choice < 1 or choice > 4:
                a = 0 / 4
            else:
                print("***____________________________________________***")
                print("Give me 2-3 minutes to generate a video buffer....")
                return [temp_data[choice], results[temp_data[choice]]]
        except:
            print("Try Again.. Enter a valid choice")
    else:
        return []


def call_the_shots(magnet):
    magnet_url = ""
    try:
        magnet_url = magnet[1]
        magnet_url = 'peerflix "' + str(magnet_url) + '" --vlc'
    except:
        print("Torrent not found")
    call(magnet_url, shell=True)


def main(query):
    call_the_shots(process_results(get_items(query)))
