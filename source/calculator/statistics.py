# -*- coding: utf-8 -*-
"""
###############################################################################

Database connector
-------------------------------------
Author : Santosh Mishra(A00278085)
Created on Mon Nov 18 12:20:01 2019

Description : This code is responsible for all sort of calculations used in stats

###############################################################################
"""

from math import sqrt

def avg(data):
    try:
        total=0
        for i in range(len(data)):
            total=total+data[i]       
        return total/len(data)
    except TypeError as e:
        print(f"{e}")
        print("please pass list of numbers")


def median(data):
    data.sort()
    median=0
    mid_index=int(len(data)/2)
    if(mid_index % 2 == 1):
        median = data[mid_index]
    else:
        median = sum(data[mid_index-1:mid_index+1])/2
    return median

def getMaximumValue(value):
    frequency_values=list(value.values())
    return max(frequency_values)

def getMaxValIndex(value_frequency,max_value):
    max_index=0
    for v in value_frequency:
        if (value_frequency[v]==max_value):
            max_index=v
            break
    return max_index

def mode(data):
    data=sorted(data)
    value_frequency={}
    for i in data:
        if i in list(value_frequency.keys()):
            value_frequency[i]=value_frequency[i]+1
        else:
            value_frequency[i]=1
            
    max_value=getMaximumValue(value_frequency)
    max_value_index=getMaxValIndex(value_frequency,max_value)
    
    return float(max_value_index)

def std_deviations(data):
    data = [ float(x) for x in data ]
    mean=avg(data)
    deviations=[ (x - mean) ** 2 for x in data ]
    std_dev=sqrt(sum(deviations)/len(data)-1)
    
    return std_dev

def deviations(data):
    data = [ float(x) for x in data ]
    mean=avg(data)
    deviations=[ (x - mean) ** 2 for x in data ]

    return deviations

def countywise_aggregate(data,index):
    aggregate_data={} 
    for d in data:
        if (d[0] not in aggregate_data.keys()):
            aggregate_data[d[0]]=d[index]
    return aggregate_data

def stats(data):
    return [format(avg(data),'.6'),
            format(median(data),'.6'),
            format(mode(data),'.6'),
            format(std_deviations(data),'.6')]