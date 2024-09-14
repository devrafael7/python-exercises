##client_choose = input('choose one of these operators: + | - | * | /: ')
##client_choose_numbers0 = int(input('enter the first number: '))
##client_choose_numbers1 = int(input('enter the second number: '))
##
##if client_choose == '+':
##    calculator = client_choose_numbers0 + client_choose_numbers1
##elif client_choose == '-':
##    calculator = client_choose_numbers0 - client_choose_numbers1
##elif client_choose == '*':
##    calculator = client_choose_numbers0 * client_choose_numbers1
##elif client_choose == '/':
##    calculator = client_choose_numbers0 / client_choose_numbers1
##else:
##    print('choose one of these four operators')
##print(calculator)

##client_number = int(input('enter a number: '))
##if client_number % 2 == 0:
##    print('odd')
##else:
##    print('even')

##import openpyxl
##
##book = openpyxl.load_workbook('Estoque (1).xlsx')
##main_page = book.active
##
##first_row = []
##for celulas in main_page[1]:
##    first_row.append(celulas.value)
##    
##dados = input('digite: ')
##
##produtos = []
##for cada_linha in main_page.iter_rows(min_row=2, values_only=True):
##    encontrado = False
##    for celulas in cada_linha:
##        if dados in str(celulas):
##            encontrado = True
##            break
##    
##    if encontrado:
##        produtos.append(cada_linha)
##
##estoque_total = 0
##
##for quantidade in produtos:
##    estoque_total += quantidade[4]
##        
##    
##print(first_row)
##print(produtos)
##print(estoque_total)

##import geocoder
##
### Obter a localização atual pelo endereço IP
##localizacao = geocoder.ip('me')
##
##cidade = localizacao.city
##
### Imprimir a localização
##print(f"Sua localização atual é {cidade}")