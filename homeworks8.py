# ('79052479075', "+# ### ### ## ##") => "+7 905 247 90 75"
# ('79052479075', "+# (###) ### ##-##") => "+7 (905) 247 90-75"
# 2 input alacaqsınız. Birində rəqəmlər və digərində rəqəmlərin uyğun gələcəyi nömrə yazılışı olacaq.
# Həmin nömrə yazılışı içərisindəki diezləri verilən rəqəmlərlə əvəzləməlisiniz.

nomre = input('Nomreni daxil edin: ')
nomre_yazilisi = input('Yazilisi daxil edin: ')
result = ''
i = 0
for j in nomre_yazilisi:
    if j == '#':
        result += nomre[i]
        i += 1
    else:
        result += j
print(result)
        


# n1 = 15 və n2 = 13. Başqa bir variable yaratmadan aşağıdakı sual işarələrini doludurun.
# print('%s + %s = %s' ??????????)
# Output bu şəkildə olmalıdır: 15 + 13 = 28
n1 = int(input('Ededi daxil edin: '))
n2 = int(input('Ededi daxil edin: '))
print('%s + %s = %s' % (n1 , n2 , n1+n2 ))


ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
ferma_1 = ferma[:len(ferma)//2]
ferma_2 = ferma[len(ferma)//2:]
total_1 = 0
total_2 = 0
for i in ferma_1:
    for j,k in qiymetler.items():
        if i==j:
            total_1 += k
for a in ferma_2:
    for p,v in qiymetler.items():
        if a==p:
            total_2 += v
if total_1 > total_2:
    vermelidir = (total_1+total_2)/2 - total_2
    result = f'Boyuk qardas kiciye {vermelidir} manat vermelidir'
else:
    vermelidir = (total_1+total_2)/2 - total_1
    result = f'Kicik qardas boyuke {vermelidir} manat vermelidir'
print(result)



animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
farm = ('inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek')
qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
"""
Axtarilan Heyvan: {???????}
{???????}
Fermadaki {???????} sayi:  {???????}
Diger heyvanlara olan faizi: {???????}
{???????} umumi qiymeti: {???????} AZN
"""
price = 0
for heyvan in farm:
    for k,v in qiymetler.items():
        if animal in farm:
            say = farm.count(animal)
        if animal == heyvan and heyvan==k:
            price += v 
        faiz = (say/len(farm))*100
axtarilan_heyvan = 'Axtarilan Heyvan: {}'.format(animal)
fermadaki_sayi = 'Fermadaki {} sayi: {}'.format(animal,say)
faizi = 'Diger heyvanlara faizi: {}'.format(faiz)
umumi_qiymet = '{} umumi qiymeti: {} AZN'.format(animal,price)
print(axtarilan_heyvan,fermadaki_sayi,faizi,umumi_qiymet)