t=(1,2,3,4,5,6)
length=len(t)
even=list()
odd=list()
print("Tuple elements are: ",t)
for i in range(0,length):
    if t[i] % 2 == 0:
        even.append(t[i])
    else:
        odd.append(t[i])
print("Even values are: ",even)
print("Odd values are: ",odd)
print()