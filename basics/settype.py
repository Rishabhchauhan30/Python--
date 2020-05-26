s={10,20,30,'RSC'}
print(s)
print(type(s))

#in set we can't add same type of elements
#it automatically ommit the duplicate values

s.update([4,99])
print(s)
print(type(s))

s.remove(10)
print(s)