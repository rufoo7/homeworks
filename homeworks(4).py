# Listin içərisindəki ədədlərin rəqəmlərinin cəmindən ibarət bir list hazırlayın. Örnək:
# list = [3587, 2454, 19305, 17, 33, 42, 427, 317]
# new_list = []
# for i in list:
#     sum = 0
#     for j in str(i):
#         sum += int(j)  
#     new_list.append(sum)
# print(new_list)

# Verilmiş listin içərisindən 0, None, False, boş string, boş list kimi dataları çıxarın.
# data = ['Python', ' ', 0, 0.0, [], 256, None, 'Coding', 0.256, True, 598, [1, 2, 3], [None]]
# new_data = []
# for i in data:
#     if i:
#         new_data.append(i)
# print(new_data)

# Verilmiş listdən heç bir elementin təkrarlanmadığı yeni bir list yaradın.
# list_1 = [22 , 35 , 66 , 22 , 75 , 66 , 92 , 75 , 43 , 81]
# list_2 = []
# list_2 = list(set(list_1))
# print(list_2)

# İstifadəçi insan yaşı bildirən data daxil edəcək. Aşağıdakı qaydalara əsasən insan 
# yaşını pişik yaşına çevirən bir kod yazın:
# - 1 il insan ömrünə 15 il pişik ömrü;
# - 2-ci il insan ilinə 9 il pişik ömrü;
# - Növbəti hər insan ilinə isə 4 il pişik ömrü qarşılıq gəlir.
# istifadeci_yasi = int(input("Yasinizi daxil edin :"))
# pisik_yasi = 0
# for i in range(1,istifadeci_yasi):
#     if i <= istifadeci_yasi and i != 1 and i != 2:
#         pisik_yasi += 4
#     if i == 1:
#         pisik_yasi += 15
#     if i == 2:
#         pisik_yasi += 9
# print(pisik_yasi)

# Listin ən böyük və ən kiçik elementlərindən başqa bütün elementlərinin cəmini əldə edin. Örnək:
# numbers = [6, 2, 1, 8, 10]
# max = numbers[0]
# min = numbers[1]
# for i in numbers:
#     if i > max:
#         max = i
# for j in numbers:
#     if j < min:
#         min = j
# print(sum(numbers)-max-min)