# Question 1
age = int(input("How old are you right now?"))
print("In 2049, you will be", age + 31)
# Question 2
score = 0
for i in range(1, 6):
    score += int(input(f"Judge {i}: "))

print(f"Your Olympic score is {score / 5}.")
# Question 3
burgerprice = 0
friesprice = 0
burger = input("Would you like a burger for $5? (yes/no)")
if burger == "yes":
    burgerprice = 5
else:
    pass
fries = input("Would you like fries for $3? (yes/no)")
if fries == "yes":
    friesprice = 5
else:
    pass
totalpricebeforetax = burgerprice + friesprice
tax = totalpricebeforetax * 0.14
totalprice = totalpricebeforetax + tax
print(f"Your total is ${totalprice:.2f}")
