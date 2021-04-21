import sys
import random
import time

#Getting number of players
def input_players():
    x=input("Enter number of players(2/4) : ")
    try:
        no=int(x)
        return no
    except ValueError:
        return None
        
#Main Menu
def menu():
    print(" Snakes and Ladders ")
    print('-'*22)
    msg = """
    Version: 1.0.0
    Developed by: Debasish Nandy

    Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you land at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you land on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit y to roll the dice.

    """
    print(msg)
    print()
    n=input_players()
    return n



#Getting Player Names
def get_name(p):
    name=input("Enter player "+str(p+1)+" name:")    
    return name

"""
import random
die=[1,2,3,4,5,6]
x=random.randint(0,5)
return die[x]
"""
#The Die
def dice():
    x=random.randint(1,6)
    return x

#Turn of players
def turn(n,players,log,score):
    
    for i in range(0,n):
        print("\nPlayer "+str(i+1)+" turn.")
        ip=input(str(players[i])+ " ,press y to spin the dice! \n")
        if ip=='y':
            print("\nRolling the die!!")
            num=dice()
            print("You got "+str(num))
            log[i]=log[i]+num
            #if total score exceeds 100
            if log[i]>100:
                log[i]=log[i]-num
                print("You need "+str(100-log[i])+" to win.")
                
        else:
            print("Wrong key pressed!!!Automatically rolling in 5 secs!!")
            time.sleep(5)
            print("\nRolling the die!!")
            num=dice()
            print("You got "+str(num))
            log[i]=log[i]+num
            if log[i]>100:
                log[i]=log[i]-num
                print("You need "+str(100-log[i])+" to win.")
        
        update(score,players,log)
        compute(score,log)

#Update the score after each turn
def update(score,players,log):
    c=0
    for i in players:
        score[i]=log[c]
        c=c+1

 #Calculating values after each turn
def compute(score,log): 
    snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang"
    ]

    ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
    ]

    # snake takes you down from 'key' to 'value'
    snakes = {
    8: 4, 18: 1, 26: 10, 39: 5, 51: 6, 54: 36, 56: 1, 60: 23,
    75: 28, 83: 45, 85: 59, 90: 48, 92: 25, 97: 87, 99: 63
    }

# ladder takes you up from 'key' to 'value'
    ladders = {
    3: 20, 6: 14, 11: 28, 15: 34, 17: 74, 22: 37, 38: 59,
    49: 67, 57: 76, 61: 78, 73: 86, 81: 98, 88: 91
    }
    
    for k,v in score.items():
        if v in snakes:
            idx=log.index(v)
            new_val=int(snakes.get(v))
            log[idx]=new_val #updating the log after snake bite
            print("\n" + random.choice(snake_bite).upper() + " ~~~~~~~~>")
            print("\n" + k + " got a snake bite. Down from " + str(v) + " to " + str(new_val))
            
        elif v in ladders:
            idx=log.index(v)
            new_val=int(ladders.get(v))
            log[idx]=new_val #updating the log after ladder jump
            print("\n" + random.choice(ladder_jump).upper() + " ########")
            print("\n" + k +  " climbed the ladder from " + str(v) + " to " + str(new_val))
        
        else:
            idx=log.index(v)
            new_val=v
            log[idx]=new_val
            print("\n"+ k + " is at "+str(v))
            
        score[k]=new_val #updating the  total score
        
        check_win(k,v) #checking if anyone's score reached 100

#Checking if anyone's score reached 100
def check_win(player_name, position):
    MAX_VAL=100
    if MAX_VAL == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game.")
        sys.exit(0)

def run():
    n=menu()
    log=list()
    players=list()
    score=dict()
    for i in range(0,n):
        log.append(0)
        nm=get_name(i)
        players.append(nm)
    print("\n The Dice is ready!!")
    while True:
        turn(n,players,log,score)
        print()
        print(score)

if __name__ =='__main__':
    run()