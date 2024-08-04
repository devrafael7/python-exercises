##name = "lucas"
##print(f"{name}, welcome!")

##def greaterNumber(n1, n2):
##    if n1 > n2:
##        return "n1 greater"
##    elif n1 < n2:
##        return "n2 greather"
##    else:
##        return "equals numbers"
##
##print(greaterNumber(5,3))

##for i in range(1, 10):
##    print(i)

##def multiplicationTable(n1, n2):
##    return n1 * n2
##
##print(multiplicationTable(10,10))

##def allTable(n1, n2):
##    choice = ( input("choose an operator: ") )
##    if choice == "/":
##        return n1 / n2
##    elif choice == "*":
##        return n1 * n2
##    elif choice == "+":
##        return n1 + n2
##    elif choice == "-":
##        return n1 - n2
##    else:
##        return "choose one of these: + | - | / | *"
##print(f"the result is: {allTable(10, 3)}")

##def fatorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n * fatorial(n - 1)
##
##print(fatorial(5))

##def countVowels(text):
##    vowels = "aeiouAEIOU"
##    count = 0
##    for char in text:
##        if char in vowels:
##            count = count + 1
##    return count
##
##print(countVowels("whats up bro"))


def length_without_spaces(word):
    word_without_spaces = word.replace(" ", "")
    return len(word_without_spaces)

word = "Whats going on?"
print(length_without_spaces(word))

