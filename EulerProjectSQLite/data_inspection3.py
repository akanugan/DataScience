#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:48:26 2019

@author: skhalil

aim: Create a generic function for variable inspection using Euler toolkit.
"""
import sys
sys.path.append('/Users/skhalil/Desktop/Analysis/DataScience/EulerProjectSQLite/Euler')
#import Euler
from Euler import Euler as Eu

data_folder = '/Users/skhalil/Desktop/Analysis/DataScience/EulerProjectSQLite/bank_data/'
data_work   = data_folder+'data_work.db'

#M A I N   F U N C T I O N
def main():
    conn = Eu.connection(data_work)
    try:        
        sql = '''
        SELECT sql FROM sqlite_master
        WHERE tbl_name = 'bank' AND type = 'table'
        ''' 
        Eu.run(sql,conn)
        
        #Calling inspect marital function
        inspect_marital(conn)
        #Calling inspect marital function
        inspect_job(conn)
        
        #Calling inspect categorical function
        inspect_categorical_var(varName='job',conn=conn)
            
    except Exception as err:
        Eu.print_error(err)
    finally:
        conn.close()
        
def inspect_marital(conn):
    try:
        #A look at the 'marital'
        sql = '''
        select distinct marital from bank
        '''
        Eu.run(sql,conn)
                
        #Order the results by descending order of people
        sql = '''
        select marital,count(*) n_people from bank
        group by marital order by n_people desc
        '''
        Eu.run(sql,conn)
    except Exception as err:
        Eu.print_error(err)

        
def inspect_job(conn):
    try:
        #A look at the 'marital'
        sql = '''
        select distinct job from bank
        '''
        Eu.run(sql,conn)
                
        #Order the results by descending order of people
        sql = '''
        select job,count(*) n_people from bank
        group by job order by n_people desc
        '''
        Eu.run(sql,conn)
    except Exception as err:
        Eu.print_error(err)
    
    
def inspect_categorical_var(varName,conn):
    '''
    Informal Inspection of Variables
    Parameters:
     varName : Variable to be inspected.
     conn    : Connection to sqlite database.
    '''
    try:
        sql = '''
        select ?varN?, count(*) n_people from bank
        group by ?varN?
        '''
        sql = sql.replace('?varN?',varName)
        print (sql)
        Eu.run(sql,conn)
    except Exception as err:
        Eu.print_error(err)
        

if __name__ == '__main__':
    main()        


