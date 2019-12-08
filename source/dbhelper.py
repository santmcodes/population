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
    """
    connects to database and executes the query
    
    Parameters
    ----------
    query : string, must
    
    Returns
    -------
    result : tuple
        result of the sql query as tuples
    """
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
    """
    connects to database and executes the query to insert data
    
    Parameters
    ----------
    query : string, must
    row: data set as list
        
    Returns
    -------
    nothing : executes and commits
    
    """
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
    """
    connects to database and creates the resources like tables
    
    Parameters
    ----------
    query : string, must
        
    Returns
    -------
    nothing : executes and commits
    
    """
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