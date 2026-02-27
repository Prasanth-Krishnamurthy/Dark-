def play(round=0):
    choices = ["ROCK", "PAPER", "SCISSORS"]
    user = input("ENTER ROCK, PAPER, SCISSORS OR EXIT: ").upper()
    if user == "EXIT":
        print("GOODBYE!")
        return
    computer = choices[round % 3]
    print("COMPUTER CHOSE:", computer)
    if user == computer:
        print("IT'S A TIE!")
    elif (user == "ROCK" and computer == "SCISSORS") or \
         (user == "PAPER" and computer == "ROCK") or \
         (user == "SCISSORS" and computer == "PAPER"):
        print("YOU WIN!")
    else:
        print("COMPUTER WINS!")
    
    play(round + 1)

play()
