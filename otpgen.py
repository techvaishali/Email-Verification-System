import random

otp = ''
for _ in range(4):
    r = random.randint(0, 9)
    otp += str(r)  
print(otp)