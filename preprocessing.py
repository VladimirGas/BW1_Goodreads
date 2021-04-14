"""
This is the preprocessing file, it contains all the functions related to getting the data ready to use
"""
import pandas as pd
import numpy as np
import re

"""
Daniel, I've added your functions here and into the preprocessing() function, 
"""


def cleaning_num(ints):
    # This function is used to clean up both num_ratings and num_reviews
    # print(">> Cleaning {}".format(ints))
    return pd.Series(int(el.split()[0].replace(',', '')) for el in ints)


def cleaning_places(places):
    # print(">> Cleaning {}".format(places))
    unclean = [str(el).split('\n') for el in places]
    clean1 = []
    for el in unclean:
        clean1.append(
            [place.replace('…more', '').replace('…less', '').replace('(', '').replace(')', '').replace('|', '') for
             place in el if place != ''])
    clean2 = []
    for part in clean1:
        clean2.append([el.strip() for el in part])
    clean = []
    for i in clean2:
        clean.append([el for el in i if el != ''])
    return pd.Series(clean)


def preprocessing(csv_path):
    book_dataframe = pd.read_csv(csv_path)
    book_dataframe = clean_data(book_dataframe)
    book_dataframe = convert_ratings(book_dataframe)

    return book_dataframe


def mean_normalise(ratings_series):
    print(">> Normalising {} with repsect to the mean".format(ratings_series.name))
    # Normalise the passed data
    normalised = ((ratings_series - np.mean(ratings_series)) / (max(ratings_series) - min(ratings_series)))
    # Move into the range of 1-10
    print(">> Transforming values to between 1 and 10")
    one_to_ten = ((normalised + 1) * 4.5) + 1
    return one_to_ten


def clean_num_pages(num_pages_series):
    print(">> Cleaning {}".format(num_pages_series.name))
    num_pages_series = num_pages_series.fillna("0 pages")

    # For num_pages, we only want the number of pages so we remove the excess text (e.g. "100 pages" --becomes-> 100)
    return (num_pages_series.str.replace(" pages", "")).astype(int)


def clean_publish_year(original_publish_year_series):
    print(">> Cleaning {}".format(original_publish_year_series.name))
    # original_publish_year_series = (original_publish_year_series.fillna(0,inplace=True))
    # publish_years = (original_publish_year_series.str.extract(r'([0-9]{4})', expand=False)).astype(int)
    # publish_years = publish_years.fillna(0)
    # For original_publish year, we only need the year, which we can find via a RegEx that looks for 4 sequential numbers (e.g. 1984) 
    return original_publish_year_series.str.extract(r'([0-9]{4})', expand=False).astype(int)
    #return publish_years

def clean_series(book_series_series):
    print(">> Cleaning {}".format(book_series_series.name))
    # For series, we only need to see if something IS a series or not, so we can use a boolean
    return book_series_series.notnull()


def clean_awards(awards_series):
    print(">> Cleaning {}".format(awards_series.name))
    # For Awards, we only want the number of awards, We'll count how many (YEAR)s there are, and replace any NaNs with a 0
    return (awards_series.str.count(r"([0-9]{4})")).replace(np.nan, 0)


def clean_genres(genres_series):
    print(">> Cleaning {}".format(genres_series.name))
    # For genres, I'm just going to replace "Science Fiction" with "Sci-Fi"
    return genres_series.str.replace("Science Fiction", "Sci-Fi")


def clean_data(dataframe):
    df = dataframe
    print("-- Cleaning data...")
    df.num_pages = clean_num_pages(df.num_pages)
    df.original_publish_year = clean_publish_year(df.original_publish_year)
    df.series = clean_series(df.series)

    # df.awards = clean_awards(df.awards)
    df["awards_won"] = clean_awards(df.awards)

    df.genres = clean_genres(df.genres)

    # Daniel 
    print(">> Cleaning num_ratings")
    df.num_ratings = cleaning_num(df.num_ratings)
    print(">> Cleaning num_reviews")
    df.num_reviews = cleaning_num(df.num_reviews)
    print(">> Cleaning places")
    df.places = cleaning_places(df.places)
    ###

    print("-- Cleaning complete!")
    return df


def convert_ratings(dataframe):
    df = dataframe
    print("Converting ratings...")
    df["mean_norm_ratings"] = mean_normalise(df.avg_rating)
    df["min_max_norm_ratings"] = min_max_norm(df.avg_rating)
    print("Conversion complete!")
    return df


def min_max_norm(x):
    # x is a series
    x = np.array(x)
    return 1 + 9 * (x - min(x)) / (max(x) - min(x))


if __name__ == "__main__":
    clean_df = preprocessing("books.csv")
    print("#####")
    # print(clean_df)
    clean_df.head()
