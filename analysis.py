
import numpy as np
import pandas as pd

# Functions
def analydsis(DataFrame, author):
    df = DataFrame
    # Creates the group out of the years
    group = df.groupby(['original_publish_year'])
    # Finding the mean of minmax_norm_ratings
    means = df.groupby('minmax_norm_ratings').mean()
    # Returns the book with higher score of an author
    book = df.loc[df['minmax_norm_ratings'] == np.max(df['minmax_norm_ratings']), author]
    
    return group, means, book

if __name__ == "__main__":
    analysis()
else:
    print(
        'Call the analysis function with the DataFrame and an author for the corresponding arguments'
    )