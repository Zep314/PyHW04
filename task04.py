# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import *

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

# Степень многочлена
k = 5
#seed(4)
polynom = [randint(-9,10) for _ in range(k+1)]

print(polynom)
print(my_pretty_print(polynom))
with open("task04.txt","w") as f:
    f.write(my_pretty_print(polynom))