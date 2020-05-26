class patient:
    
    def setId(self,id):
        self.id = id 
    
    def getId(self):
        return self.id 
    
    def setName(self,name):
        self.name = name 
    
    def getName(self):
        return self.name 
    
    def setSsn(self,ssn):
        self.ssn = ssn 
         
    def getSsn(self):
        return self.ssn 
    

s = patient()

s.setId(123) 
s.setName('john')
s.setSsn(1122)

print(s.getId())
print(s.getName())
print(s.getSsn())           