def evenOrOdd():
    number = input("enter a number: ")
    number = number.replace(",", ".")
    
    try:
        number = float(number)
        
        if number.is_integer():
            number = int(number)
            if number % 2 == 0:
                return f"{number} is even"
            else:
                return f"{number} is odd"
        else:
            return "enter an integer number please"
    except ValueError:
        return "invalid element. Please enter a number"
    
##print(evenOrOdd())

def calculator():
    number = int( input("enter a number: ") )
    number2 = int( input("enter a second number: ") )
    operator = input("choose the operator. + | - | * | /: ")
    
    if operator == "+":
        return f"the sum of numbers is equals: {number + number2}"
    elif operator == "-":
        return f"the subtraction of numbers is equals: {number - number2}"
    elif operator == "*":
        return f"the multiplication of number is equals: {number * number2}"
    elif operator == "/":
        return f"the division of number is equals: {number / number2}"
    else:
        return "choose one of those four options please"

##print(calculator())

def loop():
    
    for i in range (11):
        print(i)

##loop()

def fruitsIndex():
    fruits = ['apple', 'banana', 'cherry', 'strawberry', 'mango', 'grape']
    
    ##for i in range(len(fruits)):
    ##    print(fruits[i])
    
    for i in fruits:
        print(i)


##fruitsIndex()
        


    

        