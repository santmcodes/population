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

def draw_line_chart(dataX,dataY,dataZ,title,xlabel,ylabel,legend_label):
    fig,ax=plt.subplots(figsize=(55,20))
    fig.align_labels()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.plot(dataX,dataY,label=legend_label[0])
    ax.plot(dataX,dataZ,label=legend_label[1])
    ax.legend()
    publish(fig,title)
    
def draw_pie_chart(dataN,title):
    fig,ax=plt.subplots(figsize=(20,20))
    fig.align_labels()
    ax.set_title(title)
    ax.pie(dataN.values(),labels=dataN.keys())
    ax.legend()
    publish(fig,title)
    
def draw_horizontal_bar_chart(dataN,title,xlabel,ylabel):
    fig,ax=plt.subplots(figsize=(85,10))
    ax.set_title(title)   
    y_pos=list(range(len(dataN)))    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dataN.keys())
    
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    
    ax.barh(y_pos,dataN.values(),align="center")
    ax.legend()
    publish(fig,title)
     
def drawBoxPlot(dataN,title,ylabel):
    fig,ax=plt.subplots(figsize=(85,10))
    ax.set_title(title)   
    ax.set_ylabel(ylabel)
    ax.boxplot(dataN.values(),showfliers=False,vert=False,\
               labels=dataN.keys())
    ax.legend()
    publish(fig,title)


