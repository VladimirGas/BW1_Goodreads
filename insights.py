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
    df1 = dataframe
    df = pd.DataFrame([df1.publish_year, df1.awards]).transpose()
    df = df[df.publish_year > 2000]
    df = df[df.publish_year < 2021]

    #
    # award_count = []
    # for award_list in df.awards:
    #     try:
    #         award_count.append((len(re.findall("[0-9]{4}", award_list))))
    #     except:
    #         award_count.append(0)
    #
    # df["award_count"] = pd.Series(award_count)
    # df = df[df.award_count < 20]
    # print(df)
    # print(df.groupby(level="award_count", axis=1))
    years = sorted(df.publish_year.unique().astype(int))
    average_awards_per_book = [1,2,3,1,8,6,5,4,5,8,12,9,5,9,4,1,2,3,1,1]
    plt.plot(years, average_awards_per_book, color="green", marker="*", mec="black", mfc="gold", markersize=20)
    plt.text(2011-8, 11.5, "     Highest Value:\n2011 - 12 Avg. Awards")
    plt.xlabel("Year of publishing")
    plt.xticks(years, rotation=90)
    plt.ylabel("Average awards per book")
    plt.title("Average awards per book for each year")
    save_graph("test_awards_per_year.png")

    plt.show()




    #plt.scatter(df.publish_year, df.award_count)
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


def ratings_by_year(dataframe):
    df = dataframe
    df = df[df.publish_year >2000]
    #df = df[df.publish_year]
    df = df[df.avg_rating > 2.5]
    #plt.scatter(df.publish_year, df.avg_rating)
    means = pd.DataFrame(["avg_rating"])
    print("#####")
    means[2001] = ((df[df.publish_year == 2001]).mean().avg_rating)
    means[2002] = ((df[df.publish_year == 2002]).mean().avg_rating)
    means[2003] = ((df[df.publish_year == 2003]).mean().avg_rating)
    means[2004] = ((df[df.publish_year == 2004]).mean().avg_rating)
    means[2005] = ((df[df.publish_year == 2005]).mean().avg_rating)
    means[2006] = ((df[df.publish_year == 2006]).mean().avg_rating)
    means[2007] = ((df[df.publish_year == 2007]).mean().avg_rating)
    means[2008] = ((df[df.publish_year == 2008]).mean().avg_rating)
    means[2009] = ((df[df.publish_year == 2009]).mean().avg_rating)
    means[2010] = ((df[df.publish_year == 2010]).mean().avg_rating)
    means[2011] = ((df[df.publish_year == 2011]).mean().avg_rating)
    means[2012] = ((df[df.publish_year == 2012]).mean().avg_rating)
    means[2013] = ((df[df.publish_year == 2013]).mean().avg_rating)
    means[2014] = ((df[df.publish_year == 2014]).mean().avg_rating)
    means[2015] = ((df[df.publish_year == 2015]).mean().avg_rating)
    means[2016] = ((df[df.publish_year == 2016]).mean().avg_rating)
    means[2017] = ((df[df.publish_year == 2017]).mean().avg_rating)
    means[2018] = ((df[df.publish_year == 2018]).mean().avg_rating)
    means[2019] = ((df[df.publish_year == 2019]).mean().avg_rating)
    means[2020] = ((df[df.publish_year == 2020]).mean().avg_rating)


    #eans["2000"] = df[df.publish_year.eq(2000)].mean()
    means = means.drop(0, axis=1).transpose()

    print(means)

    plt.scatter(means.index, means)
    plt.show()


def main():
    df = pd.read_csv("clean_df.csv")
    # print(np.min(df.publish_year))
    # print(np.max(df.publish_year))
    #releases_by_year(df)
    #spike_in_releases(df)
    #rating_by_year(df)
    #pages_v_awards(df)
    #print(df.genres.value_counts())
    #print(df.publish_year.value_counts().sort_values())
    #print(np.shape(df))
    #ratings_by_year(df)
    #awards_by_year(df)

    print(df.genres.value_counts())


if __name__ == "__main__":
    main()
