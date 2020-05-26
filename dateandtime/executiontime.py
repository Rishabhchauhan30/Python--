from datetime import date
import time 

startTime = time.perf_counter()

ldates=[]
 
d1 = date(1999,10,20)
d2 = date(1999,3,30)
d3 = date(2017,4,4)

ldates.append(d1) 
ldates.append(d2) 
ldates.append(d3) 

ldates.sort()

#time.sleep(3)

for d in ldates:
    print(d)
    
endTime = time.perf_counter()

print('Execution time:-',endTime-startTime)