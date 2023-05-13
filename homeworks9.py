# Istifadəçinin daxil etdiyi stringi binary şəklində göstərin.
# sentence = input('Cumleni daxil edin: ')
# sentence_code = ''
# for i in sentence:
#         sentence_code += bin(ord(i))[2:] + ' '
# print(sentence_code)


# Istifadəçi input olaraq color: rgb(127, 255, 12) şəklində CSS rəngi daxil edəcək.
# Siz istifadəçinin daxil etdiyi rəngi 16-lıq sistemdəki qarşılığına çevirin.
# colors = 'color: rgb(127, 255, 12)'
# hex_code = ''
# colors= "color: rgb(244, 123, 12)"
# size = colors.split('rgb(')[1].split(')')[0].split(', ')
# for i in size:
#     hex_code += hex(int(i))[2:].zfill(2)
# print('color: #' + hex_code)


# İstifadəçi arada boşluq olmaqla birlikdə 2 - 9 arasında bir sayma sistemi və həmin sistemdə yazılmış bir 
# ədəd daxil edəcək. Həmin ədədi 10-luq sistemə çevirib, istifadəçiyə göstərin
# system_and_number = input('Sistemi ve ededi daxil edin: ')
# number = system_and_number.split(' ')[1]
# system = system_and_number.split(' ')[0]
# say = len(number)
# onluq_eded = 0
# for i in number:
#     onluq_eded += (int(system)**(say-1)) * int(i) 
#     say -= 1
# print(onluq_eded)


# isascii() metodundan istifadə etmədən hər hansı bir stringin isascii olduğunu yoxlayan kod yazın.
# sentence = input('Cumleni daxil edin: ')
# f = True
# for i in sentence:
#     if ord(i) >= 128:
#         f = False
#         break
# if f == False:
#     print('ASCII\'dir')
# else:
#     print('Deyil')



