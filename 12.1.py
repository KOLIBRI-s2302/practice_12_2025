text = input()
prbl = 0
maxim = -1
for i in text:
    if i == ' ':
        prbl += 1
    else:
        maxim = max(prbl , maxim)
        prbl = 0
print (maxim)

