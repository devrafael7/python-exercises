import openpyxl
import random
from datetime import datetime, timedelta

book = openpyxl.Workbook()

book.create_sheet('Info')
infoPage = book['Info']

infoPage.append(['ID', 'Purchaser', 'Product', 'Quantity Sold', 'Price', 'Date', 'Time', 'Order ID'])

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

def randomDate(startYear = 2023, endYear = 2024):
    startDate = datetime(startYear, 1, 1)
    endDate = datetime(endYear, 12, 31)
    delta = endDate - startDate
    randomDays = random.randint(0, delta.days)
    return startDate + timedelta(days=randomDays)

def randomTime():
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    seconds = random.randint(0, 59)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

for i in range(40):
    productID = i + 1
    randonName = random.choice(names)
    randomProduct = random.choice(products)
    
    quantitySold = random.randint(1, 300)
    price = round(random.uniform(10, 1000),2)
    saleDate = randomDate().strftime('%Y-%m-%d')
    
    saleTime = randomTime()
    orderID = f"ORD-{random.randint(10000, 99999)}"
    
    infoPage.append([productID, randonName, randomProduct, quantitySold, price, saleDate, saleTime, orderID])

book.save('ex02.xlsx')
    






