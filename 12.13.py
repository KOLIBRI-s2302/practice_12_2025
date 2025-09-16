text = input()
text = text + ' '
slova = []
while text != '':
    a = text.find(' ')
    slova.append(text[0:a])
    text = text[a+1:len(text)]
nomer = 0
for i in slova:
    nomer += 1
    count = 0
    for j in i:
        if j.isdigit():
            count += 1
    if count % 2 == 0:
        first_sum = 0
        second_sum = 0
        for j in range(0,len(i) // 2):
            first_sum += int(i[j])
        for j in range(len(i) // 2, len(i)):
            second_sum += int(i[j])
        if second_sum == first_sum and second_sum + first_sum != 0:

            print(nomer,i)
