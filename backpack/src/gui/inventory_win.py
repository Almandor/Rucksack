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
from inventory_config import logbox as log
from gui.window import *
from inventory_backend import inventory as inv
from pprint import pprint
import ttk

# from zim.plugins.distractionfree import _minsize

__author__ = "Christian Wunderlich"
__copyright__ = "(C) 2017 " + __author__
__email__ = "cw@almandor.de"
__version__ = "1.0"
__license__ = "GNU V3.0"
__me__ = "A RPG tool package for Python 2.7"

logger = log.createLogger('window', 'warning', '1 MB', 1, './')

class inventoryWindow(blankWindow):

    def __init__(self, tables, characters):
        '''
        Hauptfenster um das Inventar der Charaktere aus einem Shop zu befüllen.

        '''

        blankWindow.__init__(self)
        self.window.title = 'Inventory'
        self.catDropDownBox(tables.keys(), tables)
        self.charDropDownBox(characters.keys())
        print(tables.keys())
        self.tables = tables
        self.tree_columns = tables[tables.keys()[0]][0].keys()
        self.tree_data = ""
        self.tree_shop_box()
        self._build_tree()
        self.tree_inventory_boy()
        self.addButtons()
        self.window.columnconfigure(0, minsize=400)
        self.window.columnconfigure(2, minsize=400)
        self.getTableHeaders = inv.getTableHeaders
        self.tables = tables
        self.characters = characters
        self.getTableHeaders(self.tables, self.tables.keys()[0])

        self.window.mainloop()

    def wrapperTableHeaders(self, selection):
        self.getTableHeaders(self.tables, selection)
        
        
    def catDropDownBox(self, categories,tables):
        '''
        Zeigt die Shopkategorien in einer Drop-Down-Box an.
        '''

        self.dropVar=StringVar()
        self.dropVar.set(categories[0])
        self.popupMenu = OptionMenu(self.window, 
                               self.dropVar, 
                               *categories, 
                               command=self.wrapperTableHeaders)  #inv.getTableHeaders(tables,str(self.dropVar)))
        self.popupMenu.grid(column = 0, row = 0, sticky = "nw")

        
    
    def charDropDownBox(self, characters):
        '''
        Zeigt die Charaktere in einer Drop-Down-Box an.
        '''

        self.dropVar=StringVar()
        self.dropVar.set(characters[0])
        self.popupMenu = OptionMenu(self.window, 
                               self.dropVar, 
                               *characters, 
                               command=self.notdoneyet())
        
        self.popupMenu.grid(column = 2, row = 0, sticky = "nw")


    def tree_shop_box(self):
        '''
        Box um die Ausrüstung des Shops anzuzeigen.
        '''

        container1 = ttk.Frame()
        container1.grid(column = 0, row = 1, sticky = "nw", rowspan = 3)
        self.tree = ttk.Treeview(columns=self.tree_columns, show="headings")
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container1)
        vsb.grid(column=1, row=0, sticky='ns', in_=container1)
        hsb.grid(column=0, row=1, sticky='ew', in_=container1)
        container1.grid_columnconfigure(0, weight=1)
        container1.grid_rowconfigure(0, weight=1)


    def tree_inventory_box(self):
        '''
        Box um das Inventar des aktuellen Charakters anzuzeigen.
        todo: all
        '''
        pass

    def _build_tree(self):
        '''
        Funktion um die Trees zu sortieren
        '''
        for col in self.tree_columns:
            self.tree.heading(col, text=col.title(),
                              command=lambda c=col: sortby(self.tree, c, 0))
            self.tree.column(col, width=60)
        for i in range(0, len(self.tables[self.tables.keys()[0]])):
            self.tree.insert('', 'end', values=self.tables[self.tables.keys()[0]][i].values())



    def addButtons(self):
        '''
        Anlage der Buttons um Gegenstände zu und vom Inventar zu bewegen.
        '''

        self.button1 = Button(self.window, text = " --> ", command = self.notdoneyet())
        self.button1.grid(column = 1, row = 2)
        
        self.button2 = Button(self.window, text = " <-- ", command = self.notdoneyet())
        self.button2.grid(column = 1, row = 3)


    def coinsText(self, coinSum):
        '''
        Funktion um Geld des Charakters anzuzeigen
        todo: all
        '''

        pass


    def totalText(self, totalSum):
        '''
        Funktion um das Gewicht anzuzeigen
        '''

        pass
        
