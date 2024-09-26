import sys
import numpy as np

#for line in sys.stdin:
#        if 'Exit' == line.rstrip():
#            break
#        print(f'Processing Message from sys.stdin *****{line}*****')
#print("Done")

hex = sys.stdin.readline().strip().split(',')
time= sys.stdin.readline().strip().split(',')
income= sys.stdin.readline().strip().split(',')
age= sys.stdin.readline().strip().split(',')
gender= sys.stdin.readline().strip().split(',')
time = [int(i) for i in time]
totalPeople= np.array([*range(time[0],time[1])])*0
print(len(totalPeople))