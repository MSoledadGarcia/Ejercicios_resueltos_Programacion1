# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 23:00:04 2022

@author: maria
"""
import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
headers
row
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
record
record['name']

