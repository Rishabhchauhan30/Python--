class Car:
    
    
    def __init__(self,name,year):
        self.name=name
        self.year=year
        
    class Engine:
        def __init__(self,uniquenumber):
            self.uniquenumber=uniquenumber
        def start(self):
            print('Engine started')    
            
o = Car('Jaguar',2018)
o1 = o.Engine(123)
o1.start()
            