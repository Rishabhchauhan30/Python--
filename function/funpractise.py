'''def last_char(a):
    return a[-1]

print(last_char('rishabh'))


def odd_even(a):
    return a
    a=int(input('Enter a number: '))
    if a % 2==0:
        print(a,"number is even")
    else:
        print(a,'is odd')


def is_even(num):
    if num%2 == 0:
        return True
    else:
        return False
print(is_even(10))    

def is_even(num):
    return num%2 == 0
print(is_even(10))


def greater(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2
x=int(input("enter two numbers: "))
bigger = greater(x)

print(f'{bigger} is greater')'''




def greater(a,b):
    if a > b:
        return a
    else:
        return b 
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))
    bigger = greater(num1, num2)
    
    print(f"{bigger} is greater")
    

    