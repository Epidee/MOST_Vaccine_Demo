class Piece:
  def __init__(self, position, color):
    self.position = position
    self.color = color
  #end of __init__

  def printInfo(self):
  	print("position = " + str(self.position) + " color = " + self.color)
  #end of printInfo

  def setPosition(self, pos):
  	self.position = pos
  #end of setPosition

  def setColor(self, col):
  	self.color = col
  #end of setColor

#end of Piece class