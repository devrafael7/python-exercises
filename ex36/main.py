names_db = []

def name_verification(name):
    if name not in names_db:
        names_db.append(name)
        print(f'{name} was added to the db of names successfully.')
    else:
        print('This name is already in the db of names.')

name = input('Type your name: ')
name_verification(name)



        