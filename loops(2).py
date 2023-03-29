# # Verilmiş bir ədədin faktorialını hesablayın
# n = int(input("Ededi daxil edin :"))
# fakt = 1
# for i in range(1,n+1):
#     fakt *=i
# print(fakt)

# Verilmiş stringin içərsiində neçə ədəd n hərfi olduğunu göstərən kod yazın.
# sentence = 'Python is Number 1 programming language.'
# a = 0
# for i in range(len(sentence)):
#     if sentence[i] == "n" or sentence[i] == "N":
#         a+=1
# print("nlerin sayi",a)

# Verilmiş stringdən indexi cüt sayda olan elementləri print edin.
# name_surname = "Rufet Quliyev"
# for i in range (len(name_surname)):
#     if i % 2 == 0:
#         print(name_surname[i])

# 1-dən 100-ə qədər olan ədədlər arasından verilmiş list içərisində 
# olmayanları print edin (və ya onların cəmini əldə edin)
# list = [2, 7 ,35 ,89 ,77]
# sum = 0
# for i in range (1,101):
#     if i not in list :
#         sum += i
# print(sum)

# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62] 
#  list içərisindəki 
# ən böyük və ən kiçik ədədi dinamik şəkildə tapın.
# max = 0
# min = 0
# numbers.sort()
# min = numbers [0]
# max = numbers [-1]
# print(max,min)
# print(numbers)

# Aşağıda tələbələrin semestr nəticələri qeyd edilmişdir. Buna əsasən qeyd olunmuş statistik məlumatları
# eyni anda print edin.
#     1. Tələbə sayı
#     2. Ümumi ortalama.
#     3. Kəsilən tələbələrin ümumi faizi (51- qiymət alanlar)
#     4. Yüksək nəticə göstərən tələbələrin ümumu faizi (80+ qiytət alanlar)
# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# telebe_sayi = 0
# kesilen_telebeler = 0
# kecen_telebeler = 0
# for i in r:
#     telebe_sayi += i
#     if i <51 :
#         kesilen_telebeler += 1
#     elif i>80 :
#         kecen_telebeler += 1
# umumi_ortalama = telebe_sayi/len(r)
# kesilen_telebe_faiz = (kesilen_telebeler*100)/len(r)
# kecen_telebe_faiz = (kecen_telebeler*100)/len(r)
# print("Umumi ortalama :",umumi_ortalama,"Kesilen telebelerin umumi faizi",kesilen_telebe_faiz,"Kecen telebelerin umumi faizi",kecen_telebe_faiz,"Telebelerin sayi:",len(r))

# İstifadəçinin girdiyi ədədi tək ədədlərdən ibarət tərsinə çevirilmiş list şəklinə salın.
# Listin bütün elementlərinin integer olmasına diqqət edin. Örnək:
# input: 834255
# output: [5, 5, 2, 4, 3, 8]
# n = input("Ededi daxil edin:")
# reverse_n = n[::-1]
# l = []
# for i in reverse_n:
#     if int(i) % 2:
#         l.append(int(i))
# print(l)
