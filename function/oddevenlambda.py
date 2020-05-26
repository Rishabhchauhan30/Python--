#using  function 
def odd_even(n):
    if n % 2 == 0:
        return True
    return False
print(odd_even(4))


#using lambda function 

f = lambda x: 'YES' if x%2==0 else 'NO'
print(f(10))
print(f(99))
