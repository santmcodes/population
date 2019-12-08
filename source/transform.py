# -*- coding: utf-8 -*-

"""
###############################################################################

Transformer
-------------------------------------
Author : Santosh Mishra(A00278085)
Created on Thu Dec  5 16:14:15 2019

Description : This code is responsible all sorts of complex transformations,
              that help in converting one datastructure to another

###############################################################################
"""

def to_list_of_int(data):
    """
    Convert passed data to list of String
    
    Parameters
    ----------
    data : List, mandatory
        
    Returns
    -------
    list : int/float
        list as asked by callee.
    """
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
    """
    Convert passed data to dictionary of numeric value
    
    Parameters
    ----------
    string_dict : Dictionary of string, mandatory
        
    Returns
    -------
    Dictionary : int/float
        dictionary as asked by callee.
    """
    numeric_dict={}          
    
    for key, value in string_dict.items():
        try:
            numeric_dict[key] = int(value)
        except ValueError:
            numeric_dict[key] = float(value)
    return numeric_dict        