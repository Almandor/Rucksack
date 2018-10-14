import os
import ConfigParser


def readConfig(configfile = 'backpack.cfg'):
    '''
    
    Checking for Config File
    \param configfile Name of the config file.
    \retval dataDirectory Directory where the data files are located
        Returns ./data if no directory found in config file.
    
    '''
    if os.path.isfile(configfile):
        config = ConfigParser.ConfigParser()
        config.read(configfile)
        try:
            dataDirectory = config.get("global",'DataDirectory')
        except:
            print("DataDirectory not configured. Using defaults")
            dataDirectory = "../data"
    else:
        print("Config file not found. Using defaults")
        dataDirectory = "../data"

    return(dataDirectory)