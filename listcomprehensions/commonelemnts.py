a=[2,3,4,5,6,7,8]
b=[2,4,6,8]

z=[]
'''for i in a:
    if i in b:
        z.append(i)'''


z=[i for i in a if i in b]        
print(z)