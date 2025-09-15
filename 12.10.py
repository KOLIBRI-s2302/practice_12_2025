text=input()
text=text+' '
done_text=''
slova=[]
while text!='':
    a=text.find(' ')
    slova.append(text[0:a])
    text=text[a+1:len(text)]
udal=[]
for i in range(0,len(slova)):
    if slova[i]==slova[0]:
        udal.append(i)
for i in range (0,len(udal)):
    slova.pop(udal[i])
    slova.insert(udal[i],'')
for i in slova:
    A=[]
    for j in range(0,len(i)):
        if i[j] in A:
            slova.remove(i)
            slova.insert(j, '')
            break
        if i[j] not in A:
            A.append(i[j])
while '' in slova:
    slova.remove('')
for i in slova:
    done_text+=i+' '
print(done_text)