import config
from lock_manager import NoteLock
from note_manager import Notelist
from sys import argv

def init():
    global notes

    config_ok = config.Verify()

    if not config_ok:
        config.Repair()

    notes = Notelist()
    

def Main(argv: list[str]):
    argc = len(argv)
    if argc != 2:
        print("Invalid arg count.")
        return
    
    valid_args = ["lock", "unlock", "new_key"]

    try:
        cmd = argv[1].lower().strip()
        if cmd not in valid_args:
            raise Exception
    except:
        print("Invalid argument provided.")
        return
    
    init()
    
    match(cmd):
        case "lock":

            if config.files_locked:
                print("Files already locked.")
                return
        
            LockAll()
            print("All files locked.")
            config.SwitchLockState()
            return

        case "unlock":

            if not config.files_locked:
                print("Files already unlocked.")
                return
            
            UnlockAll()
            config.SwitchLockState()
            print("All files unlocked.")
            return
        
        case "new_key":
            RefreshKey()
            print("Files re-encrypted with new generated key.")
            return


def LockAll():
    paths = list(notes.notes.values())
    for path in paths:
        locker = NoteLock(path)
        locker.Lock()


def UnlockAll():
    paths = list(notes.notes.values())
    for path in paths:
        locker = NoteLock(path)
        locker.Unlock()


def RefreshKey():
    if config.files_locked:
        UnlockAll()

    config.Repair()
    LockAll()
    config.SwitchLockState()


if __name__ == "__main__":
    Main(argv)