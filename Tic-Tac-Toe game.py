
#Functions are as follows

def display_board(board):
    
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-'+'|'+'-'+'|'+'-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-'+'|'+'-'+'|'+'-')
    print(board[1]+'|'+board[2]+'|'+board[3])



def player_input():
    
    #for player1
    
    player1 = input("Player1 please pick a marker 'X' or 'O'\n")
    
    while player1!='X' and player1!='O':
        player1 = input("\nWrong input, Please pick a marker 'X' or 'O' again\n")
        
    
    #for player2
    
    if player1=='X':
        player2='O'
    elif player1=='O':
        player2='X'
    
    return (player1,player2)



def place_marker(board, marker, position):
    
        
        board[position]= marker



def win_check(board, mark):
    
    #check every rows, columns and diagonals for WIN
    
    for i in range(1,10,3): #rows 
        if board[i]==mark and board[i+1]==mark and board[i+2]==mark:
            return True
    
    for j in range(1,4): #columns
        if board[j]==board[j+3]== board[j+6]==mark:   #with same logic
            return True
                
        #diagnals 
    if (board[1]==mark and board[5]==mark and board[9]==mark) or (board[3]==mark and board[5]==mark and board[7]==mark):
          
        return True
    
    return False


import random

def choose_first():    
    
    firstplayer=random.randint(1,2)
    
    if firstplayer==1:
        return 'player1'
    else:
        return 'player2'

def space_check(board, position):
    
    if board[position]=='X' or board[position]=='O':
        return False
    else:
        return True


def full_board_check(board):
       
    for num in range(1,10):
        
        if board[num]!='X' and board[num]!='O':
            
            return False
        
    return True


def player_choice(board):
    
    position=int(input('Please select your next position between 1 and 9\t'))
    
    if not space_check(board,position):
        
        position=int(input('This is postion is already taken up, Please choose another \t'))
        
    return position


def replay():
    
    if input('Would you like to replay? Enter yes or no\t')=='yes':
        
        round_boolean=True
        
    else:
        
        round_boolean=False
        
    return round_boolean




print('Welcome to Tic Tac Toe')
while True:  #loop the entire framework


    #Setup the game here
    
    the_board=[' ']*10  #empty board
    
    player1_mark,player2_mark=player_input() #tag player_mark with 'X' or 'O'
    
    print(f'player1 chooses {player1_mark}\n')
    
    #decise who to go first

    turn = choose_first()   
    print(f'{turn} will go first!\n')        #don't reference it twice
    
    
    #Enquire whether to start the game
    
    play_game=input('Ready to start the game? Enter yes or no\n')
    
    if play_game=='yes':                                        #'yes'
        game_on = True
    else:
        game_on = False
    
        
    
    #Game On
    while game_on:
        
            #player1 turn 
        if turn == 'player1':         #string
                
            display_board(the_board)   # display the board to the player
            
            position=player_choice(the_board)   #choose the next position
            
            #space check
            if space_check(the_board,position): 
                place_marker(the_board,player1_mark,position) #place the marker on board
            else:
                print('\nthe position you chose is not available, please choose another one')
            
            #win check
            if win_check(the_board,player1_mark):
                game_on=False
                display_board(the_board)
                print('\nplayer1 won the game!')
            
            elif full_board_check(the_board):
                game_on=False
                display_board(the_board)
                print('\nTie game!')
            
            turn='player2'         #switch the turn to player2

        elif turn == 'player2':
            
            display_board(the_board)   # display the board to the player
            
            position=player_choice(the_board)   #choose the next position
            
            #space check
            if space_check(the_board,position): 
                place_marker(the_board,player2_mark,position) #place the marker on board
            else:
                print('\nthe position you chose is not available, please choose another one')
            
            #win check
            if win_check(the_board,player2_mark):
                game_on=False
                display_board(the_board)
                print('\nplayer2 won the game!')
            
            elif full_board_check(the_board):
                game_on=False
                display_board(the_board)
                print('\nTie game!')
            
            turn='player1'          #switch the turn to player1

    if not replay():
        break