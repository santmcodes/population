# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:35:50 2019

@author:Santosh Mishra
"""

import source.calculator.statistics as calculate
import statistics as stats

data=[10,20,30,40,10,20,30,30,30,10]
sample_dict={'a':5,'b':1,'c':4,'d':2}
sample_dict2=[tuple('a'),tuple('b')]


def test_avg():
    assert calculate.avg(data)==stats.mean(data)
    
def test_median():
    assert calculate.median(data)==30
    
def test_mode():
    assert calculate.mode(data)==30.0

def test_std_deviations():
    assert calculate.std_deviations(data) == 10.0
    
def test_get_maximum_value():
    assert calculate.getMaximumValue(sample_dict) == 5

def test_getMaxValIndex():
    assert calculate.getMaxValIndex(sample_dict,4) == 'c'
    
def test_deviations():
    assert calculate.deviations(data) == [169.0, 169.0, 169.0, 9.0, 9.0, 49.0, 49.0, 49.0, 49.0, 289.0]
    
def test_countywise_aggregate():
    assert calculate.countywise_aggregate(sample_dict2,0) ==  {'a': 'a', 'b': 'b'}
    
if __name__=="__main__":
    test_std_deviations()
