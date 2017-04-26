#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
\file fillshop.py
\brief Eingabefenster um den Shop mit Gegenständen zu füllen


\date (C) 2017
\author Christian Wunderlich
\email cw@almandor.de

\todo Modul: Auslesen der Config-Datei Shop.cfg
\todo Modul: Fensteraufbau
\todo Modul: Funktion
'''

import Tkinter as tk
from Tkconstants import BOTH, SINGLE
import ttk as ttk
from Tkinter import StringVar, IntVar
import json
import sys
import os

class Startwindow(object):
    pass

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
    app = Startwindow(root)
    center(root)
    root.mainloop()
    
def loadConfig():
    try:
        with open('../data/shop.cfg') as data_file:
            data = json.load(data_file)
    except:
        print("Config nicht vorhanden oder nicht lesbar")
        cwd = os.getcwd()
        print("Aktuelles Verzeichnis ist: " + cwd)
        print(os.path.isfile('../data/shop.cfg'))
        sys.exit(1)
        
    print(data)
    sys.exit(0)
    
if __name__ == '__main__':
    loadConfig()
    main()