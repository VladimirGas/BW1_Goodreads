
import numpy as np
import pandas as pd

# Functions
def analysis(file, author):
    # Creates a DataFrame
    df = pd.read_csv(file)
    # Creates the group out of the years
    group = df.groupby(['original_publish_year'])
    # Finding the mean of minmax_norm_ratings
    means = df.groupby('minmax_norm_ratings').mean()
    # Returns the book with higher score of an author
    book = df.loc[df['minmax_norm_ratings'] == np.max(df['minmax_norm_ratings']), author]
    
    return df, group, means, book

if __name__ == "__main__":
    analysis()
else:
    print(
        'Call the analysis function with a csv file and an author for the corresponding arguments'
    )