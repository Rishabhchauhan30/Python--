class Student:
    def __init__(self,id,name,testscore):
        self.id = id 
        self.name = name 
        self.testscore = testscore
        
    def display(self): 
        print(self.id)
        print(self.name) 
        print(self.testscore)  