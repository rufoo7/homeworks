# İstifadəçi 3 fərqli inputda adını, soyadını və ata adını daxil edir. Onun adı proqramda
# ata adı böyük hərflərlə və ardından ad və soyadın
# baş hərfələrinin nöqtələrlə ayrılmış şəkildə qeyd olunmalıdır. 
# Örnək:
# Javier Bardem Pablo -> JAVIER B. P
name = input("Adinizi daxil edin :")
surname = input("Soyadinizi daxil edin :")
f_name = input("Ata adinizi daxil edin :")
full_name = f"{f_name.upper()} {name[0].upper()}. {surname[0].upper()}"
print(full_name)