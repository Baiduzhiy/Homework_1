class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def split(cls, date):
        date_list = date.split(".")
        for i in range(0, 3):
            date_list[i] = int(date_list[i])
        print(date_list)

    @staticmethod
    def validation(date):
        try:
            date_list = date.split(".")
            for i in range(0, 3):
                date_list[i] = int(date_list[i])
        except ValueError:
            print("Вы ошиблись в указании даты!")


date_now = Date("27.04.2020")
print(date_now.date)
Date.split("27.04.2020")
Date.validation("e7.04.2020")
date_now.validation("27.04.2020")
