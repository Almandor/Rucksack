# -*- coding: UTF-8 -*-

import Tkinter as tk
import os.path
import time

class Mainscreen(object):
    def __init__(self, master):
        self.master = master
        self.frame_main = tk.Frame(self.master, height = 200, width = 600)
        self.frame_main.grid(row = 0, column = 0)
        self.label1 = tk.Label(self.frame_main, text = "Rucksack und Inventar Management", font = ("Helvetica", 16))
        self.label1.grid(row = 0, column = 0, padx = 10)

        self.button_new = tk.Button(self.frame_main, text = "Neue Gruppe anlegen", command = self.__create_new_group, height = 3, width = 30)
        self.button_new.grid(row = 1, column = 0, pady = 10)
        
        self.button_load = tk.Button(self.frame_main, text = "Vorhandene Gruppe laden", command = self.__load_group, height = 3, width = 30)
        self.button_load.grid(row = 2, column = 0, pady = 10)
        
        self.button_continue = tk.Button(self.frame_main, text = "Vorherige Gruppe fortführen", command = self.__continue_last_group, height = 3, width = 30)
        self.button_continue.grid(row = 3, column = 0, pady = (10, 30))

        self.button_quit = tk.Button(self.frame_main, text = "Beenden", command = master.destroy, height = 3, width = 30)
        self.button_quit.grid(row = 5, column = 0, pady = 10)
        
    def __create_new_group(self):
        # WIP
        print("WIP! New")
        self.master.destroy()
        root = tk.Tk()
        app = New_Group(root)
        center(root)
        root.mainloop()

    def __load_group(self):
        # WIP
        print("WIP! Load")

#
    def __continue_last_group(self):
        # WIP
        print("WIP!")


class New_Group(object):
        def __init__(self, master):
            self.master = master
            self.frame_main = tk.Frame(self.master, height = 600, width = 800)
            self.frame_main.grid(row = 0, column = 0)
            self.label1 = tk.Label(self.frame_main, text = "Rucksack und Inventar Management", font = ("Helvetica", 16))
            self.label1.grid(row = 0, column = 0, padx = 10, columnspan = 4)
            self.label_name = tk.Label(self.frame_main, text = "Name", font = ("Times", 8))
            self.label_name.grid(row = 1, column = 0, pady = (10, 2))
            self.entry_name = tk.Entry(self.frame_main)
            self.entry_name.grid(row = 2, column = 0, padx = (10, 0))
            self.label_weight = tk.Label(self.frame_main, text = "MaxGewicht", font = ("Times", 8))
            self.label_weight.grid(row = 1, column = 1, pady = (10, 2))
            self.entry_weight = tk.Entry(self.frame_main)
            self.entry_weight.grid(row = 2, column = 1, padx = 0)
            self.label_gold = tk.Label(self.frame_main, text = "Gold", font = ("Times", 8))
            self.label_gold.grid(row = 1, column = 2, pady = (10, 2))
            self.entry_gold = tk.Entry(self.frame_main)
            self.entry_gold.grid(row = 2, column = 2, padx = 0)
            self.label_player = tk.Label(self.frame_main, text = "Spielername", font = ("Times", 8))
            self.label_player.grid(row = 1, column = 3, pady = (10, 2))
            self.entry_player = tk.Entry(self.frame_main)
            self.entry_player.grid(row = 2, column = 3, padx = (0, 10))
            self.button_entry = tk.Button(self.frame_main, text = "+", command = self.__add_data)
            self.button_entry.grid(row = 2, column = 4, padx = 10)
            
        def __add_data(self):
            print("WIP")




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
    app = Mainscreen(root)
    center(root)
    root.mainloop()


if __name__ == '__main__':
    main()
