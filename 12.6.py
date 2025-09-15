text=input()
slova=[]
rev_text=''
text=text+' '
while text!='':
    a=text.find(' ')
    slova.append(text[0:a])
    text=text[a+1:len(text)]
slova=slova[::-1]
for i in range (0,len(slova)):
    rev_text+=slova[i]+' '
print(rev_text)
