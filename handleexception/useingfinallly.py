try:
    f = open('myfile','w')
    a,b = [int(x) for x in input('enter two number:').split()]
    c=a/b
    f.write('writning %d into file'%c) 
    print(c)
    
except ZeroDivisionError:
    print('division b zero is not allowed') 
    print('please enter new numbers')

finally:
    f.close()
    print('file closed')    
    
print('code after the exceptions')