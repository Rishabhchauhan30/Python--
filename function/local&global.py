'''x=123

def display():
    y=456
    print(y)
    
print(x)  
display()  

x=123

def display():
    x=678
    print(x)
    print(globals()['x'])

print(x)
display()'''  

x=123

def display():
    x=456
    print(x)
    print(globals()['x'])
    
print(x)     
z=display 
z()
z()
z()   



