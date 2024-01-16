import random
def single():
 
        player=None
        computer=random.choice(options)

        while player not in options:
            player=input("Enter a choice (rock ,paper ,scissor):")

        print(f"player : {player}")
        print(f"Computer: {computer}")


        if player==computer:
            print("Its a tie!")
        elif player =='rock' and computer=='scissor':
            print("You win!!!!!!!")
        elif player =='paper' and computer=='rock':
            print("You win!!!!!!!")

        elif player =='scissor' and computer=='paper':
            print("You win!!!!!!")
        else:
            print("You Lose... :( ")

def multiple():
    userscore=0
    compscore=0
    totround=3
    for i in range(totround):
           user=input("Enter a choice (rock ,paper ,scissor):")

           compchoice=random.choice(options)

           print(f"Your Choice is: {user}")
           print(f"computer choice is:{compchoice}")

    
           if user==compchoice:
               print("Its a tie!")
           elif user =='rock' and compchoice=='scissor':
               print("You win this round")
               userscore+=1
           elif user =='paper' and compchoice=='rock':
               print("You win this round")
               userscore+=1  
           elif user =='scissor' and compchoice=='paper':
               print("You win this round")
               userscore+=1
           else:
               print("Computer win this round ")
               compscore+=1
    print(f"Player Score:{userscore}")
    print(f"Computer Score: {compscore}")
    if userscore>compscore:
        print("You won most rounds!")
    elif compscore>userscore:
        print("Computer won most rounds!")

    else:
        print("Its a draw")

        
            
options=("rock","paper","scissor")

choice=int(input("Enter 1 for single round \nEnter 2 for multiple round\n"))
if choice==1:
    single()
else:
    multiple()

