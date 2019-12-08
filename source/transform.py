# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:14:15 2019

@author:Santosh Mishra
"""

def to_list_of_int(data):
    numericvalue=0
    
    for i in range(len(data)):
        if isinstance(data[i],str):
            data[i] = data[i].replace(',','') 
       
    try:
        numericvalue=[ int(i) for i in data ]
    except ValueError:
        numericvalue=[ float(i) for i in data ]
    
    return numericvalue

def to_numericvalue_dict(string_dict):
    numeric_dict={}          
    
    for key, value in string_dict.items():
        try:
            numeric_dict[key] = int(value)
        except ValueError:
            numeric_dict[key] = float(value)
    return numeric_dict        