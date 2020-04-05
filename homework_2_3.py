season_list = [1, "Winter", 2, "Winter", 3, "Spring", 4, "Spring", 5, "Spring", 6, "Summer", 7, "Summer", 8, "Summer", 9, "Autumn", 10, "Autumn", 11, "Autumn", 12, "Winter"]
season_dict = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}

month = int(input("Please select a month and write its serial number (1-12): "))
b = 0

for i in season_list:
    if month == season_list[b]:
        print(season_list[b + 1])
    b += 1

print(season_dict[month])