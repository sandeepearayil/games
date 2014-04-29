from random import randint
from collections import Counter

def draw_board(board):
    print '', board[1], '|', board[2], '|', board[3], \
          '\n-----------\n', \
          '', board[4], '|', board[5], '|', board[6], \
          '\n-----------\n', \
          '', board[7], '|', board[8], '|', board[9], \
          '\n'
          
def random_move():
    return randint(1,9)

def random_beginner():
    if not randint(2,10) % 2:
        beginner = 'Computer'
    else:
        beginner = 'You'
    return beginner
  
# Decorator to check winner    
def check_winner(check_function):
    def check_win(board,p_choice,c_choice):
        game = 'In Progress'
        available_moves = [i for i,item in enumerate(board)  if item == ' ']
        # Column win    
        for item in [1,2,3] :
            if board[item] == board[item + 3] and board[item] == board[item + 6] and board[item] != ' ':
                game = 'won'
                if board[item] == p_choice :
                    print 'You have won the game'
                else:
                    print 'Computer has won the game'
        # Row win
        for item in [1,4,7] :
            if board[item] == board[item + 1] and board[item] == board[item + 2] and board[item] != ' ':
                game = 'won'
                if board[item] == p_choice :
                    print 'You have won the game'
                else:
                    print 'Computer has won the game'
        # Diagonal win
        for item in [1,3] :
            if board[item] == board[5] and board[item] == board[10 - item] and board[item] != ' ':
                game = 'won'
                if board[item] == p_choice :
                    print 'You have won the game'
                else:
                    print 'Computer has won the game'
        #check for Tie          
        if available_moves == []:
            print 'Game over - You have been tied by the computer'
            game = 'tied'
            
        # No wins or ties
        if game == 'In Progress' :
            check_function(board,p_choice,c_choice)
        else:
            draw_board(board)
    return check_win    



@check_winner    
def player_move(board,p_choice,c_choice):
    draw_board(board)
    print 'Player has to make a move - Use numbers 1 to 9 for positions on the board starting from top left and progressing left to right.'
    play_move = input()
    if board[int(play_move)] == ' ':
        board[int(play_move)] = p_choice
    else:
        print 'Already occupied. Please make another choice'
        play_move = input()
        board[int(play_move)] = p_choice
    computer_move(board,p_choice,c_choice)


@check_winner    
def computer_move(board,p_choice,c_choice):
    print 'Computer is making a move'
    computer_play = 0
    draw_board(board)

    # Preference 1 - Win the game in the next move
    # Check for all possibilities of winning on columns
    for item in range(1,3) :
        if board[item] == board[item + 3]  and board[item] == c_choice and computer_play == 0:
            if board[item + 6] == ' ':
                computer_play = item + 6
        elif board[item] == board[item + 6] and board[item] == c_choice and computer_play == 0:
            if board[item + 3] == ' ':
                computer_play = item + 3
        elif board[item + 6] == board[item + 3] and board[item + 6] == c_choice and computer_play == 0:
            if board[item] == ' ':
                computer_play = item

    # Check for all possibilities of winnings on rows
    for item in [1,4,7] :
            if board[item] == board[item + 1] and board[item] == c_choice and computer_play == 0:
                if board[item + 2] == ' ':
                    computer_play = item + 2
            elif board[item] == board[item + 2] and board[item] == c_choice and computer_play == 0:
                if board[item + 1] == ' ':
                    computer_play = item + 1
            elif board[item + 1] == board[item + 2] and board[item + 1] == c_choice and computer_play == 0:
                if board[item ] == ' ':
                    computer_play = item              

    # Check for all possibilities for winning on Diagonals
    for item in [1,3] :
                if board[item] == board[5] and board[item] == c_choice and computer_play == 0:
                    if board[10 - item] == ' ':
                        computer_play = 10 - item
                elif board[5] == board[10 - item] and board[5] == c_choice and computer_play == 0:
                    if board[item] == ' ':
                        computer_play = item
            
#Prefernce 2 -  Check for opportunity to block the opponents winning move
    for item in range(1,3) :
                if board[item] == board[item + 3]  and board[item] == p_choice and computer_play == 0 and board[item + 6] == ' ':
                    computer_play = item + 6
                elif board[item] == board[item + 6] and board[item] == p_choice and computer_play == 0 and board[item + 3] == ' ':
                    computer_play = item + 3
                elif board[item + 6] == board[item + 3] and board[item + 6] == p_choice and computer_play == 0 and board[item] == ' ':
                    computer_play = item

                    
    for item in [1,4,7] :
                if board[item] == board[item + 1] and board[item] == p_choice and computer_play == 0 and board[item + 2] == ' ':
                    computer_play = item + 2
                elif board[item] == board[item + 2] and board[item] == p_choice and computer_play == 0 and board[item + 1] == ' ':
                    computer_play = item + 1
                elif board[item + 1] == board[item + 2] and board[item + 1] == p_choice and computer_play == 0 and board[item] == ' ':
                    computer_play = item 
                    
    for item in [1,3] :
                if board[item] == board[5] and board[item] == p_choice and computer_play == 0and board[10 - item] == ' ':
                    computer_play = 10 - item
                elif board[5] == board[10 - item] and board[5] == p_choice and computer_play == 0 and board[item] == ' ':
                    computer_play = item


    # Preference 3 - Center if center is free
    if board[5] == ' ':
        computer_play = 5
    
    # Preference 4 - Play the  corners if free [1,3,6,9]
    corners = [1,3,6,9]
    for item in corners: 
        if board[item] == ' ' and computer_play == 0:
            computer_play = item
            
    # If no opportunity
    print 'Computer play is:'
    print (computer_play)
            
    # If no corners are free and there is no winning and blocking move, choose randomly from available moves
    if  computer_play == 0:
        available_moves = [i for i,item in enumerate(board)  if item == ' ']
        print available_moves 
        if available_moves == []:
            print 'Game over - You have been tied'
        else:
            computer_play = available_moves[randint(0,len(available_moves)-1)]
            board[computer_play] = c_choice 
    else:
        board[computer_play] = c_choice   
    computer_play = 0
    player_move(board,p_choice,c_choice)


def start_game():
    print 'Welcome to Tic tac Toe'
    p_choice = raw_input('Enter your choice: ').upper()
    if p_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'
    print('You chose:',p_choice)
    board = [' '] * 10
    board[0] = 'E'
    if random_beginner() == 'You':
        player_move(board,p_choice,c_choice)
    else:
        computer_move(board,p_choice,c_choice)
    

if __name__ == '__main__':start_game()