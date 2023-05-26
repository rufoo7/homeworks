'''Kürə və koni həcmlərini tapan funksiyalar hazırlayın'''
# import math
# def kürə_həcmi(radius):
#     həcm = (4/3) * math.pi * math.pow(radius, 3)
#     return həcm

# def koni_həcmi(radius, height):
#     həcm = (1/3) * math.pi * math.pow(radius, 2) * height
#     return həcm

'''Permutasiya və kombinasiya tapan funksiyalar hazırlayın.'''

# import math
# def permutasiya(n, r):
#     permutasiya_digit = math.factorial(n) / math.factorial(n - r)
#     return permutasiya_digit

# def kombinasiya(n, r):
#     kombinasiya_digit = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
#     return kombinasiya_digit

'''Giveaway programi duzeldin. Adamlar bitənə qədər hər enter basanda bir ad göstərsin. '''
import random
def giveaway(adlar):
    count = 1
    output = random.randint(adlar)
    print(output)
    count += 1
    if count == len(adlar):
        break
adlar = input('Adlari daxil edin: ').split()

    

''' Ədəd təxmin etmə oyunu hazırlayın. Müəyən bir araılq verin 
və program həmin aralıqda bir ədəd təyin etsin. Daha sonra siz 
həmin ədədi tapana qədər oyun davam etsin. Siz gizli ədədin aşağısında 
bir təxmin etdikdə program daha yuxarı, yuxarısında təxmin etdikdə isə 
daha aşağı desin. Ən sonda ədədi neçə səfərə tapdığınızı qeyd etsin. 
Əgər 10 üzərində təxmin etdikdən sonra tapıbsızsa məğlub sayılırsız, 
əks təqdirdə qalib.'''

# import random

# def təxmin_oyunu(araliq):
#     gizli_ədəd = random.randint(araliq[0], araliq[1])

#     f = False
#     cehd_sayi = 0
#     for i in range(10):
#         cehd_sayi += 1
#         texmin = int(input("Təxmin etdiyiniz ededi daxil edin: "))

#         if texmin < gizli_ədəd:
#             print("Daha yuxarı")
#         elif texmin > gizli_ədəd:
#             print("Daha aşağı")
#         else:
#             f = True
#             break
#     if f:
#         print(f"Təbriklər! Gizli ədədi {cehd_sayi}ci cəhdinizdə tapdınız.")
#     else:
#         print(f"Mağlub oldunuz! Gizli ədəd {gizli_ədəd} idi.")
# daxil_edilen_araliq = input('Aralığı daxil edin: ')
# araliq = [int(eded) for eded in daxil_edilen_araliq.split()]
# təxmin_oyunu(araliq)

''' “Saat 17:00, 04.06.2022 tarixində dərsə gəlin” cümləsindən istifadə edərək tarixi datetime formatına çevirin. '''
# from datetime import datetime

# sentence = "Saat 17:00, 04.06.2022 tarixində dərsə gəlin"

# format_str = "Saat %H:%M, %d.%m.%Y tarixində dərsə gəlin"

# tarix = datetime.strptime(sentence, format_str)

# print(tarix)


'''“Rüfət 7 gün sonra 15-00” formasındakı input datalarını dəvətnaməyə çevirən program hazırlayın. 
Yuxarıdakı məlumatın outputu bu şəkildə olacaq: 
Hörmətli Rüfət. Sizi 2022-ci il June ayının 10-cu günü, saat 15:00 tarixində toyumuza dəvət edirik.'''
information = 'Rüfət 7 gün sonra 15-00'
from datetime import datetime, timedelta
