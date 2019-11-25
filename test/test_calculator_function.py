# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:35:50 2019

@author:Santosh Mishra
"""

import calculator.statistics as calculate

data=[10,20,30,40]

def test_avg():
    assert calculate.avg(data)==5

#if __name__=='__main__':
#    test_avg()