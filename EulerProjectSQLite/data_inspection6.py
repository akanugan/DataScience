#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 18:43:33 2019

@author: skhalil
aim: Using generic function to inspect continuous variables
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
        
        inspect_continuous_var(varName='age',conn=conn)
        inspect_continuous_var(varName='duration',conn=conn)#duration in sec of last contact in current campaign 
        
        #Exercise : Find other continous variables (Use Data Dictionary on Synopsis Page).
        #Exercise : Call inspection on those variables.
        
        inspect_continuous_var(varName='pdays',conn=conn)#days since last contacted in this campaign
        inspect_continuous_var(varName='previous',conn=conn)# no of contacts
        #inspect_continuous_var(varName='cons_conf_idx',conn=conn)#confidence index
        #inspect_continuous_var(varName='cons_price_idx',conn=conn)#consumer price
        #inspect_continuous_var(varName='emp_var_rate',conn=conn)# employment variation rate
        #inspect_continuous_var(varName='nr_employed',conn=conn) # no of employees
        
        
    except Exception as err:
        Eu.print_error(err)
    finally:
        conn.close()

def inspect_continuous_var(varName,conn):
    try:
        #Min, Max, Mean
        sql = '''
        select min(?var?*1.) min_?var?, 
        round(avg(?var?*1.),0) mean_?var?, 
        max(?var?*1.) max_?var?
        from  bank
        '''.replace('?var?',varName)
        print ('Statistics for: '+varName)
        Eu.run(sql,conn)
        
        #Min, Max, Mean by class type
        sql = '''
        select y,count(*) n_people, 
        min(?var?*1.) min_?var?, 
        round(avg(?var?*1.),0) mean_?var?, 
        max(?var?*1.) max_?var?
        from  bank
        group by y
        '''.replace('?var?',varName)
        print ('Statistics for: '+varName+ ', grouped by y')
        Eu.run(sql,conn)
            
    except Exception as err:
        Eu.print_error(err)

if __name__ == '__main__':
    main()
