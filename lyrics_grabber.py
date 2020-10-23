import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
from collections import defaultdict


page = requests.get("https://www.billboard.com/charts/year-end/2016/hot-r-and-and-b-hip-hop-songs").text
html = BeautifulSoup(page, 'html.parser')

hits_list = html.find_all('div', class_="ye-chart-item__title")
artist_list = html.find_all('div', class_="ye-chart-item__artist")

clean = re.compile('<.*?>')

df_year = pd.DataFrame(columns=["Title", "Artist(s)", "Lyrics"])

for i, title in enumerate(hits_list):
    cleaned_title = re.sub(clean, '', str(title)).strip('\n').replace("&amp;", "&").rstrip('\n')
    hits_list[i] = cleaned_title
    df_year.loc[i, "Title"] = cleaned_title

for i, artist in enumerate(artist_list):
    cleaned_artist = re.sub(clean, '', str(artist)).strip('\n').replace("&amp;", "&").rstrip('\n')
    print(cleaned_artist)
    artist_list[i] = cleaned_artist
    df_year.loc[i, "Artist(s)"] = cleaned_artist

print(df_year.to_string())

counter = 0

HitsYear = defaultdict(list)
from unidecode import unidecode
def artist_name_scrubber(input):
    input = input.split(" and")[0].split(" &")[0].split(" Duet")[0].split(" Intro")[0]
    input = input.split(" Feat")[0].split(" feat")[0].split(", ")[0]
    input = input.split(" X ")[0].split(" x ")[0].split("or")[0].split(" Or")[0]
    input = input.split("Lil ")[-1].replace(".", "").replace("ASAP", "A$AP")
    return unidecode(input)

counter = 0
for row in df_year.iterrows():
    artist = df_year.loc[counter, "Artist(s)"]
    artist = artist_name_scrubber(artist)
    # regex = re.compile(".*?\((.*?)\)")
    name_no_parens = re.sub(r" ?\([^)]+\)", "", df_year.loc[counter, "Title"])
    HitsYear[name_no_parens] = artist
    counter+=1


lyric_dict_year = defaultdict(list)

Dummy = {"I Like It": "Cardi B, Bad Bunny & J Balvin"
         }

import os
TOKEN = "gOM73bfpyx36tpzDvku-vmgRNdHxYOOER32-HR-uuv-HfzmyKOzjmr9WyeKW9eNc"

# Get song object from Genius API
def request_song_info(song_name,page):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + TOKEN}
    search_url = base_url + '/search?per_page=10&page=' + str(page)
    data = {'q': song_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response

from difflib import SequenceMatcher
# Get Genius.com song url's from song object
def request_song_url(song_name, artist_name, song_cap):
    page = 1
    songs = []
    hit_counter = 0
    while True:
        response = request_song_info(song_name, page)
        json = response.json()
        song_info = []
        # total_hits = len(json)
        # print(total_hits)
        # if hit_counter > total_hits-1 or hit_counter > 20:
        #     print("Failure to find:", song_name)
        #     songs.append("failure_to_find")
        #     break
        # else:
        for hit in json['response']['hits']:
            # print(hit_counter)
            # print(hit)
            genius_name = hit['result']['primary_artist']['name'].lower()
            genius_name = unidecode(genius_name).replace(".", "")
            if SequenceMatcher(None, genius_name, artist_name.lower()).ratio() > 0.4 or \
                    artist_name.lower() in genius_name:
                song_info.append(hit)
                print("Found:", song_name)
                break
            hit_counter += 1
        if not song_info:
            songs.append("failure_to_find")
            print("Failure to find:", song_name)
        # Collect song URL's from song objects
        for song in song_info:
            if (len(songs) < song_cap):
                url = song['result']['url']
                songs.append(url)
        if (len(songs) == song_cap):
            break
        else:
            page += 1
    return songs


def lyrics_from_url(url):
    if url == "failure_to_find":
        return ""
    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")     # remove script tags that they put in the middle of the lyrics
    [h.extract() for h in html('script')]     # at least Genius is nice and has a tag called 'lyrics'!
    lyrics = html.find("div", class_ ="lyrics").get_text()  # updated css where the lyrics are based in HTML
    lyrics = re.sub(r'[\[].*?[\]]', '', lyrics)     # remove identifiers like chorus, verse, etc
    chars = "()?/.,?*[]"
    for c in chars:
        lyrics = lyrics.replace(c, '')
    lyrics = lyrics.replace('\n', ' ').replace('\r', ' ')
    # remove empty lines
    lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
    words = ''.join(lyrics)
    return words


def get_lyrics(song_title, artist_name):
    url = request_song_url(song_title, artist_name, 1)[0]
    return lyrics_from_url(url)


def designer_finder(songdict, designers):
    for song in songdict:
        lyrics = songdict.get(song)
        for designer in designers:
            count = lyrics.count(designer)
            if count != 0:
                designers[designer] += count
                print(designer, "appears in:", song, count, "times")
    return designers

designers = {
    "Nike": 0,     # Nike
    "Zara": 0,    # Inditex
    "Céline": 0,     # LVMH
    "Vuitton": 0,
    "Louis": 0,
    "Dior": 0,
    "Pucci": 0,
    "Fendi": 0,
    "Fenty": 0,
    "Givenchy": 0,
    "Kenzo": 0,
    "Marc Jacobs": 0,
    "Bulgari": 0,
    "Gucci": 0,     # Kering
    "Saint Laurent": 0,
    "Balenciaga": 0,
    "McQueen": 0,
    "Brioni": 0,
    "Hermes": 0,    # Hermes
    "Hermès": 0,
    "Adidas": 0,    # Adidas
    "Pandora": 0,    # Pandora
    "Cartier": 0,  # Richemont
    "H&M": 0,    # H&M
    "Burberry":0,    # Burberry
    "Versace": 0,    # Private, not a "Super Winner", other
    "Off-White": 0,
    "Wrangler": 0,
    "Chanel": 0,
    "Patek": 0,
    "Audemars": 0,
    "Gosha": 0,
    "Vetements": 0,
    "Margiela": 0,
    "Moncler": 0,
    "Rick Owens": 0,
    "Acne": 0,
    "Alexander Wang": 0,
    "Balmain": 0,
    "Bape": 0,
    "Fear of God": 0,
    "Prada": 0,
    "Raf": 0,
    "Stone Island": 0,
    "Supreme": 0,
    "Rolex": 0,
    "Rollie": 0,
    "Alyx": 0,
    " AP": 0,
    " A.P.": 0
}

print(HitsYear)
counter = 0
for title, artist in HitsYear.items():
    lyrics = get_lyrics(title, artist)
    print(lyrics)
    lyric_dict_year[title] = lyrics
    df_year.loc[counter, "Lyrics"] = lyrics
    counter+=1


# bey = get_lyrics("Irreplaceable", "Beyonce")
# print(bey)
totals = designer_finder(lyric_dict_year, designers)
print(totals)

# counter = 0
# for key, value in lyric_dict_year.items():
#     print(value)
#     df_year.loc[counter, "Lyrics"] = value
#     counter+=1

# print(df_year.head())


import csv
df_year.to_csv("2015")
# lyrics1 = get_lyrics("Raf")
# print(lyrics1)
# DictRaf = {}
# DictRaf["Raf"] = lyrics1
# rafedup = designer_finder(DictRaf, designers)
# print(rafedup)

# labels = designer_finder(Dict2019, designers)
# print(labels)
# print(Dict2019.get("Beautiful"))
# lyrics = get_lyrics("I Like It")
# print(designer_finder(lyrics, designers))


