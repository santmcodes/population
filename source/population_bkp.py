# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Spyder Editor

This is a temporary script file.
"""
import csv 
import dbhelper
#import calc
import matplotlib.pyplot as plt

ds=open("C:\AIT\ASL\project\population\data\population.csv")
reader=csv.reader(ds)
headers=next(reader,None)
print(headers)
genderDistribution=dbhelper.connect('select male,female,county_ud from mytable group by county_ud,male,female')

males=[]
county=[]
females=[]
for i in genderDistribution:
    males.append(int(i[0].replace(',','')))
    females.append(int(i[1].replace(',','')))
    county.append(i[2])

yinterval = [0]
i=0
while(max(yinterval)<max(males)):  
    yinterval.append(yinterval[i]+round(max(males)*0.05))
    i+=1
#    print(yinterval[i])
    
#xinterval = [0]
#i=0
#while(max(xinterval)<int(max(females))):  
#    xinterval.append(xinterval[i]+(int(max(females))*0.1))
#    i+=1
#    print(xinterval[i])
    
xinterval = [0]
i=0
noOfCounties=len(county)
while(max(xinterval)<noOfCounties):  
    xinterval.append(xinterval[i]+round(noOfCounties*0.1))
    i+=1

#print(calc.avg(total[0][0],count[0][0]))
plt.figure(figsize=(30,10))
plt.yticks(yinterval)
plt.xticks(yinterval,county)
p1=plt.bar(yinterval,males,50, xinterval)
#p2=plt.bar(females,females,bottxom=females)
#plt.show()
