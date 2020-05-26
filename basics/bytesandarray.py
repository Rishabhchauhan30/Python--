lst=[20,30,40,240]
print(type(lst))

#to convert this list into byte

b=bytes(lst)
print(b)
print(type(b))

#indexing slicing adding cant be done in bytes 

#to convert list into bytearray

b1=bytearray(lst)
print(b1)
print(type(b1))
b1[2]=33
