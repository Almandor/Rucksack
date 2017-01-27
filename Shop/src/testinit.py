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

\todo Modul: alles
'''

import Tkinter as tk
from Tkconstants import BOTH, SINGLE
import ttk as ttk

class Startwindow(object):
    '''
    Baut Fenster um den Shop zu starten.
    Test-Charakterdaten werden angezeigt und können angepasst werden.
    '''
    def __init__(self, master):
        self.master = master
        self.frame_main = tk.Frame(self.master, height = 200, width = 600)
        self.frame_main.grid(row = 0, column = 0)
        
        self.label1 = tk.Label(self.frame_main, text = "Testtool um Shop zu testen", font = ("Helvetica", 16))
        self.label1.grid(row = 0, column = 0, padx = 10)
        
        self.frameplaceholder = tk.Frame(self.frame_main, height = 50, width = 600)
        self.frameplaceholder.grid(row = 1, column = 0, columnspan = 4)
        
        self.labelname = tk.Label(self.frame_main, text = "Name: ")
        self.labelname.grid(row = 2,column = 0,padx = (0,10)) # Falsche Spalte


#         self.button_new = tk.Button(self.frame_main, text = "Neue Gruppe anlegen", command = self.__create_new_group, height = 3, width = 30)
#         self.button_new.grid(row = 1, column = 0, pady = 10)
#         
#         self.button_load = tk.Button(self.frame_main, text = "Vorhandene Gruppe laden", command = self.__load_group, height = 3, width = 30)
#         self.button_load.grid(row = 2, column = 0, pady = 10)
#         
#         self.button_continue = tk.Button(self.frame_main, text = "Vorherige Gruppe fortführen", command = self.__continue_last_group, height = 3, width = 30)
#         self.button_continue.grid(row = 3, column = 0, pady = (10, 30))
# 
#         self.button_quit = tk.Button(self.frame_main, text = "Beenden", command = master.destroy, height = 3, width = 30)
#         self.button_quit.grid(row = 5, column = 0, pady = 10)   
    

def center(toplevel):
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
    main()