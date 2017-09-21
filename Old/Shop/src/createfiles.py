#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
\file cratefiles.py
\brief Eingabehilfe für die Equipmentfiles

Eingabehilfe für das Equipment. Eingabe der Kategorie erzeugt einen File für die Kategorie und erlaubt von da aus das Eingeben in die JSON Struktur

\date (C) 2017
\author Christian Wunderlich
\email cw@almandor.de

\todo Modul: Alles


'''

import Tkinter as tk
import json
import ttk as ttk
from Tkinter import StringVar, IntVar
import os

gegenstandsTypen = ['Weapons','Armor','Herbs', 'Poisons', 'Accessory', 'Transports','Misc']

class Mainwindow(object):
    '''
    '''

    def __init__(self, master):
        self.master = master
        self.frame_main = tk.Frame(self.master, height = 400, width = 800)
        self.frame_main.grid(row = 0, column = 0)
       
        self.labelHeader = tk.Label(self.frame_main, text = "Eingabe der Equipments", font = ("Helvetica", 16))
        self.labelHeader.grid(row = 0, column = 0, padx = 10, sticky=tk.W)
        
        self.frameplaceholder = tk.Frame(self.frame_main, height = 50, width = 800,relief=tk.RIDGE)
        self.frameplaceholder.grid(row = 1, column = 0, columnspan = 4)
        
        self.labelType = tk.Label(self.frame_main, text= "Equipmenttype: ")
        self.labelType.grid(row = 2, column = 0, sticky=tk.W)
        
        

def center(toplevel):           # Zentriert übergebenes Fenster
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w / 2 - size[0] / 2
    if w >= 2000:
        x = x / 2
    y = h / 2 - size[1] / 2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def main():
    root = tk.Tk()
    app = Mainwindow(root)
    center(root)
    root.mainloop()


if __name__ == '__main__':
    main()        