# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 13:30:29 2022

@author: hp
"""


alltimes = input("Enter times in HH:MM\:SS:n").split()

for time in alltimes:

    hour, min, sec = time.split(":")
    print(hour, "hours and", min, "minutes", sec)
