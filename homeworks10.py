# Daxil edilən stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
# upunion = ('birlesmis', 'milletler', 'teskilati') 

# def cumle (lst):
#     result = ''
#     for i in lst:
#         result += i[0]
#         result = result.upper()
#     return result
# print(cumle(upunion))


# Daxil edilən stringi qeyd edilən şəkildə dəyişən bir funksiya hazırlayın:
# chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') => 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'
# sentence = 'Kitabi sehve-sehve oxumalisan ki, orgenesen'
# def result (cumle):
#     dic = {'sehve': 'sehife',
#        'orgenesen': 'oyrenesen'}
#     for k,v in dic.items():
#         if k in cumle:
#             cumle = cumle.replace(k,v)
#     return cumle
# print(result(sentence))


# Birinci arqument ilk qiyməti, ikinci arqument isə yeni qiyməti göstərir. Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.
# find_percent(200, 60) # output: qiymet 70% azalmisdir 
# find_percent(100, 150) # output: qiymet 50% artmisdir
# digits = input('Reqemleri daxil edin: ')
# def result (reqemler):
#     saylar = reqemler.split(' ')
#     netice = int(saylar[0])/int(saylar[0])*100
#     if netice < 100:
#         print('qiymet {} azalmisdir'.format(100 - netice))
#     elif netice > 100:
#         print('qiymet {} artmisdir'.format(netice - 100))
#     return netice
# result(digits)


# Daxil edilmiş listin ən böyük ədədindən ən kiçiyini çıxarıb, nəticə verən bir funksiya hazırlayın.
# big_dif_sml([6, 3, 8, 9, 2]) => 7 # en  boyuk 9, en kicik 2
# digits = [6, 3, 8, 9, 2]
# def result (lst):
#     lst.sort()
#     print('en boyuk {},en kicik {}'.format(lst[-1],lst[0]))
# result(digits)
        
        
# Üç rəqəmli ədədləri sözə çevirən bir funksiya hazırlayın. Örnək output:
# eded_cevir(658) => altı yüz əlli səkkiz
'''solution 1'''
# eded = int(input('Ededi daxil edin: '))
# def result (digits):
#     levels = {100 : 'yüz', 200 : 'iki yüz', 300 : 'üç yüz', 400 : 'dörd yüz',500 : 'beş yüz' \
#     ,600 : 'altı yüz', 700 : 'yeddi yüz', 800 : 'səkkiz yüz',900 : 'doqquz yüz'\
#     ,10 : 'on', 20 : 'iyirmi', 30 : 'otuz', 40 : 'qırx', 50 : 'əlli', 60 : 'altmış', 70 : 'yetmmiş'\
#     ,80 : 'səksən', 90 : 'doqsam' \
#     ,1 : 'bir', 2 : 'iki', 3 : 'üç', 4 : 'dürd', 5 : 'beş', 6 : 'altı', 7 : 'yeddi', 8 : 'səkkiz', 9 : 'doqquz'
#     }
#     netice = ''
#     for k,v in levels.items():
#         if k == digits - digits % 100:
#             netice += v
#         elif k == digits % 100 - (digits % 100) % 10 :
#             netice += ' ' + v
#         elif k == digits % 10:
#             netice += ' ' + v
#     return netice
# print(result(eded))
'''solution 2'''
# num_names = {
#     0: {'1 ': 'bir', '2' : 'iki', '3' : 'üç', '4' : 'dürd', '5' : 'beş', '6' : 'altı', '7' : 'yeddi', '8' : 'səkkiz', '9' : 'doqquz'},
#     1: {'1' : 'on', '2' : 'iyirmi', '3' : 'otuz', '4' : 'qırx', '5' : 'əlli', '6' : 'altmış', '7' : 'yetmmiş', '8' : 'səksəm', '9' : 'doqsam'},
#     2: {'1' : 'yüz', '2' : 'iki yüz', '3' : 'üç yüz', '4' : 'dörd yüz','5' : 'beş yüz','6' : 'altı yüz', '7' : 'yeddi yüz', '8' : 'səkkiz yüz','9' : 'doqquz yüz'}
# }

# def get_number_name (num):
#     rev_num = str(num)[::-1]
#     result = ''
#     for index, digit in enumerate(rev_num):
#         if digit == '0':
#             continue
#         word = num_names.get(index).get(digit)
#         result = word + ' ' + result
#     return result
# print(get_number_name(256))

# Verilmiş ədədləri tərsinə çevirib toplayan bir funksiya hazırlayın
# numbers = input('Ededleri daxil edin: ')  
# def result (ededler):
#     a = ededler.split(', ')
#     cem = 0
#     for i in a:
#         reverse_number = i[::-1]
#         cem += int(reverse_number)
#     return cem
# print(result(numbers))