n = int(input("miqdari daxil edin"))
if n<2000 :
    print("kredit verilmir")
elif n<10000:
    print("sizin yekun borcunuz", n*1.05)
elif n<50000:
    print("sizin yekun borcunuz", n*1.04)
elif n<200000:
    print("sizin yekun borcunuz", n*1.03)
elif n<500000:
    print("sizin yekun borcunuz", n*1.02)
elif n>500000:
    print("kredit verilmir")
    
    
    n=int(input("ededi daxil edin:"))
if n%3==0 and n%7==0 and n%8==0:
    print("her ucune de bolunur")
else:
    print("bolunmur")