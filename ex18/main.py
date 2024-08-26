import openpyxl
import random
from datetime import datetime, timedelta

book = openpyxl.Workbook()
book.create_sheet('Info')

info_page = book['Info']

info_page.append(['Purhcaser', 'Gender', 'Location', 'Product', 'Product ID', 'Price', 'Price With Discount', 'Quantity Sold', 'Date', 'Time', 'Order ID', 'Stock Level', 'Returns'])

purchaser_names = ['Michael', 'Jessica', 'Christopher', 'Emily', 'Matthew', 'Ashley', 'Joshua', 'Sarah', 'Daniel', 'Amanda', 'David', 'Brittany', 'James', 'Samantha', 'John', 'Elizabeth', 'Joseph', 'Taylor', 'Andrew', 'Megan', 'Ryan', 'Hannah', 'Brandon', 'Lauren', 'Jason', 'Kayla', 'Justin', 'Amber', 'Robert', 'Rachel', 'Nicholas', 'Alexis', 'Jacob', 'Nicole', 'Tyler', 'Rebecca', 'Kevin', 'Michelle', 'Eric', 'Stephanie', 'Kyle', 'Jennifer', 'Brian', 'Courtney', 'William', 'Melissa', 'Zachary', 'Kaitlyn', 'Ethan', 'Alyssa', 'Nathan', 'Victoria', 'Adam', 'Morgan', 'Christian', 'Brianna', 'Jonathan', 'Savannah', 'Dylan', 'Chloe'
]

gender = ['Male', 'Female']

location = ['Statue of Liberty', 'Grand Canyon', 'Yellowstone National Park', 'Times Square', 'Golden Gate Bridge', 'Hollywood', 'Empire State Building', 'Las Vegas Strip', 'Central Park', 'Mount Rushmore', 'Disney World', 'Niagara Falls', 'The White House', 'Brooklyn Bridge', 'Yosemite National Park', 'Universal Studios', 'Space Needle', 'The Pentagon', 'Hollywood Walk of Fame', 'Miami Beach'
]

products = ['Table', 'Chair', 'Pen', 'Notebook', 'Phone', 'Computer', 'Bottle', 'Cup', 'Glass', 'Car', 'Lamp', 'Desk', 'Keyboard', 'Mouse', 'Book', 'Television', 'Remote', 'Watch', 'Shoe', 'Bag', 'Backpack', 'Pillow', 'Blanket', 'Towel', 'Mirror', 'Door', 'Window', 'Spoon', 'Fork', 'Knife', 'Plate', 'Camera', 'Headphones', 'Speaker', 'Wallet', 'Umbrella', 'Hat', 'Glasses', 'Bicycle', 'Ball', 'Bed', 'Fan', 'Rug', 'Sofa', 'Curtain', 'Stove', 'Oven', 'Refrigerator', 'Microwave', 'Toaster', 'Brush', 'Comb', 'Pencil', 'Eraser', 'Paper', 'Scissors', 'Clock', 'Calendar', 'Bag', 'Charger'
]

def random_date(start_year=2018, end_year=2024):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

def random_time():
    hours = random.randint(0, 23)
    minutes = random.randint(1, 59)
    seconds = random.randint(1, 59)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

unique_id = set()

for i in range(10000):
    names = random.choice(purchaser_names)
    genders = random.choice(gender)
    
    locations = random.choice(location) 
    all_products = random.choice(products)
    product_id = i + 1
    prices = round(random.randint(80, 800), 2)
    
    apply_discount = random.choice([True, False])
    if apply_discount:
        discount_account = prices * 0.08
        discount = round(prices - discount_account,2)
    else:
        discount = None
        
    quantity_sold = random.randint(20000, 100000)
    sale_date = random_date().strftime('%Y, %m, %d')
    sale_time = random_time() 
        
    while True:
        order_id = f"ORD-{random.randint(10000, 99999)}"
        if order_id not in unique_id:
            unique_id.add(order_id)
        break
    
    stock_level = random.randint(1000, 10000)
    returns = random.randint(5000, 20000)
     
    info_page.append([names, genders, locations, all_products, product_id, prices, discount, quantity_sold, sale_date, sale_time, order_id, stock_level, returns])
    
book.save('sales_2018_2024.xlsx')

    