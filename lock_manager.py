from config import config_path
from json import load
from config import Fernet, exists

class NoteLock:
    def __init__(self, note_path):
        self.path = note_path

        #should not happen, more an indication the code has been changed and broken.
        if not exists(note_path):
            raise FileNotFoundError(f"{note_path} does not exist.") 
        
        self.LoadContent()

        self.FetchKey()


    def FetchKey(self):
        # Key should already be verified before this stage, any errors here are practically impossible.
        with open(config_path, "r") as f:
            data = load(f)
            key = data["key"]
            self.key = key
                    
    
    def LoadContent(self):
        with open(self.path, "r") as f:
            self.content = f.read()
            if not self.content:
                raise ValueError(f"File {self.path} is empty.")
            
    
    def Lock(self):
        #i think some forms of text may break this though im not sure how. more testing needed
        c = Fernet(self.key)
        new = c.encrypt(self.content.encode())
        with open(self.path, "wb") as f:
            f.write(new)


    def Unlock(self):
        try:
            c = Fernet(self.key)
            new = c.decrypt(self.content.encode())
            with open(self.path, "wb") as f:
                f.write(new)
        except: # Files created while encryption is active cause errors as they are already decrypted, ignore them and move on is the safest approach here.
            pass

