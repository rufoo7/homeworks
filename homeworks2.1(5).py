# İstifadəçi ID nömrəsini daxil edəcək. ID nömrə10 simvoldan ibarət olmalı,
# Bunun ilk 3 hərfi hər hansı bir ölkənin qısaltması olmalı (məs, AZE, TUR, USA),
# Həmin qısaltmalar böyük hərflə yazılan ingilis şriftləri olmalı,
# Daha sonrakı 7 character isə ancaq rəqəmlərdən ibarət olmalıdır.
id = input('ID-nizi daxil edin:')
if len(id) == 10 :
    if id.isascii():
        if id[:3].isupper():
            if id.isalnum():
                print("Daxil etdiyiniz sifre dogrudur")
            else :
                print("ID-niz yalniz herf ve reqemlerden ibaret olmalidir")
        else :
            print("Herfler yalniz boyuk yazilmalidir")
    else :
        print("ID-niz yalniz ingilis herflerinden ibaret ola biler")
else : 
    print("ID-niz yalniz 10 simvoldan ibaret ola biler")