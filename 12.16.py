text=input()
flag=1
count_otk=0
count_zak=0
for i in text:
    if i == '(':
        count_otk+=1
    if i == ')':
        count_zak+=1
if count_otk!=count_zak:
    print('Количество открывающих и закрывающих скобок различно')
    flag=0
summa=0
if flag:
    for j in range(0,len(text)):
        for k in range(j,len(text)):
            if text[j]=='(' and text[k]==')':
                summa+=1
    if summa==count_zak*count_otk:
        print('Скобки расставлены правильно')
    else:
        print('Скобки расставлены неправильно')
print(summa)
print(count_zak)
print(count_otk)