import openpyxl
import xl_config
import data_collection

book = openpyxl.Workbook()

book.create_sheet('Objects')

objectsPage = book['Objects']

objectsPage.append(['Objects', 'Owner', 'Last name' , 'Price', 'Quantity'])
objectsPage.append(['Fork', 'Lucas', data_collection.LastName, '2,99', '8'])
objectsPage.append(['Chair', 'Patricia', data_collection.LastName, '5,20', '12'])
objectsPage.append(['Lamp', 'Rodrigo', data_collection.LastName, '2,99', '20'])
objectsPage.append(['Pillow', 'Fernanda', data_collection.LastName, '12,99', '9'])
objectsPage.append(['Pants', 'Cristiane', data_collection.LastName, '39,99', '15', 'Total'])
objectsPage.append(['Blanket', 'Luis', data_collection.LastName, '22,00', '20', xl_config.totalPrice])

book.save('objects-info.xlsx')


