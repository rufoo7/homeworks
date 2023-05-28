'''1000 ədəd random yığılmış floatdan ibarət list hazırlayın. 
Daha sonra daxil edilənlistin ən böyük elementini tapan 2 funksiya hazırlayın. 
Birincisi parametrdəki listi sort edib, son elementi çıxarsın, digəri isə bu əməliyyat üçün seçilmiş 
alqoritm (infinity ilə başlayan ilk dəyərə sahib alqoritm) 
ilə işləsin. timeit ilə hazırladığınız iki funksiyanın sürətlərini ölçün'''
# import random
# import timeit

# random_list = [random.uniform(0.0, 1.0) for _ in range(1000)]

# def find_largest_sorted(lst):
#     sorted_lst = sorted(lst)
#     largest = sorted_lst[-1]
#     return largest

# def find_largest_with_algorithm(lst):
#     largest = float('-inf')
#     for num in lst:
#         if num > largest:
#             largest = num
#     return largest

# time_sorted = timeit.timeit(lambda: find_largest_sorted(random_list), number=1000)
# time_algorithm = timeit.timeit(lambda: find_largest_with_algorithm(random_list), number=1000)

# print('1', time_sorted)
# print('2', time_algorithm)

'''Asağıdaki alqoritmlərin sürətini ölçün.'''
import timeit

def time_test(text):
    textreverse = text[::-1]
    vowels = 'aeiuo'
    result = ''
    for char in textreverse:
        if char not in vowels:
            result += char
    # print(result)
text = 'I live in New York'

time_taken = timeit.timeit(lambda: time_test(text), number = 1000)
print(time_taken)

def time_test2(text):
    text.reverse()
    vowels = 'aeiuo'
    for char in text:
        if char not in text:
            text.remove(char)
    # print(''.join(text))
text = list('I live in New York')

time_taken2 = timeit.timeit(lambda: time_test2(text), number = 1000)
print(time_taken2)
'''Geri sayim programi hazirlayin. Input olaraq bir deyer verin 
və program həmin dəyərdən 0-a doğru saniyə-saniyə geri saysın. 0-a çatdıqda bitdi desin.'''
# import time

# n = int(input("Ededi daxil edin: "))

# for saniye in range(n, 0, -1):
#     print(f'{saniye} saniye')
#     time.sleep(1)

# print("Bitdi.")
