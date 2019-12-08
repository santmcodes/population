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

    Applied Scripting language Assignment 
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
query='select county_ud,male,female,fert_r,age014t,age1564,aeg65p,age80p,totpop from mytable' 
population_distribution=dbhelper.connect(query)

# Data initialization and transfprmations
countywise_males=calculate.countywise_aggregate(population_distribution,1) 
countywise_females=calculate.countywise_aggregate(population_distribution,2) 
males=transform.to_list_of_int(list(countywise_males.values()))
county=list(countywise_males.keys())
females=transform.to_list_of_int(list(countywise_females.values()))

# presenting and collecting users choice
print("a) Gender Distribution in Counties")
print("b) Fertility Distribution in Counties")
print("c) Age distribution in Counties")
print("d) Total Population Distribution in Counties")

# Loop to present different choices    
while(True):
    try:
        choice=input("Enter what would you like to know (a,b,c,d) or  q to quit : ")
        if (choice.lower()== 'q'):
            break
        else:
            if (choice.lower() == 'a'):
                print("General Stats in any county")
                tbl=PrettyTable()
                tbl.add_column('Statistics',['Mean','Median','Mode',
                                             'Standard Deviation'])
                tbl.add_column('Average Males',calculate.stats(males))
                tbl.add_column('Females',calculate.stats(females))
                print(tbl)
                report.draw_pie_chart(countywise_males,"Males in different Counties")
                legend_labels=["Males","Females"]
                population_data=[county,males,females]
    
                report.draw_line_chart(population_data,"Gender distribution in different Counties","Counties","No. of Population", legend_labels)
                data_set=[transform.to_numericvalue_dict(countywise_males)]
                report.draw_horizontal_bar_chart(data_set," Males in differnt counties","Population","Counties",legend_labels)
    #            report.drawBoxPlot(countywise_males,"Population in differnt \
    #                              counties","Population")
            elif(choice.lower() == 'b'):
                fertilityrate_per_county={}
                for i in population_distribution:
                    fertilityrate_per_county[i[0]]=i[3]
                fertility_rate_values=transform.to_list_of_int(list(fertilityrate_per_county.values()))
                countywise_fertility=calculate.countywise_aggregate(population_distribution,3) 
    
                print("General Stats in any county")
                tbl=PrettyTable()
                tbl.add_column('Statistics',['Mean','Median','Mode',
                                             'Standard Deviation'])
                tbl.add_column('Males',calculate.stats(males))
                tbl.add_column('Females',calculate.stats(females))
                tbl.add_column('Fertility Rate',calculate.stats(fertility_rate_values))
                print(tbl)
                report.draw_pie_chart(countywise_fertility,"Fertility rate in different Counties")
                legend_labels=["Males","Fertility Rate"]
                population_data = [county,males,fertility_rate_values]
                report.draw_line_chart(population_data,"Fertility rate in different Counties","Counties","Fertility Rate", legend_labels)
                report.draw_horizontal_bar_chart([transform.to_numericvalue_dict(countywise_fertility)]," Fertility in differnt \
                                  counties","Fertility","Counties",legend_labels)
    #            report.drawBoxPlot(countywise_males,"Population in differnt \
    #                              counties","Population")
                
            elif(choice.lower() == 'c'):
                
                agebelow14_per_county={}
                age15to64_per_county={}
                age65_per_county={}
                age80_per_county={}
                
                for i in population_distribution:
                    agebelow14_per_county[i[0]]=i[4]
                    age15to64_per_county[i[0]]=i[5]
                    age65_per_county[i[0]]=i[6]
                    age80_per_county[i[0]]=i[7]
                
                agebelow14_values=transform.to_list_of_int(list(agebelow14_per_county.values()))
                age15to64_values=transform.to_list_of_int(list(age15to64_per_county.values()))
                age65_per_values=transform.to_list_of_int(list(age65_per_county.values()))
                age80_per_values=transform.to_list_of_int(list(age80_per_county.values()))
                
                countywise_agebelow14=calculate.countywise_aggregate(population_distribution,4) 
    
                print("General Stats in any county ")
                tbl=PrettyTable()
                tbl.add_column('Statistics',['Mean','Median','Mode',
                                             'Standard Deviation'])
                tbl.add_column('Males',calculate.stats(males))
                tbl.add_column('Females',calculate.stats(females))
                tbl.add_column('Age below 14',calculate.stats(agebelow14_values))
                tbl.add_column('Age 15 to 64',calculate.stats(age15to64_values))
                tbl.add_column('Age 65',calculate.stats(age65_per_values))
                tbl.add_column('Age 80 and above',calculate.stats(age80_per_values))
                print(tbl)
                          
                legend_labels=["Males","Age Below 14","Age 15 to 64","Age 65","Age 80 and above"]
                population_data=[county,males,agebelow14_values,age15to64_values,age65_per_values,age80_per_values]
                
                report.draw_line_chart(population_data,"Age distribution in different Counties","Counties","Age", legend_labels)
            elif(choice.lower() == 'd'):
                population_per_county={}
                for i in population_distribution:
                    population_per_county[i[0]]=i[8]
                population_values=transform.to_list_of_int(list(population_per_county.values()))
                countywise_population=calculate.countywise_aggregate(population_distribution,8) 
    
                print("General Stats in any county")
                tbl=PrettyTable()
                tbl.add_column('Statistics',['Mean','Median','Mode',
                                             'Standard Deviation'])
                tbl.add_column('Males',calculate.stats(males))
                tbl.add_column('Females',calculate.stats(females))
                tbl.add_column('Total Population',calculate.stats(population_values))
                print(tbl)
                report.draw_pie_chart(transform.to_numericvalue_dict(countywise_males),"Population in different Counties")
                legend_labels=["Males","Population"]
                population_data = [county,males,population_values]
                report.draw_line_chart(population_data,"Population in different Counties", "Counties","Population", legend_labels)
                report.draw_horizontal_bar_chart([transform.to_numericvalue_dict(countywise_males)]," Population in differnt counties","Population","Counties",legend_labels)
    #            report.drawBoxPlot(countywise_males,"Population in differnt \
    #                              counties","Population")        
            else:
                print(" Wrong Choice made, please try again !")
    except ValueError:
        print("Sorry unexpected type of data entered, please try again with valid values(a,b,c,d) ")
end_message()            


            
            



    