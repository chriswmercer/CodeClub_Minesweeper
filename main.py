import sys, termios, tty, os, time
from os import system, name 

boardSizeX = 8
boardSizeY = 8
playerPosX = 7
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
  for ypos in range(boardSizeY):
    row = []
    for xpos in range(boardSizeX):
      if playerPosX == xpos and playerPosY == ypos:
        row.append("@")
      else:
        row.append(".")

    board.append(row)
  return board

def print_board(board):
  for y in range(boardSizeY):
    for x in range(boardSizeX):
      row = board[y]
      cell = row[x]
      print(cell, end="")
    print("\r")

clear()

while atTopOfBoard == False or landminesHit <= 2:
  board = make_board()
  print_board(board)
  keyPressed = getch()
  print(f"you pressed {keyPressed}")
  if keyPressed == "d":
    playerPosY = playerPosY + 1
  elif keyPressed == "u":
    playerPosY = playerPosY + 1


if atTopOfBoard and landminesHit <= 2:
  print("Well done you win")
else:
  print("Bad luck you lost, loser")
