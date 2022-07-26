'''
Модуль включает в себя переменные разных типов. На выводе печатается название переменной, ее значение и тип.
Реализация несколько корявая, но все же...
'''

# словарь с типами данных и какие поля к ним относятся
description = {'INTs': ['id_EAN14'],
               'FLOATs': ['min_place', 'min_weight'],
               'STRs': ['bestbefore', 'name', 'provider', 'provider_country', 'veg_type'],
               'BOOLs': ['is_chestnyznak', 'is_EGAIS', 'is_instock', 'is_piece'],
               'LISTs': ['purpose']}

# переменные типа INT
id_EAN14 = 1845678901001    # штрихкод товара в системе EAN14

# переменные типа FLOAT
min_place = 0.02    # размер одного знимаемого места в м3
min_weight = 1.5    # вес минимальной единицы в килограммах

# переменные типа STR
bestbefore = '03/08/2022'   # срок годности
name = 'картофель'  # наименование овоща
provider = 'АО КОРМИЛЕЦ'    # наименование поставщика, тип str
provider_country = 'Россия'    # страна происхождения поставщика, тип str
veg_type = 'Корнеплоды'    # тип овоща


# переменные типа BOOL
is_chestnyznak = True   # учет в системе "Честный знак" - TRUE, без учета - FALSE
is_EGAIS = False    # учет в ЕГАИС - TRUE, без учета - FALSE
is_instock = True   # в наличии - TRUE, отсутствует - FALSE
is_piece = False    # штучный товар - TRUE, весовой - FALSE

# переменные типа LIST
purpose = ['для варки', 'для жарки', 'для фритюра']    # подходящие способы приготовления

# собираем все значения словаря в список
variables_list = []
for k in description.values():
    for i in k:
        variables_list.append(i)

# сортируем полученный список по алфавиту
variables_list = sorted(variables_list)

# кортеж со всеми переменными для более простого кода печати
variables = (bestbefore, id_EAN14, is_EGAIS, is_chestnyznak, is_instock, is_piece, min_place, min_weight, name,
             provider, provider_country, purpose, veg_type)

# печатаем значения
print('НАЗВАНИЕ ПЕРЕМЕННОЙ', 'ЗНАЧЕНИЕ ПЕРЕМЕННОЙ', 'ТИП ПЕРЕМЕННОЙ', sep=' ---> ')
for i in range(len(variables)):
    print(variables_list[i], variables[i], type(variables[i]), sep=' ---> ')
