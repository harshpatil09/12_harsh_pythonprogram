l=list()
p=list()
pnum=0
a=int(input("\nEnter list size: "))
print("Enter the ",a," elements :")
for i in range(0,a):
    n=int(input())
    l.append(n)
print("The list is : ",l)

for i in range(0,a):
    num=l[i]
    for j in range(2,num):
        if num % j == 0:
            p.append(num)
            pnum=pnum+1
            break
for i in range(0,pnum):
    l.remove(p[i])       
            
print("\nThe new list is: ",l)
print("The prime no. list is: ",p)
print()
        
    