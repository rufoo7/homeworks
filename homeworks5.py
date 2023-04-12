# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]
# 1. istifadəçi username-i səhv daxil edərsə belə bir istifadəçi yoxdur deyin
# username_1 = input("Usernamenizi daxil edin :")
# for i in users:
#     if i['username'] != username_1:
#         print('Bele bir istifadeci yoxdur')
#     else:
#         print("Dogrudur")
#     break
# 2. şifrəni səhv daxil edərsə şifrəniz yanlışdır deyin
# password_1 = input("Sifrenizi daxil edin:")
# for i in users:
#     if i['password'] != password_1:
#         print("Sifreniz yanlisdir")
#     else:
#         print('Sifreniz dogrudur')
#     break
# 3. əgər blok olunubsa “Siz daxil ola bilməzsiniz” deyin
# username = input("Istifadeci adinizi daxil edin :")
# for i in users:
#     if i['username'] == username:
#         if i['blocked'] == True:
#             print("Siz daxil ola bilmezsiniz")
#         break
# 4. əgər hər şey qaydasındadırsa “Filankəs, giriş etdiniz” deyin
# username_1 = input("Username daxil edin:")
# password_1 = input('Sifrenizi daxil edidn:')
# for i in users:
#     if i['username'] == username_1:
#         if i['blocked'] != False:
#             print("Siz daxil ola bilmezsiniz")
#         elif i['password'] == password_1:
#             print(f"{i['name']},giris etdiniz")
#         else:
#             print("Sifreniz yanlisdir")
#         break
# else:
#     print("Bele bir istifadeci yoxdur")


# user = {
#     'name': 'Elnur',
#     'height': 179,
#     'phone': {
#         'model': 'Iphone',
#     },
#     'orders': ['book', 'mouse', 'mousepad']
# }
# 1. İstifadəçinin boyunu artırın
# user['height'] = 194
# print(user)
# 2. Telefonun markasını dəyişərək Samsung edin
# user['phone']['model'] = 'Samsung'
# print(user)
# 3. İstifadəçinin adını silin
# del user['name']
# print(user)
# 4. İstifadəçinin ilk sifarişini silin
# del user['orders'][0]
# print(user)
# 5. İstifadəçinin sifarişlərinin başına ball əlavə edin
# 6. Sonuna headphones əlavə edin

# Istifadəçi sizə "5 salam" şəklində solda ədəd, ortada, boşluq, sağda isə bir input verəcək. Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər
# yazıb, istifadəçiyə qatarın. 
# Örnək yuxaridakı inputun outputu salam salam salam salam salam


# [2384, 12385, 13226, 653, 12362423] 
# list içərisindəki ədədlərin key
# olduğu və value-ların həmin ədədlərin 
# rəqəm sayı olduğu bir dictionary hazırlayın


# 100-dən müsbət 100-ə qədər ədədlər arasında 7-yə bölünən ədədlərin 
# 3-ə vurulmasından ibarət bir list qurun. Bunun üçün range və list comprehensions istifadə edin.
# lst = [i*3 for i in range(-100,100) if i%7==0]
# print(lst)

qiymetler = {'Nescafe 500 gr': 8, 'Tess 350 gr': 4.5, 'Jacobs 500 gr': 9.5, 'Cappucino J': 6.4}
mehsullar = ['Nescafe 500 gr', 'Jacobs 500 gr']
vergi_faizi = 0.08
total_price = 0
for k,v in qiymetler.items():
    if k in mehsullar:
        total_price += v
vergi = total_price+total_price*vergi_faizi
print(vergi)