# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:20:01 2019

@author:Santosh Mishra
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
    midIndex=int(len(data)/2)
    if(midIndex % 2 == 1):
        median = data[midIndex]
    else:
        median = sum(data[midIndex-1:midIndex+1])/2
    return median

def getMaximumValue(value):
    frequencyValues=list(value.values())
    maxVal=max(frequencyValues)
    return maxVal

def getMaxValIndex(valueFrequency,maxValue):
    maxIndex=0
    for v in valueFrequency:
        if (valueFrequency[v]==maxValue):
            maxIndex=v
            break
    return maxIndex

def mode(data):
    data=sorted(data)
    valueFrequency={}
    for i in data:
        if i in list(valueFrequency.keys()):
            valueFrequency[i]=valueFrequency[i]+1
        else:
            valueFrequency[i]=1
            
    maxValue=getMaximumValue(valueFrequency)
    maxValueIndex=getMaxValIndex(valueFrequency,maxValue)
    
    return maxValueIndex

def std_deviations(data):
    data = [ float(x) for x in data ]
    mean=avg(data)
    deviations=[ (x - mean) ** 2 for x in data ]
    std_dev=sqrt(sum(deviations)/len(data)-1)
    
    return std_dev