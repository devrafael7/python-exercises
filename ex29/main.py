
def odd_or_even_number():
    try:
        number = int(input('enter a number: '))
        
        if number % 2 == 0:
            print('even number')
        else:
            print('odd number')
            
    except ValueError:
        print('invalid value! please enter a number')

##odd_or_even_number()

grades = []
grade_average_called = False
def grade_average():
    global grade_average_called
    grade_average_called = True
    for i in range(5):
        while True:
            try:
                grade = float(input(f'enter value {i + 1}: '))
                grades.append(grade)
                break
            
            except ValueError:
                print('Invalid value! Please enter a number.')
            
##grade_average()

if grade_average_called:
    n1, n2, n3, n4, n5 = grades
    average = sum(grades) / len(grades)
    print(f'the average is {average}')
