#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import os
import random
from pprint import pprint
from conf import logbox as log
from conf import getConfig


def listCategories(dataDirectory):
    '''
    
    Loading Filenames in Data Directory as Categories
    \param dataDirectory Directory where the data files are located
    \retval category list of Item categories
    
    '''
    category = []
    try:
        dirContents = os.listdir(dataDirectory)
    except:
        print("Datadirectory: " + dataDirectory)
        print("No Data found. Abort")
        sys.exit()
        
    if dirContents == []:
        print("Datadirectory is empty. Abort")
        sys.exit()
    else:
        for i in dirContents:
            if i.endswith(".csv"):
                category.append(i[:-4])
        
        return(category)

def getTables(configfile):
    '''
    
    Fill tables-dictionary with Contents of Data files
    Filles one dictionary with Categories and all items as list.
    \param configfile Name of the config file.
    \retval tables Content of temtables as dictionary
    
    '''
    dataDirectory = getConfig.readConfig(configfile)
    categories = listCategories(dataDirectory)
    tables = {}
    for cat in categories:
        entries = []
        filename = dataDirectory + "/" + cat + ".csv"
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entries.append(row)
            csvfile.close()
        tables[cat] = entries
    return(tables)


def fillTestInventory(tables):
    '''

    Adds three random Items from shop to player inventory
    key
    \param tables Content of temtables as dictionary
    \param characters List of characters
    \retval inventory Random dictionary Key = item category, Value = list of items
    

    ----
    
    
    '''
    print("fillTestInventory -- Working on it")
    numbers = 0
    selectcategory = 0
    selectitem = 0
    inventory = {}
    
    for j in range(0,3):
        selectcategory = random.randint(0,len(tables)-1)
        if tables.keys()[selectcategory] not in inventory.keys():
            inventory[tables.keys()[selectcategory]] = []
        print("selectcategory= "+ str(selectcategory) + " / " + str(len(tables)))
        items = tables[list(tables)[selectcategory]]
        selectitem = random.randint(0,len(items)-1)
        print("selectitem= "+ str(selectitem) + " / " + str(len(items)))
        print items[selectitem]['Item']
        #print items[list(items)[category]][selectitem]['Item']      
        inventory[tables.keys()[selectcategory]].append(items[selectitem])     
        pprint(inventory)
    return inventory
 
def loadCharacters(tables, characters = {"Char1" : [], "Char2" : [], "Char3" : []}):
    '''
    Loads Characters from file
     
    For mock purpose it fills the characters manually
    '''
    dummyDic = {}

    for key in tables.keys():
        dummyDic[key] = []
    
    # Hier dummyDic mit den Gegenständen füllen
    

    
    print("LoadCharacters")
    logger = log.createLogger("LoadChars", "debug", logpath='', logfile="rucksack.log")
    logger.debug("Test")
    return characters