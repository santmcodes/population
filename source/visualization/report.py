# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import os

def publish(fig,title):
    plt.tight_layout()
    plt.show()
    fig.savefig(os.path.realpath('.') + "\\..\\"+ "outputreport\\"+title + ".png",bbox_inches="tight")

def draw_line_chart(population_data,title,xlabel,ylabel,legend_label):
    fig,ax=plt.subplots(figsize=(55,20))
    fig.align_labels()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    for i in range(1:len(population_data)):
        ax.plot(population_data[0],population_data[i],label=legend_label[i-1],loc=2)
    ax.legend(loc=2)
    publish(fig,title + " line chart")
    
def draw_pie_chart(dataN,title):
    fig,ax=plt.subplots(figsize=(20,20))
    fig.align_labels()
    ax.set_title(title)
    ax.pie(dataN.values(),labels=dataN.keys())
    ax.legend()
    publish(fig,title+ " Pie chart")
    
def draw_horizontal_bar_chart(dataN,title,xlabel,ylabel,legend_label):
    fig,ax=plt.subplots(figsize=(85,10))
    ax.set_title(title)   
    y_pos=list(range(len(dataN[0])))    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dataN[0].keys())    
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    for i in range(len(dataN)):
        ax.barh(y_pos,dataN[i].values(),align="center")
    ax.legend(legend_label,loc=2)
    publish(fig,title + " bar chart")
     
def drawBoxPlot(dataN,title,ylabel):
    fig,ax=plt.subplots(figsize=(85,10))
    ax.set_title(title)   
    ax.set_ylabel(ylabel)
    ax.boxplot(dataN.values(),showfliers=False,vert=False,\
               labels=dataN.keys())
    ax.legend()
    publish(fig,title + " box chart")


