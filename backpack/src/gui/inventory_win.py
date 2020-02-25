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
from tkinter import *
from tkinter.filedialog import *
import inventory_config.logbox as log
from gui.window import *
import inventory_backend.inventory as inv
from pprint import pprint
import tkinter.ttk
import inspect
import os
# from PIL import ImageTk, Image


# from zim.plugins.distractionfree import _minsize

__author__ = "Christian Wunderlich"
__copyright__ = "(C) 2017 " + __author__
__email__ = "cw@almandor.de"
__version__ = "1.0"
__license__ = "GNU V3.0"
__me__ = "A RPG tool package for Python 2.7"

logger = log.createLogger('window', 'debug', '1 MB', 1, logpath = './', logfile = 'inventory_win.log')



class inventoryWindow(blankWindow):


    def __init__(self, tables):
        '''
        Hauptfenster um das Inventar der Charaktere aus einem Shop zu befüllen.
        \param tables Dictionary welches Liste von Dictionaries enthält.
        \param characters ???

        '''
        self.inventory = inv.inventoryHandler()
        self.tables = tables
        ## \var self.container
        # Nimmt die Container des Shops und des Inventorys auf.
        self.container = {}
        ## \var self.tree_display
        # Nimmt die Fenster Items auf
        self.tree_display = {}
        ## \var self.vsb
        # Nimmt die Vertikalen Scrollbalken auf
        self.vsb = {}
        ## \var self.hsb
        # Nimmt die Horizontalen Scrollbalken auf
        self.hsb = {}
        blankWindow.__init__(self)
        self.window.title('Inventory')
        self.catDropDownBox(list(tables.keys()), tables)
        self.tables = tables
        self.tree_columns = {}
        for key in list(tables.keys()):           # key: 001_Weapons, 001_Weapons
            self.tree_columns[key] = list(tables[key][0].keys())
        self.selection = list(tables.keys())[0]
        self.tree_data = ""
        self.tree_box("Shop", 0, 1)
        self._build_tree_shop()
        self.tree_box("Inventory", 2, 1)
        self.switchToGrid("001_Weapons")
        self._build_tree_char()
        self.addButtons()
        self.window.columnconfigure(0, minsize = 400)
        self.window.columnconfigure(2, minsize = 400)
        self.tables = tables
        for key in self.tree_columns:
            self.tree_display["Inventory"][key].bind("<Double-1>", self.delete_from_inventory)
            self.tree_display["Shop"][key].bind("<Double-1>", self.transfer_right)

        self.addMenu()

        self.window.mainloop()


    def switchToGrid(self, target):
        '''
        Funktion zum Ein- und Ausblenden der Container
        \param target Gewünschte Kategorie
        '''
        for key in list(self.tables.keys()):
            for entry in list(self.tree_display.keys()):
                try:
                    self.container[entry][key].grid_remove()
                except:
                    pass

        self.container["Shop"][target].grid(column=0, row=1, sticky="nw", rowspan=3)
        self.container["Inventory"][target].grid(column=2, row=1, sticky="nw", rowspan=3)


    def wrapperTableHeaders(self, selection):
        '''
        Description ???
        \param selection ???
        '''
        self.selection = selection
        self.switchToGrid(self.selection)


    def catDropDownBox(self, categories, tables):
        '''
        Zeigt die Shopkategorien in einer Drop-Down-Box an.
        \param categories ???
        \param tables ???
        '''

        self.dropVar = StringVar()
        self.dropVar.set(categories[0])
        self.popupMenu = OptionMenu(self.window,
                               self.dropVar,
                               *categories,
                               command = self.wrapperTableHeaders)  #inv.getTableHeaders(tables,str(self.dropVar)))
        self.popupMenu.grid(column = 0, row = 0, sticky = "nw")


    def charDropDownBox(self, characters):
        '''
        Zeigt die Charaktere in einer Drop-Down-Box an.
        \param characters ???
        '''

        self.dropVar = StringVar()
        self.dropVar.set(characters[0])
        self.popupMenu = OptionMenu(self.window,
                               self.dropVar,
                               *characters,
                               command = self.notdoneyet())

        self.popupMenu.grid(column = 2, row = 0, sticky = "nw")


    def sortby(self, tree, col, descending):
        """Sort tree contents when a column is clicked on."""
        # grab values to sort
        data = [(tree.set(child, col), child) for child in tree.get_children('')]

        # reorder data
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)

        # switch the heading so that it will sort in the opposite direction
        tree.heading(col,
                     command=lambda col=col: self.sortby(tree, col, int(not descending)))




    def tree_box(self, tabelle, grow, gcolumn):
        '''
        Hilfsfunktion zum generieren der Tabellen
        \param grow grid row parameter
        \param gcolumn grid column parameter
        \param tabelle Type sting Shop oder Inentory
        :return:
        '''
        self.container[tabelle] = {}
        self.tree_display[tabelle] = {}
        self.vsb[tabelle] = {}
        self.hsb[tabelle] = {}
        for key in self.tree_columns:
            self.container[tabelle][key] = tkinter.ttk.Frame()
            self.tree_display[tabelle][key] = tkinter.ttk.Treeview(columns=self.tree_columns[key], show="headings")
            self.vsb[tabelle][key] = tkinter.ttk.Scrollbar(orient="vertical", command=self.tree_display[tabelle][key].yview)
            self.hsb[tabelle][key] = tkinter.ttk.Scrollbar(orient="horizontal", command=self.tree_display[tabelle][key].xview)
            self.tree_display[tabelle][key].configure(yscrollcommand=self.vsb[tabelle][key].set, xscrollcommand=self.hsb[tabelle][self.selection].set)
            self.tree_display[tabelle][key].grid(column=0, row=0, sticky='nsew', in_=self.container[tabelle][key])
            self.vsb[tabelle][key].grid(column=1, row=0, sticky='ns', in_=self.container[tabelle][key])
            self.hsb[tabelle][key].grid(column=0, row=1, sticky='ew', in_=self.container[tabelle][key])
            self.container[tabelle][key].grid_columnconfigure(0, weight=1)
            self.container[tabelle][key].grid_rowconfigure(0, weight=1)


    def _build_tree_shop(self):
        '''
        Fills the shop with merchandise.
        \bug Sorting does not work properly yet.
        '''



        # \todo Schleife anlegen welche die Werte nach kategorie in die Tabellen füllt.


        for category in list(self.tables.keys()):

            for col in self.tree_columns[category]:
                self.tree_display["Shop"][category].heading(col, text = col.title(),
                                  command = lambda c = col: self.sortby(self.tree_display["Shop"][category], c, 0))
                self.tree_display["Shop"][category].column(col, width = 60)

            for values in self.tables[category]:
                self.tree_display["Shop"][category].insert('', 'end', values = list(values.values()))




    def _build_tree_char(self):
        '''
        Funktion um Das Inventoryfenster vorzubereiten
        '''

        for category in list(self.tables.keys()):

            for col in self.tree_columns[category]:
                self.tree_display["Inventory"][category].heading(col, text = col.title(),
                                  command = lambda c = col: self.sortby(self.tree_display["Inventory"][category], c, 0))
                self.tree_display["Inventory"][category].column(col, width = 60)


    def transfer_right(self, blubb = ""):
        '''
        Adds the item which is selected in the shop window to the character inventory
        \param blubb Dummywert, ungenutzt. Nötig für den Aufrufenden Bind
        :return:
        '''
        self.tree_display["Inventory"][self.selection].insert('', 'end', values = self.tree_display["Shop"][self.selection].item(self.tree_display["Shop"][self.selection].selection())["values"])
        self.inventory.add(self.tree_display["Shop"][self.selection].item(self.tree_display["Shop"][self.selection].selection())["values"], self.selection)


    def delete_from_inventory(self, blubb = ""):
        '''
        Deletes selected item from character window
        \param blubb Dummywert, ungenutzt. Nötig für den Aufrufenden Bind
        :return:
        '''
        self.inventory.remove(self.tree_display["Inventory"][self.selection].item(self.tree_display["Inventory"][self.selection].selection())["values"], self.selection)
        self.tree_display["Inventory"][self.selection].delete(self.tree_display["Inventory"][self.selection].selection())





    def addButtons(self):
        '''
        Anlage der Buttons um Gegenstände zu und vom Inventar zu bewegen.
        '''

        self.button1 = Button(self.window, text = " --> ", command = self.transfer_right)
        self.button1.grid(column = 1, row = 2)

        self.button2 = Button(self.window, text = " <-- ", command = self.delete_from_inventory)
        self.button2.grid(column = 1, row = 3)

        self.buttonLoad = Button(self.window, text = "Load", command = self.load_inventory_from_save)
        self.buttonLoad.grid(column = 0, row = 5, rowspan = 3, sticky = "news")

        self.buttonSave = Button(self.window, text = "Save", command = self.send_inventory_to_save)
        self.buttonSave.grid(column = 2, row = 5, rowspan = 3, sticky = "news")


    def coinsText(self, coinSum):
        '''
        Funktion um Geld des Charakters anzuzeigen
        \param coinSum ???
        todo: all
        '''

        pass


    def totalText(self, totalSum):
        '''
        Funktion um das Gewicht anzuzeigen
        \param totalSum ???
        '''

        pass


    def addMenu(self):
        '''
        Funktion um das Menü anzuzeigen
        :return:
        '''

        self.filemenu = Menu(master = self.menu)
        self.menu.add_cascade(label = "File", menu = self.filemenu)
        self.filemenu.add_command(label="Save Inventory", command = self.send_inventory_to_save)

        self.menu.add_command(label = "Quit!", command = self.window.destroy)



    def load_inventory_from_save(self):
        '''
        Description ???
        '''
        self.inventory.load()

    def send_inventory_to_save(self):
        '''
        Sends inventory to Savefunktion inventory.save_inventory
        todo: alles
        '''
        self.inventory.save()

class popupEntry(blankWindow):

    def __init__(self, name):
        '''
        Popup zur Eingabe von Werten
        \param name ???
        '''

        blankWindow.__init__(self)

#        self.window.title = name
        self.window.title(name)
        self.addEntryfield()
        self.addButtons()
        self.window.mainloop()


    def addEntryfield(self):
        '''
        Description ???
        '''
        self.char = Frame(self.window)

        self.char_label = Label(self.char, text = "Charactername:")
        self.char_label.grid(row = 0, column = 0, sticky = "w", padx = (0, 10))
        self.charname = StringVar()
        self.char_entry = Entry(self.char, textvariable = self.charname)
        self.char_entry.grid(row = 0, column = 1, sticky = "w")
        self.char.grid(row = 1)


    def addButtons(self):
        '''
        Description ???
        '''

        self.plusbutton = Button(self.char, text="Add Char")
        self.plusbutton.grid(row=0, column=2)
