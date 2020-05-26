#without @decor
'''def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner 

def num():
    return 5

resultfun = decor(num)
print(resultfun())'''

#using @decor

def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner 

@decor 
def num():
    return 5
print(num())

