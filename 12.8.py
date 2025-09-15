text=input()
text=text+' '
done_text=''
slova=[]
while text!='':
    a=text.find(' ')
    slova.append(text[0:a])
    text=text[a+1:len(text)]
ctz=[]
for i in slova:
    ct=0
    for j in i:
        ct+=1
    ctz.append(ct)
ctz.sort(reverse=True)
print(ctz)
print(slova)
for i in ctz:
    for j in slova:
        if i==len(j):
            done_text+=j+' '
            slova.remove(j)
print(done_text)