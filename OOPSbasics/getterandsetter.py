class programmer:
    
    def setName(self,n):
        self.name = n 
    
    def getName(self):
        return self.name
    
    def setSalary(self,sal):
        self.salary = sal
       
    def getSalary(self):
        return self.salary 
    
    def setTechnologies(self,tech):
        self.technologies = tech   
           
    def getTechnologies(self):       
        return self.technologies  
    
o1 = programmer()

o1.setName('john')
o1.setSalary(500000)
o1.setTechnologies(['python','c++','java','java script'])

print(o1.getName())
print(o1.getSalary())
print(o1.getTechnologies())
                        