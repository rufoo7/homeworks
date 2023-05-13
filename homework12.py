# Dictionary datalarını düzləşdirən bir recursive funksiya hazırlayın. Örnək:
# letdict = {'a': 1, 'v': {'b': 2}, 'c': {'f': 3, 'c': 3, 'h': {'r': 5}, 'p': 3}, 'y': 9} 
# output: {'a': 1, 'b': 2, 'f': 3, 'c': 3, 'r': 5, 'p': 3, 'y': 9}


europe = {
    'Germany': {
        'capital': 'Berlin',
        'minimum wage per year': 23_712,
        'social welfare': 70,
        'developed': True      
    },
    'Norway': {
        'capital': 'Oslo',
        'minimum wage per year': 30_531,
        'social welfare': 80,
        'developed': True      
    },
    'Albania': {
        'capital': 'Tirana',
        'minimum wage per year': 4_176,
        'social welfare': 45,
        'developed': False      
    },
    'Moldova': {
        'capital': 'Kishinev',
        'minimum wage per year': 4_800,
        'social welfare': 40,
        'developed': False      
    },
    'Austria': {
        'capital': 'Vienna ',
        'minimum wage per year': 30_550,
        'social welfare': 72,
        'developed': False      
    }        
}
asia_europe = {
    'Azerbaijan': {
        'capital': 'Baku',
        'minimum wage per year': 2_280,
        'social welfare': 20,
        'developed': False      
    },
    'Armenia': {
        'capital': 'Yerevan',
        'minimum wage per year': 3_036,
        'social welfare': 18,
        'developed': False      
    },
    'Georgia': {
        'capital': 'Tbilisi',
        'minimum wage per year': 5_208,
        'social welfare': 30,
        'developed': False      
    },
    'Kazakhstan': {
        'capital': 'Astana',
        'minimum wage per year': 1_728,
        'social welfare': 20,
        'developed': False      
    },
    'Turkey': {
        'capital': 'Ankara ',
        'minimum wage per year': 5_868,
        'social welfare': 33,
        'developed': False      
    }        
}

europe.update(asia_europe)
def a (location):
    developed1 = []
    undeveloped1 = []
    for k,v in location.items():
        for i,j in v.items():
            if j == True:
                developed1.append(k)
            elif j == False:
                undeveloped1.append(k)
    return developed1,undeveloped1
print(a(europe))

    
