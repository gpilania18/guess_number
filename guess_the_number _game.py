import random as random
count=0
num= random.randint(1,100)

for i in range (1, 11):
    guess = int(input("guess the number between 1 and 100 :"))
    if num== guess:
            break
    else:
        if guess>num:
            print("lesser")
        else:
            print("higher")
    count=count+1
if num==guess:
    print ("congrats! you won")
else:
     print("oh! attempts over ")