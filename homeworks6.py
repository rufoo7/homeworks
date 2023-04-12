# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }
# İstifadəçi bir input vasitəsilə bunun kimi bir məlumat daxil edəcək:
# input: firstname Elcin, username elchina, birthday 18-08-2000
# Bu inputa əsasən yuxarıdakı dictionary-ni update edin ve istifadəçiyə göstərin.
# Misal yuxarıdakı inputa əsasən dictionary-in son halı aşağıdakı kimi olacaq:
# new_data = input("Verilenleri daxil edin: ")
# for i in new_data.split(', '):
#     a, b = i.split()
#     for k, v in user_info.items():
#         if a == k:
#             user_info[k] = b
# print(user_info)

# mehsullar = [["Samsung A7", 55], ["Iphone 5"], ["Xiaomi 5879", 158], ["Iphone 13", 98], ["Iphone 14", 0]]

# a = {'Samsung A7': 55, 'Iphone 5': None, 'Xiaomi 5879': 158, 'Iphone 13': 98, 'Iphone 13': 'Sold-out}
# new_dict = {}
# for i in mehsullar:
#     if len(i) != 2:
#         new_dict[i[0]] = None
#     elif i[1] == 0:
#         new_dict[i[0]] = 'Sold-out'  
#     else:
#         new_dict[i[0]] = i[1]
# print(new_dict)

# 1. İstifdəçinin daxil etdiyi bir ədədə əsasən belə bir hesablama aparılmalıdır. 
# Daxil edilmiş ədəd dəfə (1/x)lər toplanılmalıdır. x 1-dən başlayaraq üç-üç artır.
# sum = 0
# n = int(input("Ededi daxil edin: "))
# for i in range(1,n*3,3):
#     sum += 1/i
#     sum = round(sum ,2)
# print(sum)


# authors = [
#  {'author': 'Ruslana Q.',
#   'article_number': 10,
#   'read_count': 1795,
#   'loyal_readers': 15
# },{
#   'author': 'Ferid B.',
#   'article_number': 11,
#   'read_count': 1033,
#   'loyal_readers': 3
# },{
#   'author': 'Kenan M.',
#   'article_number': 7,
#   'read_count': 2560,
#   'loyal_readers': 33
# },{
#   'author': 'Cavid R.',
#   'article_number': 5,
#   'read_count': 759,
#   'loyal_readers': 0
# },{
#   'author': 'Zerife O.',
#   'article_number': 8,
#   'read_count': 1700,
#   'loyal_readers': 4
# },{
#   'author': 'Tunzale M.',
#   'article_number': 17,
#   'read_count': 4641,
#   'loyal_readers': 18
# },{
#   'author': 'Salman Q.',
#   'article_number': 4,
#   'read_count': 1800,
#   'loyal_readers': 29
# },{
#   'author': 'Qalib A.',
#   'article_number': 6,
#   'read_count': 1101,
#   'loyal_readers': 5
# }
# ]

# aze_dict = {
#     'ə': 'e',
#     'ı': 'i',
#     'ü': 'u',
#     'ö':'o',
#     'ç': 'c', 
#     'ş': 's',
# }
# sentence = input("Cumleni daxil edin: ")
# sentence = sentence.lower()
# for k, v in aze_dict.items():
#     if k in sentence:
#         sentence = sentence.replace(k,v)
# hastag = '#'
# for i in sentence.title().split():
#     hastag += i 
# print(hastag)

# dictionary = {
#   'ə': 'e',
#   'ı': 'i',
#   'ö': 'o',
#   'ü': 'u',
#   'ş': 's',
#   'ç': 'c',
#   'ğ': 'g'}

# [('ə', 'e'), ('ı', 'i'), ('ö', 'o'), ('ü', 'u'), ('ş', 's'), ('ç', 'c'), ('ğ', 'g')]
# lst = []
# for k, v in dictionary.items():
#     lst = list(tuple(dictionary.items()))
# print(lst)

