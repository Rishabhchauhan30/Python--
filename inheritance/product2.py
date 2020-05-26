class BMW:
    
    def __init__(self,make,model,year):
        self.make = make
        self.model = model 
        self.year = year
        
    def powerwindow(self):
        print("powerwindow is there ") 
        
        
    def autostart(self):
        print("autostart and stop when leg is or remove from clutch ")    
        
        
class Three_series(BMW):
    def __init__(self,cruisecontrol,make,model,year):
        BMW.__init__(self, make, model, year)
        self.cruisecontrol = cruisecontrol 
        
    def display(self):
        print(self.cruisecontrol)    
        
        
    def powerwindow(self):
        print("powerwindow and sunroof is there ")    
        

class Five_series(BMW):
    def __init__(self,parkingassist,make,model,year):
        BMW.__init__(self, make, model, year)
        self.parkingassist = parkingassist 
    
 
ts = Three_series(True,'BMW','320d',2018)
print(ts.cruisecontrol)
print(ts.make)
print(ts.model)
print(ts.year)

ts.powerwindow()
ts.autostart()
ts.display()


fs = Five_series(True,'BMW','520d',2019)
print(fs.parkingassist)
print(fs.make)
print(fs.model)
print(fs.year)