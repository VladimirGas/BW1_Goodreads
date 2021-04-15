import preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
import re

# book_data = preprocessing.preprocessing("books.csv")
# book_data.to_csv("clean.csv")
# df = book_data

# df = pd.read_csv("clean_df.csv")
# print(df.columns)
# print(df.publish_year.value_counts().sort_index())
# print(df.publish_year.min())
# print(df.publish_year.max())
# print(df.publish_year.max() - df.publish_year.min())



def releases_by_year(dataframe):
    df = dataframe
    # Equal Bins
    # Increase data window
    # Zoom in to point of interest (split it into years)
    # See if we can explain spikes with real world events
    year_ranges = []
    for year in range(2000, 2022, 1):
        year_ranges.append(year)



    plt.hist(df.publish_year, bins=year_ranges)
    plt.title("Dystopian Releases Over Time")
    plt.xlabel("Year of publication")
    plt.ylabel("Publications")
    plt.savefig('releases_by_year.png')
    plt.show()

def spike_in_releases(dataframe):
    df = dataframe
    line_data = df.publish_year.value_counts().sort_index()

    line_data = line_data[line_data.index > 2000]
    years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
    plt.plot(line_data, color="black", marker="o", mec="black", mfc="green")
    #plt.hist(line_data, bins=years)

    #plt.hist(df.publish_year, bins=line_data, histtype="step", color="black", label="outline")
    # plt.hist(df.publish_year, bins=year_range)
    #
    #plt.scatter(df.publish_year, df.avg_rating, c=df.avg_rating, cmap="plasma")
    plt.title("Dystopian Releases Over Time - 2000 to 2020")
    plt.xlabel("Year of publication")
    plt.ylabel("Publications")

    plt.text(df.publish_year.max() - 20,df.publish_year.value_counts().max()-5,"     Highest Value:\n2011 - {} publications".format(df.publish_year.value_counts().max()))
    cm = plt.cm.get_cmap('RdYlBu_r')
    plt.savefig('max_popularity.png')
    plt.show()

def awards_by_year(dataframe):
    df = dataframe
    year_ranges = [range(1800,2022)]
    plt.hist(df.awards.value_counts(), bins=year_ranges)
    plt.show()


def rating_by_year(dataframe):
    df = dataframe
    graph_data = pd.DataFrame([df.publish_year, df.avg_rating])
    graph_data.drop(df.publish_year < 2000)
    graph_data[0]
    save_graph('rating_by_year.png')
    plt.show()

def save_graph(filename):
    plt.savefig(filename)


def pages_v_awards(dataframe):
    df = dataframe
    pages = df.pages

    #print(df.awards)
    award_count = []
    for award_list in df.awards:
        try:
            award_count.append( (len(re.findall("[0-9]{4}", award_list))))
        except:
            award_count.append(0)


    df["award_count"] = pd.Series(award_count)
    #print(df.award_count)
    graph_data = pd.DataFrame([df.pages, df.award_count]).transpose()
    #line_data = line_data[line_data.index > 2000]
    graph_data = graph_data[graph_data.pages < 1000]
    graph_data = graph_data[graph_data.award_count < 30]
    print(graph_data)


    plt.scatter(graph_data.pages, graph_data.award_count, edgecolors="black", color="green")
    plt.title("Awards won against Page Length")
    plt.xlabel("No. Pages")
    plt.ylabel("Awards Won")
    save_graph("page_awards.png")
    plt.show()


def main():
    df = pd.read_csv("clean_df.csv")
    # print(np.min(df.publish_year))
    # print(np.max(df.publish_year))
    #releases_by_year(df)
    #spike_in_releases(df)
    #rating_by_year(df)
    #pages_v_awards(df)
    print(df.genres.value_counts())
    #print(df.publish_year.value_counts().sort_values())
    #print(np.shape(df))

if __name__ == "__main__":
    main()
