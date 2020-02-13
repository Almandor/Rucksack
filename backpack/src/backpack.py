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

from tkinter import *
import sys
import os
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURR_DIR)
sys.path.append(CURR_DIR + "\inventory_backend")
sys.path.append(CURR_DIR + "\inventory_config")
sys.path.append(CURR_DIR + "\gui")
print(CURR_DIR)
from inventory_backend import inventory as inv
from pprint import pprint
from inventory_config import logbox as log
from gui import window
from gui import inventory_win


if __name__ == '__main__':
  
    # Variables
    configfile = 'backpack.cfg'
 
    tables = inv.getTables(configfile)
    mywindow = inventory_win.inventoryWindow(tables)

