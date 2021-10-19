from graphics import *

win = GraphWin("NewWin", 600,600)
win.setBackground("light blue")

leftline = Line(Point(200,0),Point(200,600))
rightline = Line(Point(400,0),Point(400,600))
topline = Line(Point(0,200),Point(600,200))
bottomline = Line(Point(0,400),Point(600,400))
def MainMenu(win):
    win.setBackground("red")
    TicTacToeButton = Rectangle(Point(100,400),Point(200,500))
    TicTacToeButton.draw(win)
    Title = Text(Point(300,100),"Welcome to TicTacToe")
    Play = Text(Point(150,450),"Play")
    Play.setSize(18)
    Play.draw(win)
    Title.setSize(36)
    Title.draw(win)
    p = win.getMouse()
    Title.undraw()
    Play.undraw()
    TicTacToeButton.undraw()    

def drawlines(N,S,E,W):
    win.setBackground("cyan")
    N.draw(win)
    S.draw(win)
    E.draw(win)
    W.draw(win)
MainMenu(win)
drawlines(leftline,rightline,topline,bottomline)


def locationY(p):
    if p.getY() < 200:
        return 100
    if p.getY() > 200 and p.getY() <400:
        return 300
    else:
        return 500
def locationX(p):
    if p.getX() < 200:
        return 100
    if p.getX() > 200 and p.getX() <400:
        return 300
    else:
        return 500
def DrawXO(Y,X,Character):
    X = Text(Point(X,Y),Character)   
    X.setSize(36)
    X.draw(win) 
def CheckWin(Board):
    #Checking Horizontal Victory 
    Victory = 0
    for i in range(3):
        if Board[i][0] == Board[i][1] and Board[i][1] == Board[i][2] and Board[i][0] != 0:
            print("Horizontal Victory")
            Victory = 1
    #Checking Vertial Victory
    for i in range(3):
        if Board[0][i] == Board[1][i] and Board[1][i] == Board[2][i] and Board[0][i] != 0:
            print("Vertical Victory")
            Victory = 1
    #Checking Diagonal Win
    if Board[0][0] == Board[1][1] and Board[1][1] == Board[2][2] and Board[0][0] != 0:
        print("Right Diagonal Win")
        Victory = 1
    if Board[0][2] == Board[1][1] and Board[1][1] == Board[2][0] and Board[0][2] != 0:
        print("Left Diagonal Win")
        Victory = 1
    return Victory 


def GamePlay(win):
    Character = 'X'
    Board = [[0 for i in range(3)] for j in range(3)]
    
    ##drawlines(leftline,rightline,topline,bottomline)
    while True:
        SuccessfullMove = 0
        while(SuccessfullMove == 0):
            p = win.getMouse()      
            Y = locationY(p)
            X = locationX(p)
            BoardPositionX = int((X - 100)/200)
            BoardPositionY = int((Y - 100)/200)
         
            if Board[BoardPositionX][BoardPositionY] == 0: #For Blank Space
                SuccessfullMove = 1
                if Character == 'X':
                  Board[BoardPositionX][BoardPositionY] = 1 #For X
                else:
                  Board[BoardPositionX][BoardPositionY] = -1 #For Y
            else: 
                continue
        Win = CheckWin(Board)
        if Win == 1:
            break
        SuccessfullMove = 0
                
        DrawXO(Y,X,Character)
        if Character == 'X':
            Character = 'O'
        else: 
            Character = 'X'
    print(f"Player {Character} Wins")
GamePlay(win)


    
