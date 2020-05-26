class objectcounter:
    
    numberofobjects = 0
    
    def __init__(self):
        objectcounter.numberofobjects+=1
        
    @staticmethod    
    def displaycount():
        print(objectcounter.numberofobjects)
        
o1= objectcounter()
o2=objectcounter()
o3=objectcounter()

objectcounter.displaycount()