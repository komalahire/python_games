from random import randint
def win():
    print 'You win!'
def lose():
    print 'You lose!'
while True:
    player_choice = raw_input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = player_choice[random_move]
    if player_choice == computer_choice:
        print 'Draw!'
    elif player_choice == 'rock' and computer_choice== 'scissors':
        print win()
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print lose()
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print win()
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print lose()
    elif player_choice == 'paper' and computer_choice == 'rock':
        win()
    else:
        print   lose()
    again = raw_input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break
