amount_of_goods = int(input("Введите количества товара которое хотите добавить: "))
number_of_goods = 1
product_price = []
product_analysis = {}
name_of_goods_for_analysis = []
price_of_goods_for_analysis = []
quantity_of_goods_for_analysis = []
unit_of_goods_for_analysis = []

for i in range(amount_of_goods):
    template_product = {}

    name_of_goods = input("Введите наименование товара: ")
    template_product["Наименование"] = name_of_goods
    name_of_goods_for_analysis.append(name_of_goods)
    product_analysis["Наименование"] = name_of_goods_for_analysis

    price_of_goods = int(input(f"Введите стоимость товара '{name_of_goods}' в рублях: "))
    template_product["Цена"] = price_of_goods
    price_of_goods_for_analysis.append(price_of_goods)
    product_analysis["Цена"] = price_of_goods_for_analysis

    quantity_of_goods = int(input(f"Введите количество товара '{name_of_goods}': "))
    template_product["Количество"] = quantity_of_goods
    quantity_of_goods_for_analysis.append(quantity_of_goods)
    product_analysis["Количество"] = quantity_of_goods_for_analysis

    unit_of_goods = input(f"Введите единицу измерения товара '{name_of_goods}' (шт., ед., м.п. и тд.): ")
    template_product["Ед."] = unit_of_goods
    if unit_of_goods_for_analysis.count(unit_of_goods) == 0:
        unit_of_goods_for_analysis.append(unit_of_goods)
    product_analysis["Ед."] = unit_of_goods_for_analysis

    product_price.append((number_of_goods, template_product))
    number_of_goods += 1

for i in product_price:
    print(i)

print(product_analysis)

