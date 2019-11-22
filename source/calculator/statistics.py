# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 12:20:01 2019

@author:Santosh Mishra
"""
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
    median=0
    midIndex=int(len(data)/2)
    if(midIndex % 2 == 1):
        median = midIndex
    else:
        median = sum(data[midIndex-1:midIndex+1])/2
    return median