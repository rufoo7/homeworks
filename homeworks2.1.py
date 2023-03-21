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