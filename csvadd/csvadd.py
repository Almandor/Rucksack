#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import Tkinter as tk
import argparse
import time
import csv
import geometry

# --- classes ---

class Application(tk.Frame):

    def __init__(self, headers, filename, last_line, master=None):
        tk.Frame.__init__(self, master)
        center(self)
        self.grid()
        self.filename = filename
        lastentry = self.createWidgets(self.filename, headers, last_line)


    def createWidgets(self, filename, headers, last_line):

        self.lastentry = []
        self.entryfield = []

        self.label = tk.Label(self, text="CSV Entry Tool")
        self.label.grid(columnspan=3, pady=(0,10))

        for x, y in enumerate(headers):
            self.create_label_widget(x, y)
            columns = x

        for x, y in enumerate(last_line):
            self.lastentry.append(self.create_lastentry_widget(x, y))

        for x in range(len(last_line)):
            self.entryfield.append(self.create_entry_widget(x))

        self.lastlineLabel = tk.Label(self, text="Last Entry: ")
        self.lastlineLabel.grid(row=2, column=1, padx=(10,10), pady=(0,15))

        self.entryLabel = tk.Label(self, text="New Entry: ")
        self.entryLabel.grid(row=3, column=1, padx=(10,10), pady=(0,15))

        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.quitButton.grid(row=6, column=4)

        self.saveButton = tk.Button(self, text='+', command=lambda: writedata(filename, self.entryfield, self.lastentry))
        self.saveButton.grid(row=3, column=x+3, padx=(10,10), pady=(0,15))



        return self.lastentry


    def create_label_widget(self, x, y):
        new_widget = tk.Label(self, text=y)
        new_widget.grid(row=1, column=x+2, padx=(10,10), pady=(0,15))
        return new_widget

    def create_entry_widget(self, x):
        new_widget = tk.Entry(self)
        new_widget.grid(row=3, column=x+2, padx=(10,10), pady=(0,15))
        new_widget.bind("<Return>", lambda event: writedata(filename, self.entryfield, self.lastentry))

        return new_widget

    def create_lastentry_widget(self, x, y):
        new_widget = tk.Entry(self)
        new_widget.grid(row=2, column=x+2, padx=(10,10), pady=(0,15))
        new_widget.insert(1, y)
        new_widget.configure(state="readonly")
        return new_widget

# --- functions ---

def get_headers(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print row
            break
    return row

def file_len(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(filename)
        i = sum(1 for row in reader)

    with open(filename, 'r') as f:
        reader = csv.reader(filename)
        l = None
        for l in csv.reader(f): pass
    return i, l

def writedata(filename, entryfield, lastentry):
    print("Saving...")
    for i in range(len(entryfield)):
        print i
        lastentry[i].configure(state="normal")
        lastentry[i].delete(0,tk.END)
        lastentry[i].insert(1, entryfield[i].get())
        lastentry[i].configure(state="readonly")
        entryfield[i].delete(0,tk.END)
    with open(filename, 'a') as f:
        writer = csv.writer(f)
        outfiledata = []
        for i in range(len(lastentry)):
            outfiledata.append(lastentry[i].get())
        #outfiledata = outfiledata[2:]
        writer.writerow(outfiledata)
        
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


# --- main ---

parser = argparse.ArgumentParser()
parser.add_argument('filename', metavar='csv', nargs=1, help="file to parse")
args = parser.parse_args()

filename = args.filename[0]

headers = get_headers(filename)  # .decode('utf8')
print headers



# Check Filelengh and get back last line.
file_lengh, last_line = file_len(filename)
print("Eintrage: ".decode('utf8')) + str(file_lengh)
print last_line

app = Application(headers, filename, last_line)

app.master.title('Sample application')
app.mainloop()
