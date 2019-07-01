#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:25:00 2019

@author: skhalil
aim: Develop a generic function for inspecting continuous variables.
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
        #Eu.run(sql,conn)
        
        ##A look at the 'age'
        sql = '''
        select age*1. from bank limit 10
        '''
        #Eu.run(sql,conn)
        
        ###Average age in sample
        sql = '''
        select avg(1.*age) mean_age  from bank
        '''
        #Eu.run(sql,conn)
        
        ####Min, Max, Mean
        sql = '''
        select min(age*1.) min_age, 
        round(avg(age*1.),0) mean_age, 
        max(age*1.) max_age
        from  bank
        '''
        #Eu.run(sql,conn)
        
        #####Min, Max, Mean by class type
        sql = '''
        select y,count(*) n_people, 
        min(age*1.) min_age, 
        round(avg(age*1.),0) mean_age, 
        max(age*1.) max_age
        from  bank
        group by y
        '''
        Eu.run(sql,conn)
    
        # Exercise: Fix the function
        inspect_continuous_var(varName='duration',conn=conn)
        inspect_continuous_var(varName='age',conn=conn)
        
    except Exception as err:
        Eu.print_error(err)
    finally:
        conn.close()

def inspect_continuous_var(varName,conn):
    '''
    Exercise: Fix this function so that
    it fetches information for 'varName'
    instead of 'age'.
    '''
    try:
        #Min, Max, Mean
        sql = '''
        select min(?varN?*1.) min_?varN?, 
        round(avg(?varN?*1.),0) mean_?varN?, 
        max(?varN?*1.) max_?varN?
        from  bank
        '''
        sql = sql.replace('?varN?',varName)
        print ('Statistics for: '+varName)
        Eu.run(sql,conn)
        
        #Min, Max, Mean by class type
        sql = '''
        select y,count(*) n_people, 
        min(?varN?*1.) min_?varN?, 
        round(avg(?varN?*1.),0) mean_?varN?, 
        max(?varN?*1.) max_?varN?
        from  bank
        group by y
        '''
        sql = sql.replace('?varN?',varName)
        print ('Statistics for: '+varName+ ', grouped by y')
        Eu.run(sql,conn)
            
    except Exception as err:
        Eu.print_error(err)

if __name__ == '__main__':
    main()