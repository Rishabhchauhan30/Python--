#dict={key:value}

dict1={1:"john",2:"bob",3:"RSC"}
print(dict1)

#there are several methods in dictionary to used 

print(dict1.items())

#for keys
#to view keys only

k=dict1.keys()
for i in k:
    print(i)
    
#for values
#to view values only

v=dict1.values()
for i in v:
    print(i)
    
#we can use keys to find the value of that key
print(dict1[3]) 

del dict1[2]
print(dict1)
        

