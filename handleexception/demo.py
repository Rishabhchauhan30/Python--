try:
    a,b = [int(x) for x in input('enter two number:').split()]
    c=a/b 
    print(c)

except ZeroDivisionError:
    print('division b zero is not allowed') 
    print('please enter new numbers')
    
print('code after the exceptions')      