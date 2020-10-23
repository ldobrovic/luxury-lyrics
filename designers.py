import pandas as pd
from collections import defaultdict
import numpy as np
import math

# df_designers = pd.DataFrame(columns=["2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010",
#                               "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"])

def designer_finder(dataframe, designers):
    counter = 0
    print(len(dataframe.index))
    while counter < len(dataframe.index):
        title = dataframe.loc[counter, "Title"]
        lyrics = dataframe.loc[counter, "Lyrics"]
        if pd.isnull(lyrics):
            print(title, "is null")
            designers["Null"] +=1
            counter+=1
            continue
        for designer in designers:
            count = lyrics.count(designer)
            if count != 0:
                designers[designer] += 1
                print(designer, "appears in:", title, count, "times")
        counter +=1
    return designers

designers = {
    "Null": 0,
    "Nike": 0,     # Nike
    "Jordan": 0,
    "Zara": 0,    # Inditex
    "Céline": 0,     # LVMH
    "Vuitton": 0,
    "Louis": 0,
    "Louis Vuitton": 0,
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
    "Versace": 0,    # Capri Holdings (NOT a Super Winner)
    "Kors": 0,
    "Choo": 0,
    "Off-White": 0,  # Private, not a "Super Winner", other
    "Yeezy": 0,
    "Chanel": 0,
    "Patek": 0,
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
    "Audemars": 0,
    "Comme des Garçons": 0,
}

df_designers = pd.DataFrame.from_dict(designers, orient="index",)
years=[2002, 2003, 2004, 2005, 2006, 2007, 2008,
        2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
# df_designers.columns = years
print(df_designers.to_string())




df_2002 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2002")
df_2003 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2003")
df_2004 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2004")
df_2005 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2005")
df_2006 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2006")
df_2007 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2007")
df_2008 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2008")
df_2009 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2009")
df_2010 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2010")
df_2011 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2011")
df_2012 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2012")
df_2013 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2013")
df_2014 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2014")
df_2015 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2015")
df_2016 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2016")
df_2017 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2017")
df_2018 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2018")
df_2019 = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/yearly_lyrics/2019")



df_list = [df_2002, df_2003, df_2004, df_2005, df_2006, df_2007, df_2008, df_2009, df_2010,
           df_2011, df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019]

df_list1 = [df_2010]

print(designers)
row_counter = 0
year_counter = 2002
for df in df_list:
    labels = designers.fromkeys(designers, 0)
    labels = designer_finder(df, labels)
    for key, value in labels.items():
        df_designers.loc[key, year_counter] = int(value)
        row_counter+=1
    df_designers[year_counter] = df_designers[year_counter].astype(int)
    year_counter +=1

df_designers.loc["Audemars"] += df_designers.loc[" AP"]
df_designers.drop([" AP"], inplace=True)

df_designers.loc["Hermès"] += df_designers.loc["Hermes"]
df_designers.drop(["Hermes"], inplace=True)

df_designers.loc["Louis Vuitton"] = df_designers.loc["Louis"] + df_designers.loc["Vuitton"] - df_designers.loc["Louis Vuitton"]
df_designers.drop(["Louis", "Vuitton"], inplace=True)

df_designers.loc["Rolex"] += df_designers.loc["Rollie"]
df_designers.drop(["Rollie"], inplace=True)

df_designers = df_designers.astype(int)

df_designers["Total"] = df_designers.sum(axis=1)
df_designers.drop([0], axis=1, inplace=True)
# counter = 2002
# while counter > 2020:
#     labels = designer
print(df_designers.to_string())
df_designers.to_csv("mentions_by_year")
