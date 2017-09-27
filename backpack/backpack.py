from Tkinter import *
import ConfigParser
import os
import sys
import csv

configfile = 'backpack.cfg'

def readConfig(configfile):
    # Checking for Config File
    if os.path.isfile(configfile):
        config = ConfigParser.ConfigParser()
        config.read(configfile)
        try:
            dataDirectory = config.get("1",'DataDirectory')
        except:
            print("DataDirectory not configured. Using defaults")
            dataDirectory = "./Data"
    else:
        print("Config file not found. Using defaults")
        dataDirectory = "./Data"

    return(dataDirectory)

def listCategories(dataDirectory):
    category = []
    try:
        dirContents = os.listdir(dataDirectory)
    except:
        print("No Data found. Abort")
        sys.exit()
        
    if dirContents == []:
        print("Datadirectory is empty. Abort")
        sys.exit()
    else:
        for i in dirContents:
            if i.endswith(".csv"):
                category.append(i[:-4])
        
        return(category)

def getTables(configfile):
    dataDirectory = readConfig(configfile)
    categories = listCategories(dataDirectory)
    tables = []
    for i in categories:
        filename = dataDirectory + "/" + i + ".csv"
        with open(filename) as f:
            a = [{k: int(v) for k, v in row.items()}
                 for row in csv.DictReader(f, skipinitialspace=True)]
        tables.append(i,a)
    return(tables)





tables = getTables(configfile)
#===============================================================================
# root = Tk()
# 
# labelMain = Label(root, text="Get Inventory")
# labelMain.grid()
# 
# root.mainloop()
#===============================================================================