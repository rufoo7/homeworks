#   İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın.   
# Örnək:
# Input: This is an example! 
# Output: sihT si na !elpmaxe

sentence = "This is an example!" 
new_string = "python"
sentence_2 = sentence.split(" ")
n = []
for i in sentence_2:
    n.append(i[::-1])
a = " ".join(n)
print(a)


info = ["Resul", "Serifov", 35]
# Yuxarıdakı listi dinamik olaraq `["Resul Serifov", 25]` vəziyyətinə gətirin.
info[0] = 'Resul Serifov'
info.pop(1)
info[1] = 25
print(info) 


shop = {
					"t-shirt" : 59.00,
					"jeans" : 75.00,
					"sweatshirt" : 60.00, 
					"shoe" : 124.99, 
					"jacket" : 154.90
				}
# Dictionary əsasən istifadəçi sizə məhsul adı girəcək. Bu məhsulun mağazada olan qiymətini
# göstərən proqram hazırlayın. Girilən məhsul mağaza da olmadığı halda "None" qaytarın.
mehsulun_adi = input("Mehsulun adini daxil edin :")
for k, v in shop.items():
    if mehsulun_adi == k:
        print(v)

        
# Mağazaya yeni məhsullar və qiymətlərini əlavə edin.
new_things = {
               "nike shoe" : 215.89,
               "zara jeans" : 432.99
            }
shop.update(new_things)
print(shop)

# Mağazada nə qədər məhsul olduğunu göstərin
print(len(shop))

# Məhsulların qiymətini 30% artırıb yeni qiymətləri mağazaya əlavə edin.
for i in shop:
    shop[i] *= 1.3
print(shop)