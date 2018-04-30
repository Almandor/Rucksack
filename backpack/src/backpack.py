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
from backend import inventory as inv
from pprint import pprint
from conf import logbox as log
# from unicodedata import category

# import src.modules







if __name__ == '__main__':
  
    # Variables
    configfile = 'backpack.cfg'
 
    tables = inv.getTables(configfile)
    characters = inv.loadCharacters(tables)
    
    pprint(characters)
    
    for key in characters.keys():
        print("Filling Character " + key)
        characters[key] = inv.fillTestInventory(tables) # Achtung! FillTestInventory hat noch keine Rückgabe!!
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