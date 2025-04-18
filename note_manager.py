from os import walk

class Notelist:
    def __init__(self):
        self.notes = {}
        self.CollectNotes()

        if not self.notes:
            print("No notes have been created, please make a new note and try again.")
            exit()       


    def CollectNotes(self):
        for rt, dir, fl in walk("Notes/"):
            for file in fl:
                try:
                    n = len(file.strip())-1
                    ext_idx = None
                    
                    #iterate backwards for last '.'
                    while n > 0:
                        if file[n] == ".":
                            ext_idx = n
                        n -= 1

                    if not ext_idx:
                        raise NameError("Filename has no extension.")
                    
                    ext = file.strip()[ext_idx:]

                    valid_ext = [".txt", ".md", ".info", ".log", "m0"]

                    if ext not in valid_ext:
                        print(f"{ext} is not a valid note format.")
                        return
                    
                    name = file[:-4]
                #likely uneccessary to catch an exception here, but you never know
                except:
                    print(f"Invalid file format found: {file}")
                    self.notes = None
                    return
                
                this_path = f"{rt}{file}"
                self.notes[name] = this_path
