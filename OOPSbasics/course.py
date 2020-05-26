class course:
    def __init__(self,x,y):
        self.name=x 
        self.rating=y 
        
    def average(self):
        numberofrating=len(self.rating)
        average = sum(self.rating)/numberofrating
        print('Average rating for',self.name,'is',average)  
        
        
o1 = course('backend course',[1,2,3,4,5])

print(o1.name)
print(o1.rating)
o1.average()

o2 = course('frontend course',[5,5,5,5,5])  

print(o2.name)
print(o2.rating)      
o2.average()