from threading import *

class MyThread:
    def displayNumbers(self):
        i = 0
        print(current_thread().getName())
        while(i<=10):
            print(i)
            i+=1
            
obj = MyThread()
t = Thread(target=obj.displayNumbers)
t.start()           