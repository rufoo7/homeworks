# -20-dən 20-ə qədər (20 daxil olmaqla) olan ədədlər arasından mənfi 
# tək ədədləri, sıfırı və müsbət cüt ədələri print edin.
# Proses tamamlandıqdan sonra isə "Bitdi" yazısı print olunsun.
for number in range (-20,21):
    if ( number % 2 and number < 0 ) or number == 0 or ( number %2 == 0 and number > 0 ):
        print(number)
else :
    print("bitdi")
        