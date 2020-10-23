import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')


df = pd.read_csv("/Users/lukedobrovic/Graphics:Data/lyricAnalytics/mentions_by_year")
df.set_index("Unnamed: 0", inplace=True)


indexNames = df[df["Total"]==0].index
df.drop(indexNames, inplace=True)
print(df.to_string())
df.drop("Total", axis=1, inplace=True)
df.columns = df.columns.astype(int)
df = df.astype(int)
print(df.to_string())



df.loc["LVMH"]= df.loc["Céline"] + df.loc["Louis Vuitton"] + df.loc["Dior"] + df.loc["Fendi"] + df.loc["Fenty"] \
                 + df.loc["Givenchy"] + df.loc["Marc Jacobs"] + df.loc["Bulgari"]

df.loc["Kering"] = df.loc["Gucci"] + df.loc["Saint Laurent"] + df.loc["Balenciaga"] + df.loc["McQueen"]

df.loc["Private Luxury"] = df.loc["Chanel"] + df.loc["Margiela"] + df.loc["Moncler"] + \
                        df.loc["Alexander Wang"] + df.loc["Balmain"] + df.loc["Prada"] + df.loc["Raf"]\
                           + df.loc["Acne"] + df.loc["Comme des Garçons"]

df.loc["Luxury Streetwear"] = df.loc["Off-White"] + df.loc["Bape"] + df.loc["Supreme"] + \
                        + df.loc["Yeezy"]

df.loc["Private Jewelry"] = df.loc["Rolex"] + df.loc["Audemars"] + df.loc["Patek"]

df.loc["Capri Holdings"] = df.loc["Versace"] + df.loc["Choo"] + df.loc["Kors"]

df.loc["Athletic"] = df.loc["Nike"] + df.loc["Jordan"] + df.loc["Adidas"]


print(df.to_string())
df_supers = pd.DataFrame(columns=[2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019])
df_others = pd.DataFrame(columns=[2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019])

df_supers.loc["LVMH"] = df.loc["LVMH"]
df_supers.loc["Kering"] = df.loc["Kering"]
df_supers.loc["Richemont (Cartier)"] = df.loc["Cartier"]
df_supers.loc["Hermès"] = df.loc["Hermès"]
df_supers.loc["Burberry"] = df.loc["Burberry"]
df_supers.loc["Athletic (Nike, Jordan, & Adidas)"] = df.loc["Athletic"]


df_others.loc["Private Luxury (Chanel, Prada, Margiela, CDG, etc.)"] = df.loc["Private Luxury"]
df_others.loc["Luxury Streetwear (Off-White, Yeezy, Supreme, etc.)"] = df.loc["Luxury Streetwear"]
df_others.loc["Private Jewelry (Rolex, Audemars Piguet, & Patek Philippe)"] = df.loc["Private Jewelry"]
df_others.loc["Capri Holdings (Versace, Jimmy Choo, & Michael Kors)"] = df.loc["Capri Holdings"]
df_others = df_others.transpose()
df_supers = df_supers.transpose()


# df_supers.loc["All"] = df_supers.loc["LVMH"] + df_supers.loc["Kering"] + df_supers.loc["Richemont (Cartier)"] + \
#                        df_supers.loc["Hermès"] + df_supers.loc["Burberry"] + df_supers.loc[]

df_slimane = pd.DataFrame(columns=[2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
                                   2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019])
df_slimane.loc["Dior"] = df.loc["Dior"]
df_slimane.loc["Celine"] = df.loc["Céline"]
df_slimane.loc["Saint Laurent"] = df.loc["Saint Laurent"]


df_slimane = df_slimane.transpose()
ax0 = df_slimane.plot(figsize=(26,6))
ax0.set_title("Popularity of labels under Hedi Slimane, 2002-2019")
ax0.set_ylabel("Number of songs in which the brands appear")
ax0.axvspan(ymin=0, ymax=10, xmin=2007, xmax=2000, alpha=0.25, facecolor="indianred",
            linestyle="dashed", edgecolor="maroon")
ax0.axvspan(ymin=0, ymax=10, xmin=2012, xmax=2016, alpha=0.25, facecolor='mediumpurple',
            linestyle="dashed", edgecolor="rebeccapurple")
ax0.axvspan(ymin=0, ymax=10, xmin=2018, xmax=2019, alpha=0.25, linestyle="dashed", edgecolor="midnightblue")
ax0.text(2002.15, 1.15, "2000-2007: Slimane leads Dior Homme",
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
ax0.text(2012.3, 1.15, "2012-2016: Slimane \n leads Saint Laurent",
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
ax0.text(2016.65, 1.65, "2018-Present: \n Slimane \n leads Celine",
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
ax0.plot(2002, 0, marker='o', markersize=3, color="indianred")
ax0.plot(2007, 1, marker='o', markersize=3, color="indianred")
ax0.plot(2012, 1, marker='o', markersize=3, color="mediumpurple")
ax0.plot(2016, 2, marker='o', markersize=3, color="mediumpurple")
ax0.plot(2018, 0, marker='o', markersize=3, color="darkcyan")

plt.show()
plt.close()



ax1 = df_supers.plot(figsize=(26, 6))
                     # color=('dimgray', 'indianred', 'orchid', 'darkgoldenrod', 'seagreen', 'cornflowerblue'))
ax1.set_yticks([0, 3, 6, 9, 12, 15, 18], minor=False)
ax1.set_ylabel("Number of songs in which the firm's brands appear")
# ax1.set_yticks([2, 6, 10, 14, 18], minor=True)
# ax1.grid(b=True, which="minor", axis="y")
ax1.set_title("Luxury \"super winners'\" mentions in popular R&B songs, 2010-2019")

ax2 = df_others.plot(figsize=(24, 6))
ax2.set_title("Other luxury firms' mentions in popular R&B songs, 2010-2019")
ax2.set_ylabel("Number of songs in which the brands appear")
# plt.show()
plt.close()

df_null = pd.DataFrame(columns=[2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019])
df_null = df.loc["Null"]
df_null = df_null.transpose()
ax3 = df_null.loc[2002:2019].plot(kind="bar", color="slategrey", figsize=(26, 6), legend=None)
ax3.set_xticklabels(labels = [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011,
                    2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019], rotation=30,
                    fontdict={'verticalalignment':'top'})
ax3.set_title("Hot R&B songs for which lyrics were $not$ found, 2010-2019")
ax3.annotate("No lyrics from 2015 analyzed", xy=(12.3, 0.5), rotation=40)
ax3.legend().set_visible(False)
ax3.set_ylabel("Number of songs for which lyrics were not found")

plt.show()
plt.close()


df_gucci = pd.DataFrame(columns=[2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
                                   2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019])
df_gucci.loc["Gucci"] = df.loc["Gucci"]
df_gucci = df_gucci.transpose()
ax4 = df_gucci.plot(figsize=(26, 6))
ax4.set_title("Mentions of Gucci in popular R&B songs, 2002-2019")
ax4.legend().set_visible(False)
ax4.text(2015.25, 1.8, "2015: Alessandro Michele \n appointed creative director",
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
ax4.text(2006.15, 3.2, "2006: Frida Giannini \n appointed creative director",
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
ax4.text(2002.1, 5.3, "2004: Tom Ford and \n Domenico de Sole depart",
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
ax4.text(2010.25, 10.3, "2010: Hip-hop goes \n wild for Gucci??",
         bbox=dict(facecolor='none', edgecolor='black', boxstyle='round'))
ax4.plot(2004, 5, marker='o', markersize=3, color="maroon")
ax4.plot(2006, 4, marker='o', markersize=3, color="maroon")
ax4.plot(2015, 2.5, marker='o', markersize=3, color="maroon")
ax4.plot(2010, 11, marker='o', markersize=3, color="maroon")
ax4.set_yticks([2, 4, 6, 8, 10], minor=False)
# plt.show()
plt.close()