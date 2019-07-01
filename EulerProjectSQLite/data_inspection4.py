#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:01:09 2019

@author: skhalil
aim : Variable inspection !
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
        
        #Calling inspection on marital, job, education, deflt, 
        #housing, contact, campaign
        
        inspect_categorical_var(varName='marital',conn=conn)
        inspect_categorical_var(varName='job',conn=conn)
        #inspect_categorical_var(varName='education',conn=conn)
        #inspect_categorical_var(varName='deflt',conn=conn)
        #inspect_categorical_var(varName='housing',conn=conn)
        #inspect_categorical_var(varName='contact',conn=conn)
        #inspect_categorical_var(varName='campaign',conn=conn)
                       
    except Exception as err:
        Eu.print_error(err)
    finally:
        conn.close()


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
