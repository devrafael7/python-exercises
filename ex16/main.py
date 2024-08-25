import openpyxl
from datetime import datetime, timedelta
import random

book = openpyxl.Workbook()
book.create_sheet('Sales')

salesPage = book['Sales']
salesPage.append(['ID', 'Purchaser', 'Product', 'Price', 'Discount', 'Quantity Sold', 'Date', 'Time', 'Order ID'])

names = ['Rafael', 'Lucas', 'Rodrigo', 'Sthefany', 'Rafaela', 'Cristiane', 
         'Fernanda', 'Patricia', 'Luis', 'João', 'Maria', 'Pedro', 'Ana', 
         'Carlos', 'Clara', 'Gabriel', 'Sofia', 'Leonardo', 'Julia', 'Felipe',
         'Amanda', 'Gustavo', 'Beatriz', 'Bruno', 'Mariana', 'Thiago', 
         'Vitória', 'Vinicius', 'Larissa', 'Caio', 'Manuela', 'Ricardo', 
         'Lorena', 'Daniel', 'Helena', 'Arthur', 'Camila', 'Eduardo', 'Bianca']

products = ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Headphones', 'Keyboard', 
            'Mouse', 'Printer', 'Camera', 'Smartwatch', 'Router', 'Speaker', 
            'Charger', 'SSD', 'External Hard Drive', 'USB Drive', 'Microphone', 
            'Webcam', 'Drone', 'Projector']

def randomDate(startYear = 2020, endYear = 2024):
    startDate = datetime(startYear, 1, 1)
    endDate = datetime(endYear, 12, 31)
    delta = endDate - startDate
    randomDays = random.randint(0, delta.days)
    return startDate + timedelta(days=randomDays)

def randomTime():
    hours = random.randint(1, 23)
    minutes = random.randint(1, 59)
    seconds = random.randint(1, 59)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

for i in range(40):
    productsID = random.randint(1, 1000)
    randomName = random.choice(names)
    randomProduct = random.choice(products)
    
    quantitySold = random.randint(1, 1000)
    price = round(random.uniform(10, 500), 2)
    discountAccount = price * 0.08
    discount = round(price - discountAccount, 2)
    
    
    saleDate = randomDate().strftime('%Y,%m,%d')
    saleTime = randomTime()
    orderID = f"ORD-{random.randint(10000, 99999)}"
    
    salesPage.append([productsID, randomName, randomProduct, price, discount, quantitySold, saleDate, saleTime, orderID])
    
book.save('sales_py.xlsx')
    
    
    