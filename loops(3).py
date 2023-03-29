# Listin bütün elementlərini yoxlayın, hər hansı bir ədəd 1 və ya 
# 2 ilə başlayıb 0 və ya 9 ilə bitmirsə onu çıxarıb yeni bir listə əlavə edin. Misal:
# numbers = [256, 120, 2379, 135, 349, 159] 
# new_numbers = []
# for i in numbers:
#     if not ((str(i)[0] == "1" or str(i)[0] == "2" ) and (int(i) % 10 == 0 or int(i) % 10 == 9)):
#         new_numbers.append(i)
# print(new_numbers)

# İstifadəçi iki ədəd daxil edəcək (num, rep). Daxil edilmiş 
# ədədlərə uyğun aşağıdakı kimi hesablama aparan kod yazın. 
# num = int(input("Ededi daxil edin:"))
# rep = int(input("Ededi daxil edin:"))
# sum = 0
# for i in range(1, rep+1):
#     sum += int(str(num)*i)
# print(sum)

# 1-100 arası ədədləri 3 və 5 vahid artıraraq print edin (1, 4, 9, 12, 17, 20, 25, 28, 31, 36...)
# a = 1
# while a<100 :
#     print(a)
#     print(a+3)
#     a += 8
    
# Verilmiş listin içərisində olan sadə ədələrdən yeni bir list yaradın.
# numbers = [25, 7, 12, 58, 35, 33, 24, 14, 3, 10, 9, 11, 23, 31]
# sade_ededler = []
# for i in numbers:
#     check_number = 0
#     for j in range(2,10):
#         if i != j  and i % j == 0:
#             check_number += 1
#     if check_number == 0:
#         sade_ededler.append(i)
# print(sade_ededler)

name_list = ['Ferid', 'Rufet', 'Zuleyxa', 'Cavad', 'Cavad', 'Zuleyxa', 'Senan','Rufet', 'Cavad', 'Rufet', 'Elvin', 'Reshad']
# -> ['Ferid: 1', 'Rufet: 3', 'Zuleyxa: 2', 'Cavad: 3', 'Senan: 1', 'Elvin: 1', 'Reshad: 1'
# name = []
# for name in name_list:
#     name_and_count = name + ":" + str(name_list.count(name))
#     if name_and_count not in name :
#         name.append(name_and_count)
# print(name)
    
data = ['Ferid', 'Rufet', 123, 250.5, False, [1, 3, 5], None, 0] 
list = []