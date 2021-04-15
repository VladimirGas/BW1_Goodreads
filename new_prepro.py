"""
This is the preprocessing file, it contains all the functions related to getting the data ready to use
"""
from typing import Type

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

from pandas import Series


def mean_normalise(ratings_series):
    print(">> Normalising {} with repsect to the mean".format(ratings_series.name))
    # Normalise the passed data
    normalised = ((ratings_series - np.mean(ratings_series)) / (max(ratings_series) - min(ratings_series)))
    # Move into the range of 1-10
    print(">> Transforming values to between 1 and 10")
    one_to_ten = ((normalised + 1) * 4.5) + 1
    return one_to_ten


def min_max_norm(x):
    # x is a series
    return 1 + 9 * (x - min(x)) / (max(x) - min(x))


def normalise_ratings(raw_dataframe):
    clean_df["mean_norm"] = mean_normalise(raw_dataframe.avg_rating)
    clean_df["min_max_norm"] = min_max_norm(raw_dataframe.avg_rating)
    return


def clean_title():
    global wip_data
    wip_data = wip_data.dropna(axis=0, subset=["title"], thresh=1)
    return


def clean_pages():
    global wip_data
    wip_data = wip_data.dropna(axis=0, subset=["pages"], thresh=1)
    return


def clean_series():
    global wip_data
    wip_data.series = ~wip_data.series.isnull()
    return


def clean_genre():
    global wip_data
    # The Genres field has a lot of "<Number> users" entries, which are not helpful
    clean_genres = []

    for row in wip_data.genres[:]:
        data = row
        try:
            if "users" in row:
                data = re.sub(",? ?\'?[0-9]?[0-9]?[0-9]?,?[0-9]+ users?\'?,? ?", "", row)

            clean_genres.append(data)
        except:
            clean_genres.append(data)

    wip_data["clean_genres"] = clean_genres
    return


def clean_ratings():
    return


def clean_reviews():
    return


def clean_publish_year():
    global wip_data
    wip_data.publish_year = wip_data.publish_year.astype(int)


def preprocessing():
    global raw_data
    global wip_data
    global clean_df
    raw_data = pd.read_csv("books_data.csv")
    wip_data = raw_data.drop_duplicates()
    clean_df = pd.DataFrame()

    print(wip_data.columns)

    clean_title()
    clean_pages()
    clean_series()
    clean_genre()
    clean_ratings()
    clean_reviews()
    clean_publish_year()
    # Todo:
    # clean_places()
    # clean_awards()

    clean_df = wip_data
    normalise_ratings(raw_data)
    return clean_df


def main():
    preprocessing()


if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     clean_df = preprocessing("books.csv")
#     print("#####")
#     # print(clean_df)
#     clean_df.head()
