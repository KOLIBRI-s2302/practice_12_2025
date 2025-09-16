from keyword import kwlist
allowed_lett = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z','_', 'A',
              'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
              'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y',
              'Z', '1', '2', '3', '4', '5', '6',
              '7', '8', '9', '0']
text = input()
if text in kwlist:
    print ('Это слово ключевое')
    text = ''
if text[0].isdigit():
    print ('Имя не может начинаться с цифры')
    text = ''
for i in text:
    if i not in allowed_lett:
        print ('В имени присутствует недопустимый знак')
        text = ''
        break
if text!= '':
  print ('Это имя подходит')
