text=input()
count=0
A=set()
for i in text:
    if i not in A:
        A.add(i)
for i in A:
    for j in text:
        if j==i:
            count+=1
    print (i,count)
    count=0