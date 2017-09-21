#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
\file testinit.py
\brief Startfile fuer Shop

Startfile fuer den Aufruf des Shopsystems zu Testzwecken.
Enthält den einkaufenden Charakter

\date (C) 2017
\author Christian Wunderlich
\email cw@almandor.de

\todo Modul: Bau der Containerliste
\todo Modul: Uebergabe der Daten an shop.py
'''

import Tkinter as tk
from Tkconstants import BOTH, SINGLE
import ttk as ttk
from Tkinter import StringVar, IntVar

class Startwindow(object):
    '''
    Baut Fenster um den Shop zu starten.
    Test-Charakterdaten werden angezeigt und können angepasst werden.
    '''
    def __init__(self, master):    
        
        self.check1 = IntVar()               
                             
                             # Eingabefelder für Testdaten werden gebaut
        self.master = master
        self.frame_main = tk.Frame(self.master, height = 200, width = 600)
        self.frame_main.grid(row = 0, column = 0)
        
        self.label1 = tk.Label(self.frame_main, text = "Testtool um Shop zu testen", font = ("Helvetica", 16))
        self.label1.grid(row = 0, column = 0, padx = 10, sticky=tk.W)
        
        self.frameplaceholder = tk.Frame(self.frame_main, height = 50, width = 600,relief=tk.RIDGE)
        self.frameplaceholder.grid(row = 1, column = 0, columnspan = 4)
        
        self.labelname = tk.Label(self.frame_main, text = "Name: ")
        self.labelname.grid(row = 2,column = 0, sticky=tk.W, padx=(10,0))

        self.entryname = tk.Entry(self.frame_main, textvariable=name)
        self.entryname.config(width = 40)
        self.entryname.grid(row = 2, column = 1, padx=(0,10))
        
        self.labelgold = tk.Label(self.frame_main, text = "Gold: ")
        self.labelgold.grid(row = 3,column = 0, sticky=tk.W, padx=(10,0), pady=(5,0))

        self.entrygold = tk.Entry(self.frame_main, textvariable=gold)
        self.entrygold.config(width = 40)
        self.entrygold.grid(row = 3, column = 1, padx=(0,10), pady=(5,0))
        
        self.labelweight = tk.Label(self.frame_main, text = "Max Weight: ")
        self.labelweight.grid(row = 4,column = 0, sticky=tk.W, padx=(10,0), pady=(5,0))

        self.entryweight = tk.Entry(self.frame_main, textvariable=maxweight)
        self.entryweight.config(width = 40)
        self.entryweight.grid(row = 4, column = 1, padx=(0,10), pady=(5,0))
        
        self.labelcontainer = tk.Label(self.frame_main, text = "Prefilled Container: ")
        self.labelcontainer.grid(row = 5,column = 0, sticky=tk.W, padx=(10,0), pady=(5,0))

        self.checkcontainer = ttk.Checkbutton(self.frame_main, variable = self.check1)
        self.checkcontainer.grid(row = 5, column = 1, padx=(0,10), pady=(5,0), sticky=tk.W)

        self.button_start = tk.Button(self.frame_main, text = "Start", command = lambda: self.begin(self.entryname.get(), self.entrygold.get(),self.entryweight.get(),self.check1.get()), height = 3, width = 30, foreground='green')
        self.button_start.grid(row = 6, column = 0, pady = 10)   

        self.button_quit = tk.Button(self.frame_main, text = "Beenden", command = master.destroy, height = 3, width = 30, foreground='red')
        self.button_quit.grid(row = 6, column = 1, pady = 10)
        
        self.prefill(self.entryname, self.entrygold,self.entryweight,self.check1)
        
    def prefill(self,name,gold,weight,container):  # Füllt die Eingabefelder mit Defaultdaten
        name.insert(0, "Max Tester")
        gold.insert(0, 100000)
        weight.insert(0, 120)
           
    
    def begin(self,name,gold,weight,check):
        if check == True:
            container = []
        else:
            container = []

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


if __name__ == '__main__':
    name = ""
    gold = "0"
    maxweight = ""
    container = []
    contvar = StringVar
    main()