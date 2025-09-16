hint = input()
code = input()
code_spisok = []
for i in code:
    code_spisok.append(i)

for i in range (0,26):
    print("\n")
print(hint)
secret = []
for i in range (0, len(code)):
    secret.append('*')
for pop in range (0, 11):
    if '*' not in secret:
        break
    for z in range(0, len(secret)):
        print(secret[z], end='')
    print('\nБуква(0) или Слово(1)?')
    vibor=int(input())
    if vibor == 0:
        bykva = input('Введите букву ')
        if bykva in code_spisok:
            for i in range(0, len(code_spisok)):
                if bykva == code_spisok[i]:
                    secret.insert(i, code_spisok[i])
                    secret.pop(i + 1)
        else:
            print('Такой буквы в слове нет')
            continue
    if vibor == 1:
        slovo = input('Введите слово ')
        slovo_igroka = []
        for i in slovo:
            slovo_igroka.append(i)
        if slovo_igroka == code_spisok:
            for i in range(0, len(code_spisok)):
                secret.insert(i, code_spisok[i])
                secret.pop(i + 1)
        else:
            print('Неверное слово')
            continue
if '*' in secret:
    print('Поражение :(')
    print(code)
if '*' not in secret:
    print('Победа! :)')
    print(code)

