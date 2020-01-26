#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:33:18 2020

@author: wlhendr
"""

class Data:
    def __init__(self):
        self.key = str
        self.long = float
        self.lat = float
        
######## TEST FILE 1 ########
        
filename = 'test01.txt'
test01_data = []
emptyData = Data()
emptyData.key = None
emptyData.long = -1
emptyData.lat = -1
test01_data.append(emptyData)

input = open(filename, 'r')
for line in input:
    key, long, lat  = line.split()
    
    temp = Data()
    temp.key = key
    temp.long = float(long)
    temp.lat = float(lat)
    
    test01_data.append(temp)

input.close()

######## TEST FILE 2 ########
filename = 'test02.txt'
test02_data = []
emptyData = Data()
emptyData.key = None
emptyData.long = -1
emptyData.lat = -1
test02_data.append(emptyData)

input = open(filename, 'r')
for line in input:
    key, long, lat  = line.split()
    
    temp = Data()
    temp.key = key
    temp.long = float(long)
    temp.lat = float(lat)
    
    test02_data.append(temp)

input.close()

######## TEST FILE 3 ########
filename = 'test03.txt'
test03_data = []
emptyData = Data()
emptyData.key = None
emptyData.long = -1
emptyData.lat = -1
test03_data.append(emptyData)

input = open(filename, 'r')
for line in input:
    key, long, lat  = line.split()
    
    temp = Data()
    temp.key = key
    temp.long = float(long)
    temp.lat = float(lat)
    
    test03_data.append(temp)

input.close()


######## END INPUT DATA ########

avg_vals = []
avg_vals.append(emptyData)
for i in range(1, len(test01_data)):
    print("Curr location ID:",i)
    temp_avg = Data()
    temp_avg.key = "ID" + str(i)
    temp_avg.long = (test01_data[i].long + test02_data[i].long + test03_data[i].long) / 3
    temp_avg.lat = (test01_data[i].lat + test02_data[i].lat + test03_data[i].lat) / 3
    avg_vals.append(temp_avg)
    
    print("Long:")
    print("   ",test01_data[i].long)
    print("   ",test02_data[i].long)
    print("   ",test03_data[i].long)
    print("   AVG = ", avg_vals[i].long)
    
    print("Lat:")
    print("   ",test01_data[i].lat)
    print("   ",test02_data[i].lat)
    print("   ",test03_data[i].lat)
    print("   AVG = ", avg_vals[i].lat)

    





































#



