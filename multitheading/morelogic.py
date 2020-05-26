from threading import *

class MyBus:
    
    def __init__(self,availableSeats):
        self.availableSeats = availableSeats
        
    def buy(self,seatsRequested):
        print('total seats available :',self.availableSeats)
        if(self.availableSeats>=seatsRequested):
            print('confirming the seat')
            print('processing the payment')
            print('printing tha ticket')
            self.availableSeats-= seatsRequested
        else:
            print('sorry...No seats available')    
        
obj = MyBus(10)
t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3= Thread(target=obj.buy,args=(3,))

t1.start()
t2.start()
t3.start()