class OfficeEquipmentWarehouse:
    equipment_warehouse = {}
    equipment_to_unit = {}


class OfficeEquipment:
    def __init__(self, manufacturer, model, date):
        self.manufacturer = manufacturer
        self.model = model
        self.date = date

    @staticmethod
    def warehouse_reception(param, quantity):
        OfficeEquipmentWarehouse.equipment_warehouse[f"{param.manufacturer} {param.model}"] = \
            {"Manufacturer": param.manufacturer, "Model": param.model, "Year": param.date, "Quantity": quantity}

    @staticmethod
    def warehouse_unit(name_model, quantity, unit):
        remains_equipment = (OfficeEquipmentWarehouse.equipment_warehouse[name_model])
        request_for_equipment = int(remains_equipment["Quantity"])
        if request_for_equipment < quantity:
            print("На складе недостасточное количество техники")
        else:
            remains_equipment["Quantity"] = request_for_equipment - quantity
            OfficeEquipmentWarehouse.equipment_to_unit[unit] = OfficeEquipmentWarehouse.equipment_warehouse[name_model]
            OfficeEquipmentWarehouse.equipment_to_unit[unit]["Quantity"] = quantity
            if (request_for_equipment - quantity) == 0:
                OfficeEquipmentWarehouse.equipment_warehouse.pop(name_model)


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, date, paper_format):
        super().__init__(manufacturer, model, date)
        self.paper_format = paper_format


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, date, color=True):
        super().__init__(manufacturer, model, date)
        self.color = color


class Xerox(OfficeEquipment):
    def __init__(self, manufacturer, model, date, speed):
        super().__init__(manufacturer, model, date)
        self.speed = speed


def print_warehouse(param):
    print("\nОстатки техники на складе:")
    for i in param:
        print(f"{i} - {param[i]}")


def print_unit(param):
    print("\nОргтехника в подраздеениях:")
    for i in param:
        print(f"{i} - {param[i]}")


printer_1 = Printer("HP", "ZT-435", 2017, "A4")
print(printer_1.paper_format)

scanner_1 = Scanner("Samsung", "FF-43", 2019, True)
print(scanner_1.color)

xerox_1 = Xerox("Samsung", "X-34", 2019, 200)
print(xerox_1.speed)

OfficeEquipment.warehouse_reception(printer_1, 2)
OfficeEquipment.warehouse_reception(scanner_1, 3)
OfficeEquipment.warehouse_reception(xerox_1, 7)

print_warehouse(OfficeEquipmentWarehouse.equipment_warehouse)
OfficeEquipment.warehouse_unit("HP ZT-435", 2, "Sells")

print_unit(OfficeEquipmentWarehouse.equipment_to_unit)
print_warehouse(OfficeEquipmentWarehouse.equipment_warehouse)
