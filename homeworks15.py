# Bu kodda baş verə biləcək errorları araşdırıb, onları handle edin
# Əgər istifadəçi 10-dan artıq və ya 3-dən az 
# heyvan giribsə internetdən istədiyiniz bir erroru taparaq təyin edin. 
# animals = input('Heyvanlari girin: ').split(', ')
# try:
#     if not 3 < len(animals) < 10:
#         raise Exception('Heyvan sayi duzgun daxil edilmemisdir. ')
#     prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }
#     print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))
# except KeyError as message:
#     print('Siyahida olmayan heyvan adi daxil etmisiniz', "xeta kodu {messsage}".format)


# numbers = [str(i).zfill(4) + '\n' for i in range(1000,0,-1)]
# with open('text.txt', encoding = 'UTF-8',mode= 'w') as file:
#     file.writelines(numbers)

# with open('text.txt', encoding='UTF-8', mode='r') as file:
#     read_content = file.read()
#     read_content = read_content.split('\n')  
#     read_content.sort(key= lambda x: x.split()[2], reverse= True)
# with open('text.txt', encoding='UTF-8', mode='w') as file:
#     read_content = '\n'.join(read_content)
#     file.write(read_content)

# 1.  "article.txt" faylındakı məqalə dərc olunmağa hazır deyil. Hazır olması üçün:
#     1. "artists.txt" faylındakı mətni "article.txt" faylına append etməli
#     2. "article-part.txt" faylındakı mətni "article.txt"-ə 3-cü sətri olaraq əlavə etməli
#     3. Mətnin sonuna aşaöıdakı kimi əlavə etməlisiniz:
#     Açar sözlər: #İntibahDövrü #AvropaMədəniyyəti #RenesansArtistləri #Mikelancelo #Botiçelli

# with open('artists.txt', encoding='UTF-8', mode='r') as file:
#     artists = file.read()
#     # print(artists)
# # with open("article.txt", mode='a+', encoding='UTF-8') as file:
# #     file.write(artists)
# # result = open("article.txt", encoding='UTF-8')
# # print(result.read)
# with open('article-part.txt', encoding='Utf-8') as file:
#     article_part = file.read()
#     # print(article_part) 
# with open("article.txt", mode='r', encoding='UTF-8') as file:
#     file.seek(0)
#     content = file.read()
#     # print(content)
#     content = content.splitlines()
#     content[3] = article_part
#     content = '\n'.join(content)
#     print(content)
# with open("article.txt", mode='w', encoding='UTF-8') as file:
#     file.write(content)
    
key_words = ['İntibahDövrü', 'AvropaMədəniyyəti', 'RenesansArtistləri', 'Mikelancelo', 'Botiçelli']
key_words_2 = []
for i in key_words:
    key_words_2.append('#'+ i)
print(key_words_2)
with open("article.txt", mode='w', encoding='UTF-8') as file:
    file.seek(0)
    for j in key_words_2:
        file.write(j)