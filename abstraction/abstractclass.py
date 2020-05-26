from abc import abstractmethod, ABC
class BMW(ABC):
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        
        
    @abstractmethod
    def drive(self):
        pass 
       
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass 
        
        
        
class Three_series(BMW):
    def __init__(self,cruisecontrol,make,model,year):
        BMW.__init__(self, make, model, year)
        self.cruisecontrol = cruisecontrol 
        
    def start(self):
        super().start()
        print('starting warning')
        
    def stop(self):
        super().stop()
        print('stoping warning')        
        
        
    def drive(self):
        print('The series is being driven')   
        
        
         
        
        

class Five_series(BMW):
    def __init__(self,parkingassist,make,model,year):
        BMW.__init__(self, make, model, year)
        self.parkingassist = parkingassist 
        
        
     
    def start(self):
        super().start()
        print('start with remote')
        
    def stop(self):
        super().stop()
        print('stop with remote')     
        
        
        
    def drive(self):
        print('The series is being driven')    
    
 
ts = Three_series(True,'BMW','320d',2018)
print(ts.cruisecontrol)
print(ts.make)
print(ts.model)
print(ts.year)
print(ts.start())
print(ts.stop())

fs = Five_series(True,'BMW','520d',2019)
print(fs.parkingassist)
print(fs.make)
print(fs.model)
print(fs.year)
print(fs.start())
print(fs.stop())