text1 = input()
text2 = input()
text3 = input()
bykvi1 = set()
bykvi2 = set()
bykvi3 = set()
for i in text1:
    if i not in bykvi1:
        bykvi1.add(i)
for i in text2:
    if i not in bykvi2:
        bykvi2.add(i)
for i in text3:
    if i not in bykvi3:
        bykvi3.add(i)
bykvi1_2 = bykvi1|bykvi2
bykvi1_3 = bykvi1|bykvi3
bykvi2_3 = bykvi2|bykvi3
un1 = []
un2 = []
un3 = []
for x in bykvi1:
    if x not in bykvi2_3:
        un1.append(x)
for x in bykvi2:
    if x not in bykvi1_3:
        un2.append(x)
for x in bykvi3:
    if x not in bykvi1_2:
        un3.append(x)
print(un1)
print(un2)
print(un3)
