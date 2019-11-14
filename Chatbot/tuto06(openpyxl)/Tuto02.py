# -*- coding: utf-8 -*-
"""

@author: Tommy
"""

from openpyxl import load_workbook


def got_drink(item_dict, item):
    item_dict[item] -= 1
    return 0


EXCEL_FILE_NAME = 'Database.xlsx'
db = load_workbook(filename=EXCEL_FILE_NAME)
machine_db = db['자판기']

item_dict = {}

for row in machine_db.rows:
    if row[0].value is not None:
        item_dict[row[0].value] = row[1].value

got_drink(item_dict, '사이다')
got_drink(item_dict, '콜라')

# 딕셔너리의 Key 값을 읽기
print(item_dict.keys())
# 딕셔너리의 Value 값을 읽기
print(item_dict.values())
# 딕셔너리의 Key, Value Pair 로 읽기
print(item_dict.items())

