km = int(input("Введите количество километров которое спортсмен пробежал в первый день: "))
finish = int(input("Введите количество километров которое спортсмен хочет пробегать за день: "))
days = 1

while km < finish:
    km = km * 1.10
    days += 1

print(f"На {days}-й день спортсмен достиг результата - не менее {finish} км.")