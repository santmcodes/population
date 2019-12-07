# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
###############################################################################

Applied Scripting language Assignment
-------------------------------------
Author : Santosh Mishra(A00278085)
Subject :Population Study
Description : This program presents statistical analysis on a population data
This file in particular is main controller class that initiated the requests and
interacts other components 
###############################################################################
"""

import dbhelper
import transform
import visualization.report as report
import calculator.statistics as calculate
from prettytable import PrettyTable

header = """################################################################### 

Scripting language Assignment 
-------------------------------------
Author      : A00278085
Subject     :Population Study
Description : This program presents statistical analysis of a population study.
Disclaimer  : The source data used in the analysis and reports has been taken from
https://data.gov.ie/dataset/all-island-population-sa/resource/09abb272-a52a-4149-b8fc-9013d846594e?inner_span=True
All reports produced here are only for learning purpose.

###############################################################################
"""
def end_message():
    message = """
     ##########################################################################
     #                                                                        # 
     #Thank you for using this software - visit again                         #
     #A special thank you to Cormac McClean who coached me python from scratch#
     ###############################  Bye !  ##################################"""
    print(message)
       
print(header)

# Collecting data from postgress database
query='select county_ud,male as males,female as females, \
fert_r as fr from mytable' 
gender_distribution=dbhelper.connect(query)

# Data initialization and transfprmations
countywise_males=calculate.countywise_aggregate(gender_distribution,1) 
countywise_females=calculate.countywise_aggregate(gender_distribution,2) 

males=transform.to_list_of_int(list(countywise_males.values()))
county=list(countywise_males.keys())
females=transform.to_list_of_int(list(countywise_females.values()))

populationPerCounty={}
fertilityRatePerCounty={}
for i in gender_distribution:
    populationPerCounty[i[0]]=i[1]+i[2]
    fertilityRatePerCounty[i[0]]=i[3]

# presenting and collecting users choice
print("a) Gender Distribution in Counties")
while(True):
    choice=input("Enter what would you like to know or  q to quit : ")
    if (choice== 'q'):
        break
    else:
        if (choice == 'a'):
            print("General Stats ")
            tbl=PrettyTable()
            tbl.add_column('Statistics',['Mean','Median','Mode',
                                         'Standard Deviation'])
            tbl.add_column('Males',calculate.stats(males))
            tbl.add_column('Females',calculate.stats(females))
            print(tbl)
            report.draw_pie_chart(countywise_males,"Males in different Counties")
            legend_labels=["Males","Females"]
            report.draw_line_chart(county,males,females,"Gender distribution in different Counties",\
                    "Counties","No. of Population", legend_labels)
            report.draw_horizontal_bar_chart(transform.to_numericvalue_dict(countywise_males)," Males in differnt \
                              counties","Population","Counties")
#            report.drawBoxPlot(countywise_males,"Population in differnt \
#                              counties","Population")
end_message()            
# TODO: CSV interaction TBD:



            
            



    