#Variables are just nicknmes
import random

people = ["Sabrina",
          "Abraham"]

weight = [140,
          160]

random_people = random.choice(people)
random_weight = random.choice(weight)
random_sum = random_weight + random_weight

print(f"So I believe that {random_people} and {random_weight} 's weight combined is {random_sum}")