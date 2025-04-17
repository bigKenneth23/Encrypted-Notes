from os import walk

class Notelist:
    def __init__(self):
        self.notes = {}
        self.CollectNotes()

        if not self.notes:
            raise TypeError()
        

    def CollectNotes(self):
        for rt, dir, fl in walk("Notes/"):
            for file in fl:
                try:
                    ext = file.strip()[-4:]

                    if ext != ".txt":
                        print(f"{ext} is not a valid note format, expected .txt.")
                        return
                    
                    name = file[:-4]
                except:
                    print(f"Invalid file format found: {file}")
                    self.notes = None
                    return
                
                this_path = f"{rt}{file}"
                self.notes[name] = this_path


