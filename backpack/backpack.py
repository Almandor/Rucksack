#!/usr/bin/env python

'''
\package Rucksack
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
from pprint import pprint
import src.modules


configfile = 'backpack.cfg'

def readConfig(configfile):
    # Checking for Config File
    if os.path.isfile(configfile):
        config = ConfigParser.ConfigParser()
        config.read(configfile)
        try:
            dataDirectory = config.get("1",'DataDirectory')
        except:
            print("DataDirectory not configured. Using defaults")
            dataDirectory = "./Data"
    else:
        print("Config file not found. Using defaults")
        dataDirectory = "./Data"

    return(dataDirectory)

def listCategories(dataDirectory):
    # Loading Filenames in Data Directory as Categories
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
    # Fill tables-dictionary with Contents of Data files
    dataDirectory = readConfig(configfile)
    categories = listCategories(dataDirectory)
    tables = {}
    for i in categories:
        entries = []
        filename = dataDirectory + "/" + i + ".csv"
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entries.append(row)
            csvfile.close()
        tables[i] = entries
    return(tables)





tables = getTables(configfile)
pprint(tables)
#===============================================================================
# root = Tk()
# 
# labelMain = Label(root, text="Get Inventory")
# labelMain.grid()
# 
# root.mainloop()
#===============================================================================