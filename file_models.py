import pickle
import os
import jsonpickle

class FileService:
    def __init__(self,
                 filename):
        self.__filename = filename
        if not os.path.exists(filename):
            self.write([])
                
    def read(self):
        with open(self.__filename,"r") as f:
            return jsonpickle.decode(f.read())

    def write(self,data):
        with open(self.__filename,"w") as f:
            f.write(jsonpickle.encode(data))

class Db:
    def __init__(self,
                 filename):
        self.fileservice = FileService(filename)
        self.data = self.fileservice.read()
        
    def save(self):
        self.fileservice.write(self.data)

    def append(self,element):
        self.data.append(element)
        self.save()

    def pop(self,number):
        self.data.pop(number)
        self.save()

    def remove(self,element):
        self.data.remove(element)
        self.save()

    def clear(self):
        self.data.clear()
        self.save()

    def __len__(self):
        return len(self.data)
    
    def __getitem__(self,number):
        return self.data[number]
    
    def __str__(self):
        return f"{self.data}"

users = Db("users.txt")
