# Verilmiş dictionary-dən aşağıdakı list-i yaradın.
d = {'toddler_age': '1-5', 'kid_age': '5-13', 'teen_age': '13-17', 'young_age': '17-30', 'adult_age': '30+'}
# [['toddler_age', (1, 5)], ['kid_age', (5, 13)], ['teen_age', (13, 17)], 
#  ['young_age', (17, 30)], ['adult_age', (30, 'and more')]]
# l = []
# for k, v in age_categories.items():
#     age_range = []
#     if v.endswith('+'):
#         age_range.append(v.strip('+'))
#         age_range.append('and more')
#         age_range = tuple(age_range)

#         l.append(k)
#         l.append(age_range)

#     else:
#         age_range.append(int(v.split('-')[0]))
#         age_range.append(int(v.split('-')[1]))
#         age_range = tuple(age_range)

#         l.append(k)
#         l.append(age_range)
# print(l)


abreviatura = 'AMEAM'
words = ['Azerbyacan','Milli','Elmler','Akademiyasi', 'Mezunlari']

# Result -> {'A': 'Azerbyacan', 'M': 'Milli', 'E': 'Elmler', 'A(2)': 'Akademiyasi', 'M(2)': 'Mezunlari'}
"""1st solution"""
# ordered_dict = dict()

# for letter in abreviatura:
#     for word in words:
#         if word.startswith(letter) and letter not in ordered_dict:
#             ordered_dict[letter] = word
#             break
#         elif word.startswith(letter) and letter in ordered_dict:
#             key = letter + '(2)'
#             ordered_dict[key] = word
# print(ordered_dict)
""""""
"""Dynamic solution"""
# def get_count (words, letters):
#     count_letters = {}
#     for letter in letters:
#         counter = 0
#         for word in words:
#             if word.startswith(letter):
#                 counter += 1
#         if letter not in count_letters:
#             count_letters[letter] = counter
#     return count_letters
                
# ordered_dict = dict()

# for letter in abreviatura:
#     for word in words:
#         if word.startswith(letter) and letter not in ordered_dict:
#             ordered_dict[letter] = word
#             break
#         elif word.startswith(letter) and letter in ordered_dict:
#             counter = 0
#             counter_dict = get_count(words, abreviatura)
#             for k, v in counter_dict.items():
#                 key = letter + str(counter_dict[letter]+counter)
#                 ordered_dict[key] = word
# print(ordered_dict)


"""
*       *                                                                                                   
*       *                                                                                                   
* *   * *                                                                                                   
*   *   *                                                                                                   
*       *                                                                                                   
*       *                                                                                                   
*       *
"""

# pattern = ''

# for row in range(0, 7):
#     for col in range(0, 5):
#         if col == 0 or col == 4 or (row == 2 and (col == 1 or col == 3)) or (row == 3 and col == 2):
#             pattern += '* '
#         else:
#             pattern += '  '
#     pattern += '\n'
# print(pattern)