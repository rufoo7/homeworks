# İstifadəçinin daxil etdiyi mətn daxilindəki hərflərin ingilis 
# əlifbasındakı sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin. Örnək:
# input: Men Python oyrenirem
# output: 13,5,14, 10,1,22,1,19,3,18,9,16,20, 15,25,18,5,14,9,18,5,13,
sentence = input('Cumleni daxil edin: ')
sentence_code = ''
for i in sentence:
    if i.isalpha():
        sentence_code += str(ord(i)) + ', '
    else:
        sentence_code += i
print(sentence_code)


# for numbers in range(0,30):
#     print('{:<8} {:<10} {:<10} {:<10}'.format(numbers,bin(numbers)[2:],oct(numbers)[2:],hex(numbers)[2:]))