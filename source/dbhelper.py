# -*- coding: utf-8 -*-
"""
###############################################################################

Database connector
-------------------------------------
Author : Santosh Mishra(A00278085)
Created on Mon Nov  4 17:55:12 2019

Description : This code is responsible for making database connections

###############################################################################
"""
import psycopg2
from config.dbconfig import datasource

def connect(query):
    conn=None
    try:
        params=datasource()
        db=psycopg2.connect(**params)
        curr=db.cursor()
        curr.execute(query)
        result = curr.fetchall()
        curr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection is closed")
            
    return result 

def load_data(query,row):
    conn=None
    try:
        params=datasource()
        db=psycopg2.connect(**params)
        curr=db.cursor()
        curr.execute(query,row)
        db.commit()
        curr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection is closed")

def connect_create(query):
    conn=None
    try:
        params=datasource()
        db=psycopg2.connect(**params)
        curr=db.cursor()
        curr.execute(query)
        curr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection is closed")
            
#if __name__=='__main__':
#    connect()