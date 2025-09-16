text = input()
text = text + ' '
slova = []
flag = 1
while text != '':
    a = text.find(' ')
    slova.append(text[0:a])
    text = text[a+1:len(text)]
bykva_last = []
for i in slova:
    bykva_last.append(i[-1])
for k in range (0,len(bykva_last)):
    j = bykva_last[k].upper()
    bykva_last.insert(k,j)
    bykva_last.pop(k + 1)
if len(bykva_last) != 1:
    for i in range(1,len(slova)):
        if slova[i].startswith(bykva_last[i - 1]):
            continue
        else:
            if i % 2 == 1:
                print('Не жульничай, Вася')
                flag = 0
                break
            if i % 2 == 0:
                print('Не жульничай, Петя')
                flag = 0
                break
    if flag:
        if i % 2 == 1:
            print('Победил Вася')
        if i % 2 == 0:
            print('Победил Петя')
    if flag==0:
        if i % 2 == 0:
            print('Победил Вася')
        if i % 2 == 1:
            print('Победил Петя')
else:
    print('Вася не назвал слово')



