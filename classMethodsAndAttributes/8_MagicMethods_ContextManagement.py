#context Mangement app

class TextFileManger:
    def __init__(self,filename,mode ="a"):
        self.filename=self.constructFilename(filename)
        self.mode =mode
        self.file =None
    
    @staticmethod
    def constructFilename(filename)->str:
        if not isinstance(filename,str):
            return "default.txt"
        return filename if filename.endswith(".txt")  else f"{filename}.txt"         
        
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self):
        if self.file:
            self.file.close()
            print("The file is closed")

with   TextFileManger("file") as file:
    file.write("Hello World")
            
    
