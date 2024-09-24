import openpyxl
import random
import products
from datetime import datetime, timedelta

book = openpyxl.load_workbook('my_file.xlsx')
main_page = book.active


unique_id  = set()

def random_time():
    hour = random.randint(1, 23)
    minute = random.randint(1, 59)
    second = random.randint(1, 59)
    return f"{hour:02d}:{minute:02d}:{second:02d}"

yesterday = datetime.now() - timedelta(days=1)

for i in range(2000):
    
    ##while True:
    ##    product_id = f"PD-{random.randint(1000, 10000)}"
    ##    if product_id not in unique_id:
    ##        unique_id.add(product_id)
    ##        break
        
    allProducts = random.choice(products.products_with_id)
    teams = f"Equipe {random.randint(1, 20)}"
    qnt_produced = random.randint(15, 500)
    time = random_time()
    date = yesterday.strftime("%d/%m/%Y")
    main_page.append([allProducts, teams, qnt_produced, time, date])
    
book.save('my_file.xlsx')