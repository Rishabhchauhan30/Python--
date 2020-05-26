lst=[]
print(lst)

lst=[10,20,30,"rashu",-15,20.305]
print(lst)
print(lst[3])
print(lst[4:6])
print(lst*3)
print(len(lst))

lst.append(80)
print(lst)

lst.append(80)
lst.remove('rashu')
del(lst[1])
print(lst)

print(max(lst))
print(min(lst))

lst.insert(3,100)
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)



