# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:11:46 2022

@author: LENOVO
"""

def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
print most_frequent('Mississippi')