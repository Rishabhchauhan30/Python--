import logging

logging.basicConfig(filename='mylog.log',level=logging.DEBUG)
try:
    f = open('myfile','w')
    a,b = [int(x) for x in input('enter two number:').split()]
    logging.info('divison in progress')
    c=a/b
    f.write('writning %d into file'%c) 
    print(c)
    
except ZeroDivisionError:
    print('division b zero is not allowed') 
    print('please enter new numbers')
    logging.error('division by zero')
    
else:
    print('you have entered a non zero number')    

finally:
    f.close()
    print('file closed')    
    
print('code after the exceptions')