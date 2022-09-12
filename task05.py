# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def my_pretty_print(poly): # красиво переводим полином в строку по всем правилам
    ret = ""
    for i in range(len(poly)-1,-1,-1): # идем по списку в обратном направлении
        if poly[i]!=0:                 # нулевые коэффициенты не обрабатываем
            ret += "+" if poly[i] > 0 else "-"  # знаки выводим отдельно
            if (abs(poly[i])!=1) or (i==0):     # печатаем коэффициент, если не 1. Последний коэффициент выводим всегда
                ret += f"{abs(poly[i])}"        # без знака
            if (abs(poly[i])!=1) and (i>0): ret += "*"  # выводим знак * (если степень>0)
            if i>0: ret += "x"
            if i>1: ret += f"^{i}"
    return ret[1:] if (ret[0:1] == "+") else ret  # убираем самый первый + если он есть

def my_parse_poly(s):
    ret = []
    s = s.replace("-","+-")
    if s[0:1] == "+": s = s[1:]
    ret = s.split("+")

    print(s)
    return ret

with open("task05_1.txt","r") as f:
    str1 = f.read()

with open("task05_2.txt","r") as f:
    str2 = f.read()

print("Прочитано из файлов:")
print(str1)
print(str2)
print()
poly1 =my_parse_poly(str1)
#poly2 =my_parse_poly(str2)
# print("Коэффициенты полиномов:")
print(poly1)
#print(poly2)
