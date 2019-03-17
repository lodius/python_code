#!/usr/bin/python

class Board:
    def __init__(self):
        self.board_matrix = [["-","-","-"],
                             ["-","-","-"],
                             ["-","-","-"],]
        self.winner = None

    def __str__(self):
        ret =  ("   x \n")
        ret += ("   2 | {}  {}  {} \n".format(*self.board_matrix[2]))
        ret += ("   1 | {}  {}  {} \n".format(*self.board_matrix[1]))
        ret += ("   0 | {}  {}  {} \n".format(*self.board_matrix[0]))
        ret += ("------------------\n")
        ret += ("   y | 0  1  2    \n")
        return ret

    def __assert_item(self, item, list):
        if item in list:
            return True
        else:
            return False

    def reset_game(self):
        self.board_matrix = [["-","-","-"],
                             ["-","-","-"],
                             ["-","-","-"],]

    def check_victory(self, player):
        if player.move < 3:
            pass
        else:
            #Check all rows
            for i in self.board_matrix:
                if i == [player.mark,player.mark,player.mark]:
                    return True

            #Check all columns
            checks=0
            for i in range(3):
                for j in range(3):
                    if self.board_matrix[j][i] == player.mark:
                        checks+=1
                        if checks == 3:
                            return True
                checks=0

            #Check diagonal
            if [self.board_matrix[0][0],self.board_matrix[1][1],self.board_matrix[2][2]] == [player.mark,player.mark,player.mark]:
                return True
            if [self.board_matrix[0][2],self.board_matrix[1][1],self.board_matrix[2][0]] == [player.mark,player.mark,player.mark]:
                return True
        return False

    def make_move(self, player, x, y):
        if self.board_matrix[y][x] != "-":
            print("Illegal move!")
            return
        self.board_matrix[y][x] = player.mark
        player.move += 1
        if self.check_victory(player) == True:
            self.winner = player

class Player:
    def __init__(self, name, mark):
        self.move = 0
        self.name = name
        self.mark = mark

#Initialization
print("Welcome to the Tic Tac Toe game!!")
player1=Player("quaky","o")
player2=Player("god","x")
board = Board()
total_moves = 0
turn_switch = False

#Enter game loop
while board.winner == None :
    try:
        #Print instruction and game
        print("Player {}'s move please input x and y seperated by space and then enter (type exit to quit)"
              .format(player2.name if turn_switch else player1.name))
        print(board)

        #Prompt user to input move coordinate
        str_input = input().split(" ")
        if str_input[0] == "exit":
            break
        if len(str_input) != 2:
            print("Illegal input! Please enter again!")
            continue
        coordinate = [int(a) for a in str_input]

        #Reflect move coordinate
        board.make_move(player2 if turn_switch else player1, coordinate[1],coordinate[0])

        #Prepare for next turn
        turn_switch = not turn_switch
        total_moves += 1

        #Check for tie
        if (total_moves > 8):
            print("It's a tie")
            print("Now reset game")
            board.reset_game()
    except ValueError:
        print("Illegal input! Please enter again!")
else:
    print(board)
    print("Winner is {}".format(board.winner.name))

print("Bye")
