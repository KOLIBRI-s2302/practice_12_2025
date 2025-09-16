code = input()
code_spisok = []
flag = 1
for i in code:
    code_spisok.append(i)

if flag:
    for i in range(0, 26):
        print("\n")
    for pop in range(0, 11):
        bik = 0
        korova = 0
        print('Введите число')
        chislo = input()
        chislo_igroka = []
        for i in chislo:
            chislo_igroka.append(i)
        for j in range (0,len(code)):
            if chislo_igroka[j] in code_spisok and chislo_igroka[j] == code_spisok[j]:
                bik += 1
            if chislo_igroka[j] in code_spisok:
                korova += 1
        korova = korova-bik
        print('Количество быков:', bik, 'Количество коров: ', korova)
        if bik == 4:
            print('Победа!')
            print(code)
            break
        if pop == 10 and bik != 4:
            print('Поражение')
            print(code)

