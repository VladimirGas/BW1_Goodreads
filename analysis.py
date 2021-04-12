#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:59:41 2021

@author: vladimirgasanov
"""
import numpy as np
import pandas as pd

# Functions
def main(file, author):
    # Creates a DataFrame
    df = pd.read_csv(file)
    # Creates the group out of the years
    group = df.groupby(['original_publish_year'])
    # Finding the mean of minmax_norm_ratings
    means = df.groupby('minmax_norm_ratings').mean()
    # Returns the book with higher score of an author
    book = df.loc[df['minmax_norm_ratings'] == np.max(df['minmax_norm_ratings']), author]
    return df, group, means, book

A = {
    'ratings': [1, 3, 4, 2, 5, 3],
    'original_publish_year': [2018, 2016, 2010, 2012, 2019, 2000],
    'minmax_norm_ratings': [.3, .4, .8, .2, .1, .6]
}

data = pd.DataFrame(A)