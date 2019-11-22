# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

def drawBarChart(dataX,dataY,title,xlabel,ylabel):
    fig,ax=plt.subplots(figsize=(85,10))
    fig.align_labels()
    #ax.set_xlim([0,0])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)   
    ax.plot(dataX,dataY)
    publish()
    fig.savefig("male_dist.png",bbox_inches="tight")
    
def drawPieChart(dataN,title):
    fig,ax=plt.subplots(figsize=(85,20))
    fig.align_labels()
    ax.set_title(title)
    ax.pie(dataN.values(),labels=dataN.keys())
    publish()
    fig.savefig("male_dist_pie.png",bbox_inches="tight")
    
def drawHorizontalBarChart(dataN,title,xlabel,ylabel):
    fig,ax=plt.subplots(figsize=(85,10))
    ax.set_title(title)   
    y_pos=list(range(len(dataN)))    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dataN.keys())
    
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    
    ax.barh(y_pos,dataN.values(),align="center")
    publish()
     
def drawBoxPlot(dataN,title,ylabel):
    fig,ax=plt.subplots(figsize=(85,10))
    ax.set_title(title)   
    ax.set_ylabel(ylabel)
    ax.boxplot(dataN.values(),showfliers=False,vert=False,\
               labels=dataN.keys())
    publish()

def publish():
#   fig = plt.figure(tight_layout=True)
    plt.tight_layout()
    plt.show()