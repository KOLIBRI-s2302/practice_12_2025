text=input()
pvtr=1
maxim=-1
for i in range (0,len(text)-1):
    if text[i]==text[i+1]:
        pvtr+=1
    else:
        maxim=max(pvtr,maxim)
        pvtr=1
print(maxim)
