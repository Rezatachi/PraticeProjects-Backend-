import random

amount = input("Choose how many numbers you want in your wheeler\n")
while isinstance(amount,str) == True:
    print("Please respond with a number.")
if isinstance(amount,int) == True:
    choice_array = []
    for i in range(int(amount)):
        string = input("Choice:")
        choice_array.append(str(string))
    print(choice_array)
    answer = input("Shall I continue to randomize?\n")
    if answer in ["Y", "y", "Yes", "yes"]:
        choice_array_random = random.choice(choice_array)
        print(choice_array_random)
    else:
        print("Alright then. Since you didn't say yes, I'll stop the program.")

