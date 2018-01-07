#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
\package backpack
\file backpack.py

\brief first installment of a backpack handling tool

The program is intended to supplement players of P&P games to handle their backpack.

Done:
- Reading Config file
- Importing itemcategories from CSV-filenames
- Importing items from CSV files into one dictionary

\author Christian Wunderlich
\date (c) 2017
\version 0.0.1 alpha
\email cwunderlich@almandor.de
\todo Todo list
- userinterface
- usermanagment
- inventorymanagement
- export
'''

from Tkinter import *
import ConfigParser
import os
import sys
import csv
import random
from pprint import pprint
# from unicodedata import category

# import src.modules


def readConfig(configfile = 'backpack.cfg'):
    '''
    
    Checking for Config File
    \param configfile Name of the config file.
    \retval dataDirectory Directory where the data files are located
        Returns ./Data if no directory found in config file.
    
    '''
    if os.path.isfile(configfile):
        config = ConfigParser.ConfigParser()
        config.read(configfile)
        try:
            dataDirectory = config.get("global",'DataDirectory')
        except:
            print("DataDirectory not configured. Using defaults")
            dataDirectory = "./Data"
    else:
        print("Config file not found. Using defaults")
        dataDirectory = "./Data"

    return(dataDirectory)

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
    \param configfile Name of the config file.
    \retval tables Content of temtables as dictionary
    
    '''
    dataDirectory = readConfig(configfile)
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

    return characters


if __name__ == '__main__':
  
    # Variables
    configfile = 'backpack.cfg'
 
    tables = getTables(configfile)
    characters = loadCharacters(tables)
    
    pprint(characters)
    
    for key in characters.keys():
        print("Filling Character " + key)
        characters[key] = fillTestInventory(tables) # Achtung! FillTestInventory hat noch keine Rückgabe!!
        for char in characters:
            print "%s %s"%(char,str(characters[char]))
    

#===============================================================================
# root = Tk()
# 
# labelMain = Label(root, text="Get Inventory")
# labelMain.grid()
# 
# root.mainloop()
#===============================================================================