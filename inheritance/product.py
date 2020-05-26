class BMW:
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        
        
class Three_series(BMW):
    def __init__(self,cruisecontrol,make,model,year):
        BMW.__init__(self, make, model, year)
        self.cruisecontrol = cruisecontrol 
        
        

class Five_series(BMW):
    def __init__(self,parkingassist,make,model,year):
        BMW.__init__(self, make, model, year)
        self.parkingassist = parkingassist 
    
 
ts = Three_series(True,'BMW','320d',2018)
print(ts.cruisecontrol)
print(ts.make)
print(ts.model)
print(ts.year)



fs = Five_series(True,'BMW','520d',2019)
print(fs.parkingassist)
print(fs.make)
print(fs.model)
print(fs.year)
        
                