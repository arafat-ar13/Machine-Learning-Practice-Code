import re

import requests
from bs4 import BeautifulSoup


website = requests.get('https://genius.com/albums/Taylor-swift/Lover').text
soup = BeautifulSoup(website, "html.parser")

songs = []
for song in soup.find_all("h3", attrs={"class": "chart_row-content-title"}):
    songs.append(song.text.strip())

songs = [song.split("\n") for song in songs]
new_songs = []
for song in songs:
    new_songs.append(song[0])

songs = new_songs

stuff_to_remove = "\xa0"
muddied_songs = []
for song in songs:
    matches = re.search(f"{stuff_to_remove}", song)

    if matches:
        muddied_songs.append(song.split(f"{stuff_to_remove}"))

collabed = []
for song in muddied_songs:
    collabed.extend(song)

collabed = " ".join(collabed)
collabed_1 = collabed[:41]
collabed_2 = collabed[42:]

songs[11] = collabed_1
songs[15] = collabed_2

links = []
for link in soup.find_all("a", class_="u-display_block"):
    song_link = link["href"]

    links.append(song_link)

lyrics = []
for link in links:
    content = requests.get(link).text
    content_soup = BeautifulSoup(content, "html.parser")

    for lyrics in content_soup.find_all("div", class_="lyrics"):
        song_lyrics = lyrics.p.text

        with open("lyrics.txt", "a", encoding="UTF-8") as file:
            file.write(song_lyrics)
            for x in range(4):
                file.write("\n")

print("DONE SIR!!")