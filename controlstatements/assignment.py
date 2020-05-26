x=int(input('Enter a number less then 100:'))
for i in range(0,x):
    i+=1
    if i % 10 == 0:
        continue
    assert i>100,'number should be less then 100'
    print(i)