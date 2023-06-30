import random
from functools import reduce
choose=[1,2,3]
up=[]
cp=[]
print('Welcome in danger zone ,this is the most playing but u will regret if you don not play it , the name of the game is: "The Thunder"-Snake/Water/Gun' )
name=input("Enter your name-> ")
age=int(input("Enter your age-> "))
print(f"Player name is : {name}")
print(f"Player age is : {age}")

ask=input("Do you really want danger in life(y/n)-> ")
n=1
while(n<=10):
 if(ask=='y'):
    print("")
    n=n+1
 else:
    print("Try another time")
    break
     
 turn=int(input("Enter number 1(Snake) or 2(Water) or 3(Gun)-> "))
 print("Your turn is->",turn)
 computer=random.choice(choose)
 print(computer)
 if(turn==computer):
    print("Draw")
    up.append(0)
    cp.append(0)
 elif(turn==1 and computer==2):
    print("You win!")  
    up.append(1)
    cp.append(0) 
 elif(turn==1 and computer==3):
    print("You lose!") 
    up.append(0)
    cp.append(1)
 elif(turn==2 and computer==1):
    print("You lose!") 
    up.append(0)
    cp.append(1)
 elif(turn==2 and computer==3):
    print("You win!")
    up.append(1)
    cp.append(0)
 elif(turn==3 and computer==1):
    print("You win!")
    up.append(1)
    cp.append(0) 
 elif(turn==3 and computer==2):
    print("You lose!")
    up.append(0)
    cp.append(1) 
 else:
    print("Invalid turn")
    up.append(0)
    cp.append(1) 
    

print("Game over") 
usum=reduce(lambda x,y:x+y , up)  
csum=reduce(lambda x,y:x+y , cp) 
print(f"{name}:{usum}")
print(f"Computer:{csum}")  
if(usum==csum):
    print(f"Well played {name} match is drawn")
elif(usum>csum):
    print(f"Congratulation {name} you win the match")  
elif(csum>usum):
    print(f"{name} You lose the game")                   