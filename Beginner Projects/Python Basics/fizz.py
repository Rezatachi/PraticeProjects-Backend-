
number = int(input("Choose a number and we'll decide if its worthy of the fizz or buzz \n"))
total = 0
for total in range(1,101):
    if (number % 3 == 0):
        #If Divisble by 3
        print("Fizz") 
        break
    elif (number % 3 == 0 and number % 5 == 0):
        #If Divisble by 3
        print("FissBuzz")
        break
    elif(number % 5 == 0):
        #If Divisble by 3
        print("Buss")
        break
    else:
        number = int(input("Try Again \n"))
        
