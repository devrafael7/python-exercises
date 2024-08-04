##def invertText(text):
##    return text[::-1]
##print(invertText("python ex"))


##def sumList(list):
##    sum = 0
##    for number in list:
##        sum += number
##    return sum
##
##print(sumList([10, 10, 10, 10, 10, 10, 10, 10]))


##x = "hello world "
##strip = x.strip()
##print(len(strip))


##import random
##import string
##
##def password_generator(len_pass = 8):
##    ascii_options = string.ascii_letters
##    number_options = string.digits
##    punt_options = string.punctuation
##    options = ascii_options + number_options + punt_options
##    
##    user_password = ""
##    
##    for i in range(0, len_pass):
##        digit = random.choice(options)
##        user_password = user_password + digit
##    
##    return user_password
##
##choice_user = input("how much digits on ur password? ")
##
##if choice_user.isdigit():
##    choice_user = int(choice_user)
##else:
##    print("valid")
##    quit()
##
##response = password_generator(len_pass = choice_user)
##print(f"generated password:\n{response}")
