#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:51:13 2019

@author: skhalil

aim: Inspect variables: ‘marital’
"""

import sys
sys.path.append('/Users/skhalil/Desktop/Analysis/DataScience/EulerProjectSQLite/Euler')
#import Euler
from Euler import Euler as Eu

data_folder = '/Users/skhalil/Desktop/Analysis/DataScience/EulerProjectSQLite/bank_data/'
data_work   = data_folder+'data_work.db'

#M A I N  F U N C T I O N
#- - - - - - - - - - - - - - - - - - -
def main():
    conn = Eu.connection(data_work)
    try: 
        #Call data_ingestion to create a working database.
        data_ingestion()
        #Check the column names
        sql = '''
        SELECT sql FROM sqlite_master
        WHERE tbl_name = 'bank' AND type = 'table'
        ''' 
        Eu.run(sql,conn)
        
        #A look at the column: 'marital'
        sql = '''
        select distinct marital 
        from bank
        '''
        Eu.run(sql,conn)
        
        #Count how many entries for each value of marital
        sql = '''
        SELECT marital, 
        COUNT(*) n_people 
        FROM bank
        GROUP by marital
        '''
        Eu.run(sql,conn)
        
        #Order the results by descending order of people
        sql = '''
        SELECT marital,
        COUNT(*) n_people 
        FROM bank
        GROUP by marital 
        ORDER by n_people desc
        '''
        Eu.run(sql,conn)
        
    except Exception as err:
        Eu.print_error(err)
    finally:
        conn.close()
     

def data_ingestion():
    '''
    This function reads CSV file
    and loads it into a SQLITE 
    database in Table form.
    '''
    try:
        csvfile = data_folder+'bank_dataset.csv'
        pcsv = Eu.pycsv_reader(csvfile)
        #Dump into the database. Specify the tablename,sqlite filename etc
        pcsv.to_database(tabName='bank',database=data_work,verbose=False)
      
    except Exception as err:
        Eu.print_error(err)
    finally:
        pcsv.close()

if __name__ == '__main__':
    main()
