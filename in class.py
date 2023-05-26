# İstifadəçinin daxil etdiyi mətn daxilindəki hərflərin ingilis 
# əlifbasındakı sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin. Örnək:
# input: Men Python oyrenirem
# output: 13,5,14, 10,1,22,1,19,3,18,9,16,20, 15,25,18,5,14,9,18,5,13,
# sentence = input('Cumleni daxil edin: ')
# sentence_code = ''
# for i in sentence:
#     if i.isalpha():
#         sentence_code += str(ord(i)) + ', '
#     else:
#         sentence_code += i
# print(sentence_code)


# for numbers in range(0,30):
#     print('{:<8} {:<10} {:<10} {:<10}'.format(numbers,bin(numbers)[2:],oct(numbers)[2:],hex(numbers)[2:]))
'''
Verilmiş stringin sözlərindən bir hashtag yaradan kod yazın. Cümləni hashtag-a çevirərkən
Azərbaycan şriftləri ingilis şriftləri ilə 
əvəz olunmalıdır (Bütün hərflər nəzərə alınmalıdır) və hashtag camelcase ilə yazılmalıdır. Örnək
'''
# aze_dict = {
#     'ə': 'e',
#     'ı': 'i',
#     'ü': 'u',
#     'ö':'o',
#     'ç': 'c', 
#     'ş': 's',
# }

# def count_palindromes(a, b):
#     start = int(a) + 1 if a % 1 > 0 else int(a)
#     end = int(b)
#     polindromes = [num for num in range(start, end+1) if str(num) == str(num)[::-1]]
#     return len(polindromes)
# print(count_palindromes(2.2, 2.9))
