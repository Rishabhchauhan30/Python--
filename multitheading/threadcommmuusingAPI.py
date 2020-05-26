from threading import *;
from time import *;

class producer:
    
    def __init__(self):
        self.products = []
        self.c = Condition()
       
        
    def produce(self):
        for i in range(1,5):
            self.products.append('product'+str(i))
            sleep(1)
            print('item added')    
        
        self.c.notify()
        self.c.release()    
        
class consumer:
    
    def __init__(self,prod):
        self.prod = prod
        
    def consume(self):
        
        self.prod.c.acquire()
        self.prod.c.wait(timeout=0)
        self.prod.c.release()
       
        print('order shipped',self.prod.products)
        
p = producer()
c = consumer(p)

t1 = Thread(target = p.produce) 
t2 = Thread(target = c.consume)

t1.start() 
t2.start()
           
            
                            