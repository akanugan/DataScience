#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:00:27 2019

@author: skhalil

aim: Inspect variables: ‘marital’, ‘job’
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
        
        #Exercise: Following function needs fixing
        inspect_job(conn)
        
    except Exception as err:
        Eu.print_error(err)
    finally:
        conn.close()

def inspect_marital(conn):
    '''
    This function examines
    the variable 'marital'
    '''
    try:
        #A look at the 'marital'
        sql = '''
        select distinct marital from bank
        '''
        Eu.run(sql,conn)
                
        #Order the results by descending order of people
        sql = '''
        select marital, count(*) n_people from bank
        group by marital order by n_people desc
        '''
        Eu.run(sql,conn)
    except Exception as err:
        Eu.print_error(err)


def inspect_job(conn):
    '''
    This function examines
    the variable 'job'
    '''
    try:
        #A look at the 'job'
        sql = '''
        select distinct job from bank
        '''
        Eu.run(sql,conn)
                
        #Order the results by descending order of people
        sql = '''
        select job, count(*) n_people from bank
        group by job order by n_people desc
        '''
        Eu.run(sql,conn)
    except Exception as err:
        Eu.print_error(err)
        


if __name__ == '__main__':
    main()