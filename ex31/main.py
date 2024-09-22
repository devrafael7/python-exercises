import openpyxl
import random

book = openpyxl.load_workbook('my_file.xlsx')
main_page = book.active


unique_id  = set()
for i in range(10):
    
    while True:
        product_id = f"PD-{random.randint(1000, 10000)}"
        if product_id not in unique_id:
            unique_id.add(product_id)
            break
    
    main_page.append([product_id])
    
book.save('my_file.xlsx')