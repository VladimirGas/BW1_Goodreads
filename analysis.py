#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:59:41 2021

@author: vladimirgasanov
"""
import numpy as np
import pandas as pd

a = np.random.randint(10, size = 100)
b = np.random.randint(10, size = 100)

a_list = {'a': a, 'b':b }

with open('file.py', 'w') as file:
    file.write(a)

def open_file(file):
    with open(file, 'r') as csv:
        data = csv.read()
    return data