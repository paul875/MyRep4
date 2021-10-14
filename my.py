Ntickets=int(input("Введите количество билетов:"))
age = 0.0
Sum = 0.0
for i in range(Ntickets):
    age = float(input("Введите возраст посетителя:"))
    if age < 18.0:
        Sum += 0.0
    elif 18.0<=age<25.0:
        Sum+=990.0
    elif 25.0<=age:
        Sum+=1390.0
if Ntickets>3:
    Sum = Sum * 0.9
print("Сумма к оплате:",Sum)