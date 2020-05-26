from abc import abstractmethod

class Touch_Screen_Laptop:
    
    @abstractmethod 
    def scroll(self):
        pass 
    
    @abstractmethod 
    def touch(self):
        pass 
    
    
class HP(Touch_Screen_Laptop):
        
    def scroll(self):
        print('allows')
        
                


class DELL(Touch_Screen_Laptop):

        
    def scroll(self):
        print('allows')  
        
        
hp = HP()
print(hp.scroll())

dell = DELL()
print(dell.scroll())       
        
        
          