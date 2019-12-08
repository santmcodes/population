# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
###############################################################################

Database connector
-------------------------------------
Author : Santosh Mishra(A00278085)
Created on Mon Nov  6 17:55:12 2019

Description : This code is responsible for reading from csv and loading databse
###############################################################################
"""

import csv 
import dbhelper

ds=open("C:\AIT\ASL\project\population\data\population.csv")
reader=csv.reader(ds)
headers=next(reader,None)
print(headers)
genderDistribution=dbhelper.connect('select male,female,county_ud from mytable group by county_ud,male,female')

#create table
query = """	CREATE TABLE public.mytable
	(
		geog_id character varying(59) COLLATE pg_catalog."default" NOT NULL,
		airo_ai_id integer NOT NULL,
		ed_ward character varying(43) COLLATE pg_catalog."default" NOT NULL,
		ed_ward_id character varying(43) COLLATE pg_catalog."default" NOT NULL,
		county_ud character varying(22) COLLATE pg_catalog."default" NOT NULL,
		country character varying(3) COLLATE pg_catalog."default" NOT NULL,
		totpop character varying(5) COLLATE pg_catalog."default" NOT NULL,
		male character varying(5) COLLATE pg_catalog."default" NOT NULL,
		female character varying(5) COLLATE pg_catalog."default" NOT NULL,
		popdenkm numeric(9,2) NOT NULL,
		age014t integer NOT NULL,
		age1524t integer NOT NULL,
		age2544t integer NOT NULL,
		age4564 integer NOT NULL,
		aeg65p integer NOT NULL,
		age1564 integer NOT NULL,
		age80p integer NOT NULL,
		depr numeric(5,1) NOT NULL,
		ydepr numeric(5,1) NOT NULL,
		odepr numeric(5,1) NOT NULL,
		sex_r character varying(5) COLLATE pg_catalog."default" NOT NULL,
		pc_male integer NOT NULL,
		pc_female numeric(4,1) NOT NULL,
		pcage014t numeric(4,1) NOT NULL,
		pcage1524t numeric(4,1) NOT NULL,
		pcage2544t numeric(4,1) NOT NULL,
		pcage4564 numeric(4,1) NOT NULL,
		pcaeg65p numeric(4,1) NOT NULL,
		pcage1564 numeric(5,1) NOT NULL,
		pcage80p numeric(4,1) NOT NULL,
		fert_r character varying(7) COLLATE pg_catalog."default" NOT NULL,
		CONSTRAINT mytable_pkey PRIMARY KEY (geog_id)
	)
"""
dbhelper.connect_create(query)
 


#load data
for row in reader:
    query="INSERT INTO public.mytable(geog_id, airo_ai_id, ed_ward, ed_ward_id, county_ud, country, totpop, male, female, popdenkm, age014t, age1524t, age2544t, age4564, aeg65p, age1564, age80p, depr, ydepr, odepr, sex_r, pc_male, pc_female, pcage014t, pcage1524t, pcage2544t, pcage4564, pcaeg65p, pcage1564, pcage80p, fert_r) 	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    dbhelper.load_data(query,row)

