l=list()
dupli=list()
pnum=0
size=int(input("\nEnter list size: "))
print("Enter the ",size," elements :")
for i in range(0,size):
    n=int(input())
    l.append(n)
for i in range(0,size):
    num=l[i]
    for j in range(i+1,size):
        if l[j] == num:
            dupli.append(num)
            l.remove(num)
print(l)
print(dupli) 