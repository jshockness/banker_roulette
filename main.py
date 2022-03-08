import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_ppl = len(names)
random_person = random.randint(0, total_ppl)
print(names[random_person])


