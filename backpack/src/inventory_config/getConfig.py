import os
import configparser


def readConfig(configfile = 'backpack.cfg'):
    '''
    
    Checking for Config File
    \param configfile Name of the config file.
    \retval config_dict Contains DataDirectory and SaveDirectory
    
    '''

    config_dict = {}

    if os.path.isfile(configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        try:
            config_dict["DataDirectory"] = config.get("global",'DataDirectory')
        except:
            print("DataDirectory not configured. Using defaults")
            config_dict["DataDirectory"] = "../data"

        try:
            config_dict["SaveDirectory"] = config.get("global", 'SaveDirectory')
        except:
            print("SaveDirectory not configured. Using defaults")
            config_dict["SaveDirectory"] = "../save"
    else:
        print("Config file not found. Using defaults")
        config_dict["DataDirectory"] = "../data"
        config_dict["SaveDirectory"] = "../save"

    return config_dict