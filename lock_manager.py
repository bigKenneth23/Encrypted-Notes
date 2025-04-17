from config import config_path
from json import load
from config import Fernet, exists

class NoteLock:
    def __init__(self, note_path):
        self.path = note_path

        if not exists(note_path):
            raise FileNotFoundError(f"{note_path} does not exist.") 
        
        self.LoadContent()

        self.FetchKey()


    def FetchKey(self):
        # Key should already be verified before this stage
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
        c = Fernet(self.key)
        new = c.encrypt(self.content.encode())
        with open(self.path, "wb") as f:
            f.write(new)


    def Unlock(self):
        c = Fernet(self.key)
        new = c.decrypt(self.content)
        with open(self.path, "wb") as f:
            f.write(new)

