import random
upperlet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerlet=upperlet.lower()
digi="0123456789"
sym="(){}[],;:.-_/?\\+*&%$#@!~`"
upper, lower, nums, syms= True, True, True, True
all=" "
if upper:
    all+=upperlet
if lower:
    all+=lowerlet
if nums:
    all+=digi
if syms:
    all+=sym
length=15
amount=10
for x in range(amount):
    password="".join(random.sample(all,length))
    print(password)