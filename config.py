from os.path import exists
import json
from cryptography.fernet import Fernet

config_path = "config.json"

def Verify():
    if exists(config_path):

        with open(config_path, "r") as f:
            try:
                data = json.load(f)
            except:
                return False

            try:
                k = data["key"]

                if len(k) < 32:
                    return False
                
                l = data["locked"]
                if type(l) != bool:
                    return False
                
                global files_locked
                
                files_locked = l
                
                return True
            
            except:
                return False
            
    return False


def Repair():
    k = Fernet.generate_key().decode()
    _def = {
        "key": k,
        "locked": False
    }

    with open(config_path, "w") as f:
        json.dump(_def, f)


def SwitchLockState():
    with open(config_path, "r") as f:
        data = json.load(f)

    # Improvement credit - Masco
    data["locked"] = not data["locked"]
    
    with open(config_path, "w") as f:
        json.dump(data, f)