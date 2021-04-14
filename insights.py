import preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

# book_data = preprocessing.preprocessing("books.csv")
# book_data.to_csv("clean.csv")
# df = book_data

df = pd.read_csv("clean.csv")
print(df.columns)
print(df.original_publish_year.value_counts().sort_index())
print(df.original_publish_year.min())
print(df.original_publish_year.max())
print(df.original_publish_year.max() - df.original_publish_year.min())

year_ranges = [1976,1980,1985,1990,1995,2000,2005,2010,2015,2019]
plt.hist(df.original_publish_year.value_counts())

plt.show()
