# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:35:50 2019

@author:Santosh Mishra
"""

import source.calculator.statistics as calculate
import statistics as stats

data=[10,20,30,40,10,20,30,30,30,10]

def test_avg():
    assert calculate.avg(data)==stats.mean(data)
    
def test_median():
    assert calculate.median(data)==stats.median(data)
    
def test_mode():
    assert calculate.mode(data)==stats.mode(data)

def test_std_deviations():
    assert calculate.std_deviations(data) == 10
    
    
if __name__=="__main__":
    test_std_deviations()
