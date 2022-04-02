import requests
from bs4 import BeautifulSoup

URL = "https://kprofiles.com/twice-discography/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find("div", {"class": "entry-content herald-entry-content"})

# cant use find_all since i have to loop through the section of the site
# and stop at the NOTE
for element in content:
    # Stop condition yes mega scuffed
    if(element.get_text() == "NOTE: BOLDED SONGS HAVE RELEASED MUSIC VIDEOS/SPECIAL VIDEOS .・゜-: ✧ :-───── ❝ Credits ❞ ─────-: ✧ :-゜・． sorrysweetie"):
        break
    # only get elements with text
    if(element.get_text() != ''):
        # get album details
        if(element.name == 'p'):
            print("ALBUM NAME")
            print(element.get_text())
        # get song list of album     
        elif(element.name == 'ol'):
            print("SONGS:")
            for song in element:
                print(song.get_text())
