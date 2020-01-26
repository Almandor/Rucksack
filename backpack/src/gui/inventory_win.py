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


    def __init__(self, tables, characters):
        '''
        Hauptfenster um das Inventar der Charaktere aus einem Shop zu befüllen.
        \param tables Dictionary welches Liste von Dictionaries enthält.
        \param characters ???

        '''
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
        self.catDropDownBox(tables.keys(), tables)
        self.charDropDownBox(characters.keys())
        self.tables = tables
        self.tree_columns = {}
        for key in tables.keys():           # key: 001_Weapons, 001_Weapons
            self.tree_columns[key] = tables[key][0].keys()
        # print("Debug: ")
        # print(self.tree_columns)
        # sys.exit()
        # self.tree_columns = tables[tables.keys()[0]][0].keys()
        self.selection = list(tables.keys())[0]
        self.tree_data = ""
        # self.tree_shop_box()
        self.tree_box("Shop", 0, 1)
        self._build_tree_shop()
        # self.tree_inventory_box()
        self.tree_box("Inventory", 2, 1)
        self.switchToGrid("001_Weapons")
        self._build_tree_char()
        self.addButtons()
        self.window.columnconfigure(0, minsize = 400)
        self.window.columnconfigure(2, minsize = 400)
        self.getTableHeaders = inv.getTableHeaders
        self.tables = tables
        self.characters = characters
        self.getTableHeaders(self.tables, self.tables.keys()[0])
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
        for key in self.tables.keys():
            for entry in self.tree_display.keys():
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
        self.getTableHeaders(self.tables, selection)
        self.selection = selection
        print(self.selection)
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


    def sortby(self, col, descending):
        """Sort tree contents when a column is clicked on."""
        # grab values to sort
        data = [(tree.set(child, col), child) for child in tree.get_children('')]

        # reorder data
        data.sort(reverse=descending)
        for indx, item in enumerate(data):
            tree.move(item[1], '', indx)

        # switch the heading so that it will sort in the opposite direction
        tree.heading(col,
                     command=lambda col=col: sortby(tree, col, int(not descending)))




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
            self.container[tabelle][key] = ttk.Frame()
            # self.container[tabelle][key].grid(column=gcolumn, row=grow, sticky="nw", rowspan=3)
            self.tree_display[tabelle][key] = ttk.Treeview(columns=self.tree_columns[key], show="headings")

            self.vsb[tabelle][key] = ttk.Scrollbar(orient="vertical", command=self.tree_display[tabelle][key].yview)
            self.hsb[tabelle][key] = ttk.Scrollbar(orient="horizontal", command=self.tree_display[tabelle][key].xview)
            self.tree_display[tabelle][key].configure(yscrollcommand=self.vsb[tabelle][key].set, xscrollcommand=self.hsb[tabelle][self.selection].set)
            self.tree_display[tabelle][key].grid(column=0, row=0, sticky='nsew', in_=self.container[tabelle][key])
            self.vsb[tabelle][key].grid(column=1, row=0, sticky='ns', in_=self.container[tabelle][key])
            self.hsb[tabelle][key].grid(column=0, row=1, sticky='ew', in_=self.container[tabelle][key])
            self.container[tabelle][key].grid_columnconfigure(0, weight=1)
            self.container[tabelle][key].grid_rowconfigure(0, weight=1)


    def _build_tree_shop(self):
        '''
        Funktion um die Trees zu sortieren
        '''

        # for col in self.tree_columns[self.selection]:
        #     self.tree_shop[self.selection].heading(col, text = col.title(),
        #                       command = lambda c = col: sortby(self.tree_shop[self.selection], c, 0))
        #     self.tree_shop[self.selection].column(col, width = 60)
        #
        # for i in range(0, len(self.tables[self.tables.keys()[0]])):
        #     self.tree_shop[self.selection].insert('', 'end', values = self.tables[self.tables.keys()[0]][i].values())

        for col in self.tree_columns[self.selection]:
            self.tree_display["Shop"][self.selection].heading(col, text = col.title(),
                              command = lambda c = col: sortby(self.tree_display["Shop"][self.selection], c, 0))
            self.tree_display["Shop"][self.selection].column(col, width = 60)

        for i in range(0, len(self.tables[self.tables.keys()[0]])):
            self.tree_display["Shop"][self.selection].insert('', 'end', values = self.tables[self.tables.keys()[0]][i].values())




    def _build_tree_char(self):
        '''
        Funktion um die Trees zu sortieren
        '''

        # for col in self.tree_columns[self.selection]:
        #     print(self.tree_columns[self.selection])
        #     self.tree_char.heading(col, text = col.title(),
        #                            command = lambda c = col: sortby(self.tree_char, c, 0))
        #     self.tree_char.column(col, width = 60)

        for col in self.tree_columns[self.selection]:
            self.tree_display["Inventory"][self.selection].heading(col, text = col.title(),
                                   command = lambda c = col: sortby(self.tree_char, c, 0))
            self.tree_display["Inventory"][self.selection].column(col, width = 60)


    def transfer_right(self, blubb = ""):
        '''
        Adds the item which is selected in the shop window to the character inventory
        \param blubb ???
        :return:
        '''
        print("DEBUG: transfer_right")
        self.tree_display["Inventory"][self.selection].insert('', 'end', values = self.tree_display["Shop"][self.selection].item(self.tree_display["Shop"][self.selection].selection())["values"])


    def delete_from_inventory(self, blubb = ""):
        '''
        Deletes selected item from character window
        \param blubb ???
        :return:
        '''
        print("DEBUG: delete_from_inventory")
        self.tree_display["Inventory"][self.selection].delete(self.tree_display["Inventory"][self.selection].selection())



    def addButtons(self):
        '''
        Anlage der Buttons um Gegenstände zu und vom Inventar zu bewegen.
        '''

        self.button1 = Button(self.window, text = " --> ", command = self.transfer_right)
        self.button1.grid(column = 1, row = 2)

        self.button2 = Button(self.window, text = " <-- ", command = self.delete_from_inventory)
        self.button2.grid(column = 1, row = 3)


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


        self.charmenu = Menu(master = self.menu)
        self.menu.add_cascade(label = "Characters",
                              menu = self.charmenu)
        self.charmenu.add_command(label = "create new character",
                                  command = self.__newChar)
        self.charmenu.add_command(label="delete character",
                                  command=self.__delChar)
        self.filemenu = Menu(master = self.menu)
        self.menu.add_cascade(label = "File", menu = self.filemenu)
        self.filemenu.add_command(label = "Load Character", command = self.__loadChar)
        self.filemenu.add_command(label="Save Character", command = self.__saveChar)

        self.menu.add_command(label = "Quit!", command = self.window.destroy)


    def dummy(self):
        pass


    def __newChar(self):
        '''
        Description ???
        '''
        popupEntry("Enter Charaktername")

    def __delChar(self):
        '''
        Description ???
        '''
        pass

    def __loadChar(self):
        '''
        Description ???
        '''
        pass

    def __saveChar(self):
        '''
        Schreibt Charaktere in Datei
        todo: alles
        '''
        for child in self.tree_char.get_children():
            print(self.tree_char.item(child)["values"])  # Todo: Got the items, now I need to save them

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
