# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv 
import psycopg2

ds=open("population.csv")
reader=csv.reader(ds)
headers=next(reader,None)
print(headers[0])    

db=psycopg2.connect("dbname=postgres user=postgres password=12shroot")
curr=db.cursor()
curr.execute('SELECT * from mytable')
db_version = curr.fetchone()
print(db_version)