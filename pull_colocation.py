#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:14:14 2020

@author: hamishgibbs

implement unit tests

make a reader file of target urls for different countries mobility and colocation

"""

import sys
import pandas as pd
from utils import download_data, move_most_recent_files, get_update_date
from colocation import get_file_dates, get_urls
from datetime import datetime
from getpass import getpass
from itertools import compress

#%%   

def main(_args):
    '''
    download colocation data
    
    Parameters
    ----------
    _args : list
        Arg list facebook keys, outdir. n

    Returns
    -------
    None.

    '''
    
    username = input("Username: ")
        
    password = getpass()
    
    keys = [username, password]
    
    #check if updating or downloading full ts
    update = input("Update datasets? (y/n): ")
    
    if update == 'y':
        update = True
    elif update == 'n':
        update = False
    else:
        sys.exit('Unknown update input. Choose "y", "n". Exiting.')
        
    #read target datasets
    data_target = pd.read_csv(_args[1]) 
    
    for i, dataset_id in enumerate(data_target['id']):
        
        country_output = _args[len(_args) - 1] + "/" + data_target.loc[i, 'country'] + '_colocation'
    
        base_url = 'https://www.facebook.com/geoinsights-portal/downloads/vector/?id=' + str(dataset_id) + '&ds='
        
        earliest_date = datetime(int(data_target.loc[i, 'year']), int(data_target.loc[i, 'month']), int(data_target.loc[i, 'day']))
    
        data_dates = get_file_dates(earliest_date)
        
        if update:
            data_dates = list(compress(data_dates, [x > get_update_date(country_output) for x in data_dates]))
        
        if len(data_dates) == 0:
            sys.exit('No datasets to download. Exiting.')
        
        urls = get_urls(base_url, data_dates)
        
        download_data(urls, keys)
    
        move_most_recent_files(_args[len(_args) - 1] + "/" + data_target.loc[i, 'country'] + '_colocation', urls)
    
    print('Success.')

#%%
if __name__ == "__main__":
    
    _args = sys.argv

    main(_args)

        
