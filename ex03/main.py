##name = input("type ur name: ")
##print("welcome, " + name + "!")

##def even_or_odd(n1):
##    if n1 % 2 == 0:
##        return "even number"
##    else:
##        return "odd number"
##
##print(even_or_odd(6))

##x = 0
##def alternation():
##    while x < 10:
##        if x % 2 == 0:
##            print("even number")
##        else:
##            print("odd number")
##        x = x + 1
##print(alternation())

##def alternation():
##    x = 0
##    while x < 10:
##        if x % 2 == 0:
##            print("even number")
##        else:
##            print("odd number")
##        x = x + 1
##
##print(alternation())
        

def alternation(max):
    x = 0
    result = []

    while x < max:
        if x % 2 == 0:
            result.append("even")
        else: 
            result.append("odd")
        x = x + 1
    return(result)
print(alternation(10))