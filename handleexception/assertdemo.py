try:
    num = int(input('enter a even number'))
    assert num%2 == 0,'you have entered a odd number '
    
except AssertionError as object:
    print(object)

print('After the assertion')        