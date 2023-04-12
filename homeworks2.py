# Aşağıdakı ədədlərin tərsinə çevrilmiş hallarının cəmini alın. Əgər cəmin ilk rəqəmi təkdirsə
# silinərək qalan hissə qaytarılmalı (məs, 532→32), əks halda isə 2 qatı 
# ilə əvəzlənib geri qaytarılmalıdır (numeric data tipində).
x = 124
y = 651
reverse_x = int(str(x)[::-1])
reverse_y = int(str(y)[::-1])
sum = reverse_x + reverse_y
if (int(str(sum)[0]) % 2 == 1) :
    print(int(str(sum)[1:]))
else:
    print(sum*2)
    

# İstifadəçi 3 fərqli inputda adını, soyadını və ata adını daxil edir. Onun adı proqramda
# ata adı böyük hərflərlə və ardından ad və soyadın
# baş hərfələrinin nöqtələrlə ayrılmış şəkildə qeyd olunmalıdır. 
# Örnək:
# Javier Bardem Pablo -> JAVIER B. P
name = input("Adinizi daxil edin :")
surname = input("Soyadinizi daxil edin :")
f_name = input("Ata adinizi daxil edin :")
full_name = f"{f_name.upper()} {name[0].upper()}. {surname[0].upper()}"
print(full_name)


# 256.91872 ədədinin nöqtədən sonrakı və əvvəlki 
# 2-ci ədədə qədər yuvarlaqlaşdırın. (2 fərqli cavab almalısınız)
x = 256.91872 
print(round(x,-1))
print(round(x,2))


# Verilən floatın tam hissəsinin neçə ədəddən ibarət olduğunu göstərən proqram hazırlayın.
# Bunun üçün input və print funksiyalarından istifadə edin.
n = float(input("Ededi daxil edin :"))
print(len(str(int(n))))



# İstifadəçi ID nömrəsini daxil edəcək. ID nömrə10 simvoldan ibarət olmalı,
# Bunun ilk 3 hərfi hər hansı bir ölkənin qısaltması olmalı (məs, AZE, TUR, USA),
# Həmin qısaltmalar böyük hərflə yazılan ingilis şriftləri olmalı,
# Daha sonrakı 7 character isə ancaq rəqəmlərdən ibarət olmalıdır.
id = input('ID-nizi daxil edin:')
if len(id) == 10 :
    if id.isascii():
        if id[:3].isupper() and id[:3].isalpha():
            if id[3:].isnumeric():
                print("Daxil etdiyiniz sifre dogrudur")
            else :
                print("Yalniz ilk 3 simvol herf ola biler")
        else :
            print("ilk 3 xarakter yalniz boyuk herflerden ibaret olmalidir")
    else :
        print("ID-niz yalniz ingilis herflerinden ibaret ola biler")
else : 
    print("ID-niz yalniz 10 simvoldan ibaret ola biler")