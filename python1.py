a=[3,83,92,48,2,9,90,99,0,1,2]
max=a[0]
min=a[0]
for i in a:
    if i>max:
     max=i
    if i<min:
     min=i

print("the largest number is :",max)
print("the smallest number is :",min)
