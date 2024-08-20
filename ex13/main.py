import openpyxl
import info

book = openpyxl.Workbook()

book.create_sheet('User-info')

usersPage = book['User-info']

usersPage.append(['Name', 'Id', 'Password'])
usersPage.append([info.name, info.id, info.password])

book.save('Users-xl.xlsx')
