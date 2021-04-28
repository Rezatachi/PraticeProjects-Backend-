#Password Generator Project
import random
print("Welcome to the PyPassword Generator!")

# This for loop shows the range of 1 to the number of letters to the user wanted. In this case, it would be 1 to the Input + 1 to include the input
def extractor():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password = ""
    for char in range(1, nr_letters + 1):
    #Use a random command to randomize a random item from the list
        password += random.choice(letters)
    for char in range(1, nr_numbers + 1):
        password += random.choice(numbers)
    for char in range(1, nr_symbols + 1):
        password += random.choice(symbols)

    def randomizer():
        random.sample(password)
    print("Your generated password is" + password)
    question = input("Do you want to randomize again?\n")
    if question in "Yes":
        print(f"Your new generated password is {extractor()}")
extractor()







    

        
