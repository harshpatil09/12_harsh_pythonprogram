str1=input("\nEnter the string: ")
print(str1)
l1=list(str1)
print(l1)
vo=['a','e','i','o','u']
length1=len(l1)
print(length1)

for i in range(0,length1):
    for j in range(0,5):
        if l1[i]==vo[j]:
            l1.remove(l1[i])
print(l1)


