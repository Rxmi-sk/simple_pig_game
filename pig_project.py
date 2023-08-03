import random

def roll_dice():
    min=1
    max=6
    
    return random.randint(min,max)


while True:
    player_num = input("Please enter the number of players (between 2 & 4 players): ")
    if player_num.isdigit():
        player_num= int(player_num)

        if player_num<2 or player_num>4:
            print("Number must be between 2-4 players")
        
        else:
            break

    else:
        print("Invalid, try again")


print("Let the game start!")
scoreBoard=[]


for i in range(player_num):
    scoreBoard.append(0)

won=False

while True:
    
    if won == True:
        break
    
    player_indx=0
    currentScore=0

    while player_indx<player_num:
        action=input("Player "+str(player_indx+1)+" would you like to roll (r) or hold (h) (Your Total score is: " + str(scoreBoard[player_indx])+ "): ")
        

        if action.lower() == 'r':
            
            while True:
                
                roll=roll_dice()
                
                if roll==1:
                    print("You have rolled a 1 and so your Total Score will be reset to what it was before the round")
                    print("Here is your Total Score: " + str(scoreBoard[player_indx]))
                    currentScore=0
                    player_indx=player_indx+1
                    break

                else:
                    print("You've rolled a: "+ str(roll))
                    currentScore= currentScore + roll

                    if scoreBoard[player_indx]+currentScore>=100:
                        won=True
                        print("==============================")
                        print("Player "+str(player_indx+1)+" has reached 100 Points!!!!!")
                        print("Congrats you've won")
                        print("Game Over")
                        print("==============================")
                        player_indx=10
                        break


                    print("Current Score is for this turn is "+str(currentScore)+ " and Total Score is: "+ str(scoreBoard[player_indx]+currentScore))
                    action=input("Would you like to roll again or hold: ")
                    
                    if action.lower()=='h':
                        scoreBoard[player_indx]= scoreBoard[player_indx] + currentScore
                        currentScore=0
                        player_indx=player_indx+1
                        break 


        elif action.lower()=='h':
            currentScore=0
            player_indx=player_indx+1

            
            


        


    