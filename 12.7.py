text = input()
text = text + ' '
slova = []
while text != '':
    a = text.find(' ')
    slova.append(text[0:a])
    text = text[a+1:len(text)]
ctz = []
for i in slova:
    ct=0
    for j in i:
        ct += 1
    ctz.append(ct)
print(min(ctz))
