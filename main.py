import sys, termios, tty, os, time
from os import system, name

boardSizeX = 8
boardSizeY = 8
playerPosX = 0
playerPosY = 0
numberOfLandmines = 0
atTopOfBoard = False
landminesHit = 0

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def make_board():
  board = []
  for Y in range(boardSizeY):
    row = []
    for X in range(boardSizeX):
      if playerPosX == X and playerPosY == Y:
        row.append("@")
      else:
        row.append(".")

    board.append(row)
  return board

def print_board(board):
  for Y in reversed(range(boardSizeY)): #why is it reversed? :)
    for X in range(boardSizeX):
      row = board[Y]
      cell = row[X]
      print(cell, end="")
    print("\r")

while atTopOfBoard == False or landminesHit <= 2:
  clear()
  board = make_board()
  print_board(board)
  keyPressed = getch()
  if keyPressed == "d":
    playerPosY += - 1
    if playerPosY < 0:
      playerPosY = 0
  elif keyPressed == "u":
    playerPosY += 1
    if playerPosY >= boardSizeY - 1:
      playerPosY = boardSizeY - 1
      atTopOfBoard = True
  elif keyPressed == "l":
    playerPosX -= 1
    if playerPosX <=0:
      playerPosX = 0
  elif keyPressed == "r":
    playerPosX += 1
    if playerPosX >= boardSizeX - 1:
      playerPosX = boardSizeX - 1


if atTopOfBoard and landminesHit <= 2:
  print("Well done you win")
else:
  print("You Lose! Better Luck Next Time!!")

CRAPCRAPCRAPCRAPCRAPCRAPCRAPCRAPCRAPCRAP