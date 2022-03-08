import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Get total number of items in array
total_ppl = len(names)
random_person = random.randint(0, total_ppl - 1)
payer = names[random_person]
print(payer + " will pay the bill today.")
# Final Solution
