#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:59:41 2021

@author: vladimirgasanov
"""
import numpy as np
import pandas as pd
import csv

# Necessary functions
def open_file(file):
    with open(file, 'r') as csv:
        data = csv.read()
    return data