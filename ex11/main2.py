import openpyxl

book = openpyxl.load_workbook('shopping-spreadsheet.xlsx')

fruits_page = book['fruits']

for rows in fruits_page.iter_rows(min_row=2,max_row=5):
    for cell in rows:
        if cell.value == 'banana':
            cell.value = 'fruit 1'
        ##if cell.value is not None:
        ##    print(cell.value)
        
book.save('shopping-spreadsheet.xlsx')
        
