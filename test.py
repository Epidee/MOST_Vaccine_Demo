from pkg.Piece import Piece
import random

print("Hello, World!")

# number of squares on the board at X and Y
numX = 8
numY = 8
# number of cells to start off with
numCells = 6
# list of where the cells are currently at
# list is from position 0 (top-left) to position 63 (bottom-right)
cellPositionList=[]

# Randomize cell positions to any square on the board
# used for testing purposes, delete when you have sensors
def randomizeCellPositions():
	while len(cellPositionList) < numCells:
	    r=random.randint(0,(numX*numY-1))
	    if r not in cellPositionList: 
	    	cellPositionList.append(r)

	print(cellPositionList)
#end of randomizeCellPositions

# Get the position of the cells on the board by reading
# all the sensors and determining which ones has the cell on it
# update once you have the sensors set up
def getCellPositions():
	for i in range(numX*numY):
		#readSensor
		#if cell, add to list
		cellPositionList.append("something")
#end of getCellPositions

# place the cells on the board
randomizeCellPositions()

# create a test piece
testPiece = Piece(1, "blue")
testPiece.setPosition(2)
testPiece.setColor("red")
testPiece.printInfo()