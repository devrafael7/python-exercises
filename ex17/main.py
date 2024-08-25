import openpyxl
import random
from datetime import datetime, timedelta

book = openpyxl.Workbook()
book.create_sheet('Info')

info_page = book['Info']
info_page.append(['Purchaser', 'Gender', 'Location', 'Product', 'Product ID', 'Price', 'Discount', 'Quantity Sold', 'Date', 'Time', 'Order ID', 'Stock Level', 'Quantity Returns'])

names = ['Rafael', 'Lucas', 'Rodrigo', 'Sthefany', 'Rafaela', 'Cristiane', 
         'Fernanda', 'Patricia', 'Luis', 'João', 'Maria', 'Pedro', 'Ana', 
         'Carlos', 'Clara', 'Gabriel', 'Sofia', 'Leonardo', 'Julia', 'Felipe',
         'Amanda', 'Gustavo', 'Beatriz', 'Bruno', 'Mariana', 'Thiago', 
         'Vitória', 'Vinicius', 'Larissa', 'Caio', 'Manuela', 'Ricardo', 
         'Lorena', 'Daniel', 'Helena', 'Arthur', 'Camila', 'Eduardo', 'Bianca']

gender = ['Male', 'Female']

locations = ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Salvador', 'Curitiba']

products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Headphones', 'Keyboard', 
            'Mouse', 'Printer', 'Camera', 'Smartwatch', 'Router', 'Speaker', 
            'Charger', 'SSD', 'External Hard Drive', 'USB Drive', 'Microphone', 
            'Webcam', 'Drone', 'Projector']

def random_date(start_year = 2020, end_year = 2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_time():
    hours = random.randint(1, 23)
    minutes = random.randint(1, 59)
    seconds = random.randint(1, 59)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

unique_order_ids = set()

for i in range(500):
    purchaser_name = random.choice(names)
    products_name = random.choice(products)
    gender_type = random.choice(gender)
    locations_name = random.choice(locations)
    product_id = i + 1
    product_price = round(random.uniform(100, 1000), 2)
    discountAccount = product_price * 0.08
    discount = round(product_price - discountAccount, 2)
    quantity_sold = random.randint(100, 10000)
    date = random_date().strftime('%Y, %m, %d')
    time = random_time()
    stock_level = random.randint(100, 10000)
    quantity_returns = random.randint(5, 90)
    
    while True:
        order_id = f"ORD-{random.randint(10000, 99999)}"
        if order_id not in unique_order_ids:
            unique_order_ids.add(order_id)
            break
    info_page.append([purchaser_name, gender_type, locations_name, products_name, product_id, product_price, discount, quantity_sold, date, time, order_id, stock_level, quantity_returns])
    
book.save('info.xlsx')


