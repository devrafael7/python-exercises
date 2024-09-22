import random

products = [
    f'Laptop.{random.randint(100, 2000)}',
    f'Smartphone.{random.randint(100, 2000)}',
    f'Tablet.{random.randint(100, 2000)}',
    f'Monitor.{random.randint(100, 2000)}',
    f'Headphones.{random.randint(100, 2000)}',
    f'Keyboard.{random.randint(100, 2000)}',

    f'Mouse.{random.randint(100, 2000)}',
    f'Printer.{random.randint(100, 2000)}',
    f'Camera.{random.randint(100, 2000)}',
    f'Smartwatch.{random.randint(100, 2000)}',
    f'Router.{random.randint(100, 2000)}',
    f'Speaker.{random.randint(100, 2000)}',
    
    f'Charger.{random.randint(100, 2000)}',
    f'SSD.{random.randint(100, 2000)}',
    f'External Hard Drive.{random.randint(100, 2000)}',
    f'USB Drive.{random.randint(100, 2000)}',
    f'Microphone.{random.randint(100, 2000)}',

    f'Webcam.{random.randint(100, 2000)}',
    f'Drone.{random.randint(100, 2000)}',
    f'Projector.{random.randint(100, 2000)}'
]

products_with_id = [f'PD-{i+1}.{product}' for i, product in enumerate(products)]






    