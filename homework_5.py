profit = int(input("Приветствую Вас! Введите пожалуйста прибыль своей организации: "))
cost = int(input("А теперь введите издержки фирмы: "))

if profit < cost:
    print("Вы работаете в убыток. Издержки больше выручки!")
else:
    income = profit - cost
    print("Вы Получили прибыль! Ваша выручка больше издержек и она составила %.2f руб." % income)
    personal = int(input("Введите количество Вашего персонала: "))
    income_personal = income / personal
    print("Ваша выручка в расчете на одного сотрудника составила %.2f руб." % income_personal)
    