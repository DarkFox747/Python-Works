a= 4
b = 1
c = 6
lst = []
lst2 = []
lst3 = []
lst4 = []
for i in range(0,121): 
    if(i % 11 == a):
        lst.append(i)
for i in range(0,121): 
    if(i % 11 != b):
        lst2.append(i)
for i in range(0,121): 
    if(i % 11 != c):
        lst3.append(i)

for i in range(0,121):
    if i in lst or i in lst2 and i in lst3:
        lst4.append(i)
print(lst4)
