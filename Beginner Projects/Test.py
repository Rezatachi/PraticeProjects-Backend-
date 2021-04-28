

print("Welcome to the Love Caclulator")
name1 = input("Enter the first name! \n")
name2 = input("Enter the second name! \n")
combined_string = name1 + name2
lower_num = combined_string.lower()

# COUNT FINDS INSTANDCES OF THAT OBJECT BEING PROCESSED
t = lower_num.count("t")
r = lower_num.count("r")
u = lower_num.count("u")
e = lower_num.count("e")

true = t + r + u + e

l = lower_num.count("l")
o = lower_num.count("o")
v = lower_num.count("v")
e = lower_num.count("e")

love = l + o + v + e

love_score = int(str(true) + (str(love)))


if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you'll get into a good one")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love, {love_score} is somewhat average")
else:
    print("Yikes..")


