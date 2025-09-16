text = input()
text = text + ' '
done_text = ''
slova = []
while text != '':
    a = text.find(' ')
    slova.append(text[0:a])
    text=text[a+1:len(text)]
for j in range(0, len(slova) - 1):
    for i in range (j + 1, len(slova)):
        if slova[j] == slova[i]:
            print(slova[j])
            break
