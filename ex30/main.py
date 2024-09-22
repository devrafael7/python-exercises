import openpyxl

book = openpyxl.load_workbook('Estoque (1).xlsx')
main_page = book.active

first_row = []
for cell in main_page[1]:
    first_row.append(cell.value)

data = input('type something: ')

rows_found = []
for each_row in main_page.iter_rows(min_row=2, values_only=True):
    it_found = False
    for cell in each_row:
        if data in str(cell):
            it_found = True
            break
    if it_found:
        rows_found.append(each_row)
        
stock_quantity = 0
for cell in rows_found:
    stock_quantity += cell[4]

print(first_row)
print(rows_found)
print(stock_quantity)        