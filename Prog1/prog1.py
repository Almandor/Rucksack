from Tkinter import *
import ConfigParser
import os
import sys

configfile = 'prog1.cfg'

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
                category.append(i[3:-4])
        
        return(category)

    

listCategories(readConfig(configfile))
#===============================================================================
# root = Tk()
# 
# labelMain = Label(root, text="Get Inventory")
# labelMain.grid()
# 
# root.mainloop()
#===============================================================================