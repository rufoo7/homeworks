users = [
    {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
    {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
    {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
]
user_name = input('İstifadeci adinizi daxil edin: ')
user_found = False

for i in users:
    if user_name == i['username']:
        user_found = i 

if not user_found:
    print('Bele bir istifadeci yoxdur')
    exit()

password = input('Sifrenizi daxil edin: ')

if password == user_found['password']:
    if user_found['blocked'] == False:
        print(user_found['name'], 'giris etdiniz')
    else:
        print('Siz daxil ola bilmezsiniz')
else:
    print('Sifre yalnisdir')


user = {
    'name': 'Elnur',
    'height': 179,
    'phone': {
        'model': 'Iphone',
    },
    'orders': ['book', 'mouse', 'mousepad']
}
# 1. İstifadəçinin boyunu artırın
n = int(input('Boyunu artirin: '))
user['height'] += n
print(user)
# 2. Telefonun markasını dəyişərək Samsung edin
user['phone']['model'] = 'Samsung'
print(user)
# 3. İstifadəçinin adını silin
del user['name']
print(user)
# 4. İstifadəçinin ilk sifarişini silin
del user['orders'][0]
print(user)
# 5. İstifadəçinin sifarişlərinin başına ball əlavə edin
# 6. Sonuna headphones əlavə edin




# Istifadəçi sizə "5 salam" şəklində solda ədəd, ortada, boşluq, sağda isə bir input verəcək. Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər
# yazıb, istifadəçiyə qatarın. 
# Örnək yuxaridakı inputun outputu salam salam salam salam salam
n = input('Metni daxil edin: ')
number, greeting = n.split()
result = int(number) * (greeting + ' ')
print(result)


# list içərisindəki ədədlərin key
# olduğu və value-ların həmin ədədlərin 
# rəqəm sayı olduğu bir dictionary hazırlayın
numbers = [2384, 12385, 13226, 653, 12362423]
result = {number: len(str(number)) for number in numbers}
print(result)


# 100-dən müsbət 100-ə qədər ədədlər arasında 7-yə bölünən ədədlərin 
# 3-ə vurulmasından ibarət bir list qurun. Bunun üçün range və list comprehensions istifadə edin.
lst = [i*3 for i in range(-100,100) if i%7==0]
print(lst)

qiymetler = {'Nescafe 500 gr': 8, 'Tess 350 gr': 4.5, 'Jacobs 500 gr': 9.5, 'Cappucino J': 6.4}
mehsullar = ['Nescafe 500 gr', 'Jacobs 500 gr']
vergi_faizi = 0.08
total_price = 0
for k,v in qiymetler.items():
    if k in mehsullar:
        total_price += v
vergi = total_price+total_price*vergi_faizi
print(vergi)