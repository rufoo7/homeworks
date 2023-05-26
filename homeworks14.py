baliqlar = {
    'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'koteks vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}
'1. Quşların xüsusiyyətlərinə `"2 ayaq"` əlavə edin.'
# quslar.add('2 ayaq')
# print(quslar)
'2. Balıqların xüsusiyyətlərindən `"4 ayaq"` məlumatını çıxarın'
# baliqlar.remove('4 ayaq')
# print(baliqlar)
'3. Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın'
# print(amfibialar.intersection(cuculer))
'4. Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın'
# print(baliqlar.difference(amfibialar))
'5. Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın'
# f = False
# for sinif,s in sinifler.items():
#     if baliqlar.intersection(s) == False:
#         f == True 
# if f:
#     print(sinif)
# else:
#     print('Bele bir sinif yoxdur')

'6. Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın'
# max = 0
# max_ortaq = ''
# for sinif,s in sinifler.items():
#     if sinif == 'quslar':
#         continue
#     say = len(quslar.intersection(s))
#     if say > max:
#         max = say
#         max_ortaq = sinif
# print(max_ortaq)

# İstifadəçi input ilə sizə bəzi özəlliklər girəcək 
# Siz həmin özəlliklərə əsasən heyvanın hansı 
# sinifə aid ola biləcəyini təxmin edən kod yazın.
characteristic_things = input('')
d = dict()
for sinif,s in sinifler.items():
    sinif_count = 0
    for i in characteristic_things.split(', '):
        if i in s:
            sinif_count += 1
        d[sinif] = sinif_count
print(d)