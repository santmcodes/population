# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
###############################################################################

Visualization report publisher
-------------------------------------
Author : Santosh Mishra(A00278085)
Created on Mon Nov 18 12:20:01 2019

Description : This code is responsible for publishing all visualization reports

###############################################################################
"""
import matplotlib.pyplot as plt
import os

def publish(fig,title):
    """
    publish charts of passed figure with asked title
    
    Parameters
    ----------
    fig : figure, mandatory
    title: String, mandatory
        
    Returns
    -------
    nothing, just published the graph
        
    """
    plt.tight_layout()
    plt.show()
    fig.savefig(os.path.realpath('.') + "\\..\\"+ "outputreport\\"+title + ".png",bbox_inches="tight")

def draw_line_chart(population_data,title,xlabel,ylabel,legend_label):
    """
    puslish line chart of passed data
    
    Parameters (all mandatory)
    ----------
    population_data : list
                    list of lince carts to be drawn on same graphs
    title: String
            title of the graph
    xlabel:  string
            x-axis labels
    ylabel:  string
            y axis labels
    legend_label : List of String
            list of labels to be shown in legend
      
    Returns
    -------
    nothing, just published the graph
        
    """
    fig,ax=plt.subplots(figsize=(55,20))
    fig.align_labels()
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    for i in range(1,len(population_data)):
        ax.plot(population_data[0],population_data[i],label=legend_label[i-1])
    ax.legend(loc=2)
    publish(fig,title + " line chart")
    
def draw_pie_chart(dataN,title):
    """
    puslish pie chart of passed data
    
    Parameters (all mandatory)
    ----------
    dataN : Dictionary
            key value of data to be drawn to be drawn on same graphs
    title: String
            title of the graph
     
    Returns
    -------
    nothing, just published the graph
        
    """

    fig,ax=plt.subplots(figsize=(20,20))
    fig.align_labels()
    ax.set_title(title)
    ax.pie(dataN.values(),labels=dataN.keys())
    ax.legend()
    publish(fig,title+ " Pie chart")
    
def draw_horizontal_bar_chart(dataN,title,xlabel,ylabel,legend_label):
    """
    puslish horizontal bar chart of passed data
    
    Parameters (all mandatory)
    ----------
    dataN : Dictionary
            key value of data to be drawn on same graphs
    title: String
            title of the graph
    xlabel:  string
            x-axis labels
    ylabel:  string
            y axis labels
    legend_label : List of String
            list of labels to be shown in legend
      
    Returns
    -------
    nothing, just published the graph
        
    """
    
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
    """
    puslish horizontal bar chart of passed data
    
    Parameters (all mandatory)
    ----------
    dataN : Dictionary
            key value of data to be drawn on same graphs
    title: String
            title of the graph
    ylabel:  string
            y axis labels
      
    Returns
    -------
    nothing, just published the graph
        
    """    
    fig,ax=plt.subplots(figsize=(85,10))
    ax.set_title(title)   
    ax.set_ylabel(ylabel)
    ax.boxplot(dataN.values(),showfliers=False,vert=False,\
               labels=dataN.keys())
    ax.legend()
    publish(fig,title + " box chart")


