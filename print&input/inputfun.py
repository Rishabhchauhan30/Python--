''''s=input()
print(s)
s=input('Enter your name-')
print(s)
i=int(input("Enter a integer number-"))
print(i)
print(type(i))

lst=[int(x) for x in input('Enter three numbers seperated by space-').split()]
print(lst)'''

lst=[int(x) for x in input('Enter three numbers seperated by comma-').split(',')]
print(lst)