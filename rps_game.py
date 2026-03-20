import random 

comp = random.randint(0 ,2)
user = int (input("Enter your number 0 for rock , 1 for paper , 2 for scissor: "))

def cheak(user, comp):
    if (user == comp):
        return "Draw"
    elif (user == 0 and comp == 1):
        return "Computer Win"
    elif (user == 1 and comp == 2):
        return "Computer Win"
    elif (user == 2 and comp == 0):
        return "Computer Win"
    else:
        return "User Win"


print(cheak(user, comp))    

print(user)
print(comp)


