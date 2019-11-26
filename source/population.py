# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Spyder Editor

This is a temporary script file.
"""

import dbhelper
import visualization.report as report
import calculator.statistics as calculate
# CSV interaction TBD:
query='select county_ud,count(male) as males,count(female) as females, \
count(fert_r) as fr from mytable group by county_ud' 
#query='select male,female,county_ud from mytable group by county_ud,male,female'
genderDistribution=dbhelper.connect(query)

populationPerCounty={}
fertilityRatePerCounty={}
males=[]
county=[]
females=[]
for i in genderDistribution:
    county.append(i[0])
    females.append(i[1])
    males.append(i[2])
    populationPerCounty[i[0]]=i[1]+i[2]
    fertilityRatePerCounty[i[0]]=i[3]
#avg=calculate.avg(males)
#print(f"Average number of males Age is {avg}")
med=calculate.median([10,20,30,40,10,20,30,30,30,10])
print(f"Median of males Age is {med}")
#mod=calculate.mode(males)
#print(f"Mode of males Age is {mod}")
  
#report.drawBarChart(county,males,"Male population in different Counties",\
#                    "Counties","No. of Males")
#report.drawPieChart(populationPerCounty,"Population in different Counties")    
#report.drawHorizontalBarChart(populationPerCounty,"Population in differnt \
#                              counties","Population","Counties")
#report.drawBoxPlot(fertilityRatePerCounty,"Population in differnt \
#                              counties","Population")