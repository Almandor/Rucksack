#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
\file inventory_win.py
\package gui.window
\brief Some classes for GUI


\date (C) 2017
\author Christian Wunderlich
\email cw@almandor.de
\version 1.0
'''
from Tkinter import *
from tkFileDialog import *
from conf import logbox as log
from gui.window import *
from inventory import *

__author__ = "Christian Wunderlich"
__copyright__ = "(C) 2017 " + __author__
__email__ = "cw@almandor.de"
__version__ = "1.0"
__license__ = "GNU V3.0"
__me__ = "A RPG tool package for Python 2.7"

logger = log.createLogger('window', 'warning', '1 MB', 1, './')

class inventoryWindow(blankWindow):
    def __init__(self, tables, characters):
        blankWindow.__init__(self)
        self.window.title = 'Inventory'
        self.catDropDownBox(["Test1","Test2"])
        self.charDropDownBox(["Tom", "Tim","Tony"])
        self.itemListBox(["1","2","3"])
        self.inventoryListBox("")
        self.addButtons()
        self.window.mainloop()
        
        
    def catDropDownBox(self, categories):
        self.dropVar=StringVar()
        self.dropVar.set(categories[0])
        self.popupMenu = OptionMenu(self.window, 
                               self.dropVar, 
                               *categories, 
                               command=self.notdoneyet())
        self.popupMenu.grid(column = 0, row = 0, sticky = "nw")

        
    
    def charDropDownBox(self, characters):
        self.dropVar=StringVar()
        self.dropVar.set(characters[0])
        self.popupMenu = OptionMenu(self.window, 
                               self.dropVar, 
                               *characters, 
                               command=self.notdoneyet())
        
        self.popupMenu.grid(column = 2, row = 0, sticky = "nw")
    
    def itemListBox(self, items):
        self.listbox = Listbox(self.window)
        self.listbox.grid(column = 0, row = 1, sticky = "nw", rowspan = 3)
        
        for item in items:
                self.listbox.insert(END, item)
    
    def inventoryListBox(self, inventory):
        self.listbox = Listbox(self.window)
        self.listbox.grid(column = 2, row = 1, sticky = "nw", rowspan = 3)
        
        for item in inventory:
                self.listbox.insert(END, item)
    
    def addButtons(self):
        self.button1 = Button(self.window, text = " --> ", command = self.notdoneyet())
        self.button1.grid(column = 1, row = 2)
        
        self.button2 = Button(self.window, text = " <-- ", command = self.notdoneyet())
        self.button2.grid(column = 1, row = 3)
    
    def coinsText(self, coinSum):
        pass
    
    def totalText(self, totalSum):
        pass
        


mywindow = inventoryWindow()