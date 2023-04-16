# bu listdən yeni bir dictionary hazırlayın. 
# Həmin dictionarynin keyləri ədədlər, valueləri isə mübət və ya mənfi yazılı stringlər olacaq.
# Ornək: {10: 'musbet', -21: 'menfi', ...}
# numbers = [58, 78, 96, 33, 25, 29, 12, 46]
# result = {n:('tek' if n%2 else 'cut') for n in numbers }
# print(result)

cumle = "sehvelerden en yaxsi sehife bu sehvedir"
l = ["sehve", "sehife"]
result = cumle.replace(*l)
# print(result)

userData = [
    {
        'debt': 12543,
        'paid': 341.346742,
        'paid_percent': 0.027214122777644904,
        'card_number': '5326-6644-1234-6432',
        'first_name': 'Akif',
        'last_name': 'Serifov',
        'father_name': 'Elekber',
    }
]
# Hormetli A. E. Serifov, sizin 5326-6644********** nomreli   kredit kartiniza 341.35AZN odenis edildi.  
# Umumi 12,543AZN teskil eden borcunuzdan 2.72% borc silinmisdir!
text = 'Hormetli {first_name:.1}. {father_name:.1}. {last_name}, sizin {card_number:*<19.9} nomreli   \
kredit kartiniza {paid:.2f}AZN odenis edildi. Umumi {debt:,}AZN teskil eden borcunuzdan {paid_percent:.2%} borc silinmisdir!'.format_map(userData[0])

print(text)