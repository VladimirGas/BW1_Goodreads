#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:59:41 2021

@author: vladimirgasanov
"""
import numpy as np
import pandas as pd

# Functions
def open_file(file):
    return pd.read_csv(file)

def groupby(df):
    return df.groupby(['original_publish_year'])

def best_book(df, author):
    h_rate = np.max(df['minmax_norm_ratings'])
    return 


def main(file, author):
    df = open_file(file) # Create DataFrame
    group = groupby(df)
    
    return df, group


# min_max_norm_ratings means
means = df.groupby('minmax_norm_ratings').mean()


a = groupby(df, ['original_publish_year'])

print(a)