import requests
from bs4 import BeautifulSoup
import json

URL = "https://kprofiles.com/twice-discography/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find("div", {"class": "entry-content herald-entry-content"})

class Album:
    def __init__(self, name, release_date, type):
        self.name = name
        self.release_date = release_date
        self.type = type
    songs = []

albums = []
# cant use find_all since i have to loop through the section of the site
# and stop at the NOTE
for element in content:
    # Stop condition yes mega scuffed
    if(element.get_text() == "NOTE: BOLDED SONGS HAVE RELEASED MUSIC VIDEOS/SPECIAL VIDEOS .・゜-: ✧ :-───── ❝ Credits ❞ ─────-: ✧ :-゜・． sorrysweetie"):
        break
    # only get elements with text
    if(element.get_text() != ''):
        # get album details
        # WHY THE FUCK IS EYES WIDE OPEN HANDICAPPED
        # 2 P ELEMENTS????
        if(element.name == 'p'):
            text = element.get_text()
            albuminfo = text.splitlines()
            # blacklist LMAO some albums wont be available sadly
            if len(albuminfo) < 4:
                continue
            else:
                """
                album = Album(albuminfo[0],albuminfo[1],albuminfo[3])
                albums.append(album)
                """
                # test
                print("album info: ")
                print(f"name: {albuminfo[0]}")
                print(f"date: {albuminfo[1]}")
                print(f"type: {albuminfo[3]}")

        # get song list of album
        elif(element.name == 'ol'):
            songs = []
            print("SONGS:")
            for song in element:
                songs.append(song.get_text())
            print(songs)
            print('\n')
