import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

URL = "https://kprofiles.com/twice-discography/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
content = soup.find("div", {"class": "entry-content herald-entry-content"})

# Hello class
class Album:
    def __init__(self, name, release_date, type):
        self.name = name
        self.release_date = release_date
        self.type = type
    songs = []
    #thank you https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

    def __repr__(self):
        return "Name: %s, %s, Type: %s \n Songs: %s \n" % (self.name, self.release_date, self.type, self.songs)

# List to insert albums in
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
                # convert date string to datetime object
                date_string = albuminfo[1].split("date: ")[1]
                date_object = datetime.strptime(date_string, "%B %d, %Y")
                json_date = date_object.isoformat()
                album = Album(albuminfo[0], json_date ,albuminfo[3])
                albums.append(album)

        # get song list of album
        elif(element.name == 'ol'):
            songs = []
            #print("SONGS:")
            for song in element:
                songs.append(song.get_text())
            #print(songs)
            #add songs to last album
            albums[-1].songs = songs

def write_json():
    with open('data.json', 'w') as file:
        json.dump([album.__dict__ for album in albums], file)

write_json()
