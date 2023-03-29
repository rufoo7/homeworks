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