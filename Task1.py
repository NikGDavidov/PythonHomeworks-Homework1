#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#- 6 -> да
#- 7 -> да
#- 1 -> нет
txt = ""
day_num=0
while True:
    day_num =int(input())
    if day_num>0 and day_num <8 :
        break
if day_num<6 :
    txt = "нет" 
else :
    txt ="да"
print (f"{day_num} -> {txt}")