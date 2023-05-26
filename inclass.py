# aze_dict = {
#     'ə': 'e',
#     'ı': 'i',
#     'ü': 'u',
#     'ö':'o',
#     'ç': 'c', 
#     'ş': 's',
#     'ğ': 'g'
# }
# hastag_word = input('Cumleni daxil edin: ')
# hastag_word = hastag_word.lower()
# def k (sentence):
#     result = ''
#     for k,v in aze_dict.items():
#         if k in sentence:
#             sentence = sentence.replace(k,v)
#     for i in sentence.title().split():
#         result += i
#     return result
# print('#'+ k(hastag_word))


# fruits = {
#     ('banana', 'kiwi'): 'citrus',
#     ('banana', 'kiwi', ['banana', 'orange']): 'citrus'
# }
# print(fruits)


# def get_sum (prices):
#     result = 0
#     for i in prices:
#         result += i
#     return result

# def getcurrency (*args, **kwargs):
#     # args = (24, 560, 58, 478)
#     # kwargs = {'azn': 1.78, 'euro': 2}
#     for k, v in kwargs.items():
#         # return f'{k.upper()} total price: {get_sum(args) * v}'
#         print(f'{k.upper()} total price: {get_sum(args) * v}')
        

# getcurrency(24, 560, 58, 478, dollar=1.78, euro=2)


# def get_reversed (num):
#     num = str(num)[::-1]
#     return int(num)

# get_reversed = lambda num: int(str(num)[::-1])
# print(get_reversed(453))



# Lambda ilə factorial hesablayan recursive function hazırlayın.
# factorial = lambda number: 1 if number == 0 else number*factorial(number-1)
# print(factorial(5))


# Aşağıdakı ədədlər arasında rəqəmlərinin cəmi ən yüksək olanı çıxarın.
# numbers = [85856, 73930, 95298, 57870, 99688, 92907, 13075, 12905, 52948, 97687, 10832, 78757, 
#            99502, 65889, 34618, 59109, 83419, 31486, 94522, 34400 ]
# def sum_of_digits(number):
#     sum = 0
#     for i in str(number):
#         sum += int(i)
#     return sum
# max_number = max(numbers, key = sum_of_digits)
# print(max_number)
        
        
# children = ['Arif', 'Babek', 'Hesen', 'Rufet', 'Sahin', 'Eldeniz', 'Turan', 'Sahmar', 'Kamal', 'Ruslan']
# gifts = ['Ball', 'Iphone', 'Bicycle', 'Ball', 'Piano', 'Bicycle', 'Socks', 'Play Station', 'Ball', 'Socks']
# prices = {'Ball': 10, 'Iphone': 1100, 'Bicycle': 500, 'Piano': 1500, 'Socks': 10, 'Play Station': 1200}

# children_and_gifts = list(zip(children,gifts))

# sorted_children_gifts = sorted(children_and_gifts, key=lambda x: prices[x[1]],reverse = True)
# for name,gifts in sorted_children_gifts:
#     print('{} {} manat deyerinde {} goturub'.format(name,prices[gifts],gifts))


# data = [{'a': 1, 'b': 2}, 5, 7.8, 'asdf', 23, ['a', 'b'], True,  False]
# types = {list: 1, dict: 2, bool: 3, int: 4 ,float: 5, str: 6}
# sorted_data = sorted(data, key=lambda d: types.get(type(d)))
# print(sorted_data)

# def max_sum_between_two_negatives(arr):
#     m = []
#     n = []
#     count = 0
#     s = 0
#     for i in arr:
#         if i < 0:
#             m.append(i)
#             count = 0
#             s = 0
#         else:
#             count += 1
#             if count >= 1:
#                 s += i
#                 n.append(s)
#     if len(m) == 1:
#         return -1
#     elif len(n) == 1:
#         return 0
#     return max(n)
# print(max_sum_between_two_negatives([8, 0, 5, 2, -9, 5, -6, -9, 4, -5]))
# students = {
#     'Azer Hasanov': {
#         'class': '7B',
#         'gpa': 90,
#         'best-at subject': 'math'    
#     },
#     'Rena Agayeva': {
#         'class': '9B',
#         'gpa': 82,
#         'best-at subject': 'literature'     
#     },
#     'Amir Ehmedov': {
#         'class': '7A',
#         'gpa': 84,
#         'best-at subject': 'biology'     
#     },
#     'Guler Hasanova': {
#         'class': '9C',
#         'gpa': 95,
#         'best-at subject': 'math'     
#     },
#     'Azerin Qasimova': {
#         'class': '11B',
#         'gpa': 81,
#         'best-at subject': 'chemistry'    
#     },
#     'Sema Agayeva': {
#         'class': '11C',
#         'gpa': 90,
#         'best-at subject': 'chemistry'     
#     },
#     'Amina Alili': {
#         'class': '10B',
#         'gpa': 84,
#         'best-at subject': 'math'     
#     },
#     'Gulnar Huseynova': {
#         'class': '8C',
#         'gpa': 90,
#         'best-at subject': 'history'     
#     },
#     'Afaq Azimova': {
#         'class': '10B',
#         'gpa': 84,
#         'best-at subject': 'literature'     
#     },
#     'Sima Amirli': {
#         'class': '8C',
#         'gpa': 83,
#         'best-at subject': 'sport'     
#     }
# }
# 1) Verilmiş dict-dən riyaziyyat üzrə daha yaxşı olan tələbələrdən ibarət və;
# gpa göstəricisinə əsasən sıralanmış list əldə edin;

# math_students = tuple(filter(lambda x: students[x]['best-at subject'] == 'math', students))
# math_students_sorted = sorted(math_students, key=lambda x: students[x]['gpa'])

# math_students_gpa = tuple(map(lambda x: students[x]['gpa'], math_students))

# math_students_name_gpa = tuple(zip(math_students, math_students_gpa))

# # 2) Bu il məzun olacaq şagirdlərdən ibarət list əldə edin;
# graduatio_students = list(filter(lambda x: students[x]['class'][:-1] == '11',students))
# print(graduatio_students)
# # 3) Gpa göstəricisi ən yüksək olan 8-ci sinif şagirdini tapın;
# students_of_8 = tuple(filter(lambda x: students[x]['class'].startswith('8'),students))
# best_of_8 = max(students_of_8,key=lambda x: students[x]['gpa'])
# print(best_of_8)
# # 4) Gpa göstəricisi ən az 90 olan şagirdlərin siyahısını əldə edin.
# students_w_high_gpa = list(filter(lambda x: students[x]['gpa'] >= 90,students))
# print(students_w_high_gpa)


# def divisors(n):
#     c = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             c += 1
#     return c
# print(divisors(6))


# def next_letter(s):
#     replacement = ''
#     for i in s:
#         if not i.isalpha():
#             replacement += i
#         elif i == 'z' or i == 'Z':
#             replacement += chr(ord(i) - 25)
#         elif i.isalpha():
#             replacement += chr(ord(i) + 1)
#     return replacement



# def max_sum_between_two_negatives(arr): 
#     only_one_negative = list(filter(lambda x: x < 0, arr)) 
#     all_pos = all((map(lambda x: x >= 0, arr))) 
#     if len(only_one_negative) == 1 or all_pos: 
#         return -1 
#     for i in range(len(arr)): 
#         if arr[i] < 0: 
#             arr = arr[i:] 
#             break 
#     count = 0 
#     result = [] 
#     for i in range(len(arr)): 
#         if arr[i] >= 0:
#             count += arr[i] 
#         else: 
#             result.append(count) 
#             count = 0 
#             continue 
#     return max(result)
# print(max_sum_between_two_negatives([-1,6,-2,3,5,-7]))



# numbers = [2, 0, 56, 1, 12, 87, 7]

# def my_sort (iterable):
#     sorting_done = True
#     counter = 0
    
#     while True:
#         first = iterable[counter]
#         second = iterable[counter+1]
        
#         if second < first:
#             iterable[counter] = second
#             iterable[counter+1] = first
#             sorting_done = False

#         if counter == len(iterable) - 2:
#             # print(iterable)
#             if sorting_done:
#                 return iterable
#             else:
#                 print(iterable)
#                 counter = 0
#                 sorting_done = True
#                 continue
#         counter += 1
        
# print(my_sort(numbers)) 

# def sort_my_string(s):
#     result1 = ''
#     result2 = ''
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result1 += s[i]
#         else:
#             result2 += s[i]
#     return result1 + ' ' + result2
# print(sort_my_string("CodeWars")) 




# def bubble_sort(items):
#     for i in range(len(items)):
#         for j in range(len(items)-1-i):
#             if items[j] > items[j+1]:
#                 items[j], items[j+1] = items[j+1], items[j]
#     return items

# items = [6,20,8,19,56,23,87,41,49,53]
# print(bubble_sort(items))


# a = {1, 14, 16, 4, 5, 15, 6}
# b = {6, 5, 15, 7, 11, 10, 9, 8}
# x = [6, 25, 1]
# print(a.intersection(b))
