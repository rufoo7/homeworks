# 1. 1-dən 100-ə kimi olan bütün 
# ədədlərin toplamını tapın (1+2+3+...+99+100)
# 2. 100000-dən aşağı doğru gedərək 
# 9999-a bölünən ilk ədədi konsolda göstərin.
# 3. `'Men her gun Python oyrenirem’` bu stringin saitlər çıxarılmış vəziyyətini konsolda göstərin.


# sum = 0
# for i in range(100):
#     sum += i
# print(sum)

# sum = 0
# number = 1
# while number < 100:
#     sum += number
#     number += 1
# print(sum)

# for i in range(100000,1,-1):
#     if i % 9999 == 0:
#         print(i)
#         break

# number = 100000
# while number <= 100000:
#     if number % 9999 == 0:
#         print(number)
#         break
#     number -= 1

# saitler = 'aioueAIOUE'
# sentence = 'Men her gun Python oyrenirem'
# for i in sentence:
#     if i not in saitler:
#         print (i)

# saitler = 'aioueAIOUE'
# sentence = 'Men her gun Python oyrenirem'
# i = 0
# while i < len(sentence):
#     if sentence[i] not in saitler:
#         print(sentence[i])
#     i += 1

# # İstifadəçinin daxil etdiyi cümlədə neçə heca olduğunu deyən program hazırlayın.
# sentence = input("Cumleni daxil edin :")
# heca_sayi = 0
# saitler = 'aioueAIOUE'
# for i in sentence:
#     if i in saitler:
#         heca_sayi += 1
# print('Hecalarin sayi :',heca_sayi)

# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci'] 
# # Fermada keçinin sırasını tapı
# print (ferma.index('keci'))

# # Fermadakı heyvanları ad sırasına görə sıralayın
# k = sorted(ferma)
# print (k)

# # Fermadan bir at çıxarıb, ən sağdan bir toyuq əlavə edin
# ferma.pop("at")
# ferma.append('toyuq')
# print(ferma)

# # Ən soldan bir keci əlavə edin
# ferma.insert(0,'keci')
# print(ferma)

# # Fermanın yarısını dinamik bir şəkildə silin
# new_ferma = ferma[:len(ferma)//2]
# print(new_ferma)

# Yeni gələn 
# a = ['at', 'qoyun', 'inek', 'inek', 'qoyun'] 
# heyvanları fermaya əlavə edin
# ferma.extend(a)
# print(ferma)

# Fermadakı heyvanları 3 qatına çıxarın
# ferma = ferma*3
# print(ferma)

# Fermadakı heyvanları tərsinə sıralayın
# ferma.reverse()
# print(ferma)

# Fermadakı inəklərin sayının ümumi fermanın neçə faizi olduğunu tapın
# ineklerin_sayi = ferma.count("inek")
# umumi_say = len(ferma)
# faiz = (ineklerin_sayi*100)/umumi_say
# print(faiz)

# Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verini
# ferma_2 = ferma.copy()
# print(ferma_2)

# Fermadan heyvanları çıxarın
# ferma.clear()
# print(ferma)

#  Aşağıdakı result listinin 0-cı indexinə numbers listi daxilindəki müsbət ədədlərin
#  cəmini, 1-ci indexə isə mənfi ədədlərin cəmini yerləşdirin. 
# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# for i in numbers:
#     if i>0:
#         result[0] += i
#     if i<0:
#         result[1] += i
# print(result)