text=input()
A=set()
for i in text:
    if i not in A:
        A.add(i)
print(A)
print(len(A))
