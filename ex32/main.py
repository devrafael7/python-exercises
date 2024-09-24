import openpyxl

excel_file = openpyxl.load_workbook('my_file.xlsx')
first_page = excel_file.active


data_client = input("what do you want to search? ")

product = []
for each_row in first_page.iter_rows(min_row=2, values_only=True):
    product_found = False
    for cell in each_row:
        if data_client.lower() == str(cell).lower():
            product_found = True
            break
    
    if product_found:
        product.append(each_row)

for each_product in product:
    print(each_product)