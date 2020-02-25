#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv
import os
import random
from pprint import pprint
from inventory_config import logbox as log
from inventory_config import getConfig
import json


class inventoryHandler():
    '''
    Handles the inventory operations and keeps the inventory dictionary
    '''
    def __init__(self):
        self.inventory = {}
        print("Setting up Inventory...")

    def add(self, item, selection):
        '''
        @param item: Receives the list from the GUI which contains the bought item data
        @param selection: Contains the selected category as string
        :return:
        '''
        # print(item) # debug_print
        # print(selection)

        if selection not in self.inventory:
            self.inventory[selection] = []

        self.inventory[selection].append(item)

    def remove(self, item, selection):
        '''
        @param item: Receives the list from the GUI which contains the removed item data
        @param selection: Contains the selected category as string
        :return:
        '''
        print(item)
        try:
            self.inventory[selection].remove(item)
        except:
            pass
        if len(self.inventory[selection]) == 0:
            del(self.inventory[selection])

    def save(self):
        # print(json.dumps(self.inventory, sort_keys=True, indent=4))
        f = open('../save/savefile.json', "w")
        f.write((json.dumps(self.inventory, sort_keys=True, indent=4)))
        f.close()


    def load(self):
        f = open('../save/savefile.json', "r")
        self.temp = json.loads(f.read())
        f.close()
        print(self.temp)


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
        print(("Datadirectory: " + dataDirectory))
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
    config_dict = getConfig.readConfig(configfile)
    categories = listCategories(config_dict["DataDirectory"])
    tables = {}
    for cat in categories:
        entries = []
        filename = config_dict["DataDirectory"] + "/" + cat + ".csv"
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entries.append(row)
            csvfile.close()
        tables[cat] = entries
    return(tables)


def save_inventory(name, equipment):
    pass