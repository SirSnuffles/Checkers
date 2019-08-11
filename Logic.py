#imports
# import Database

# board = Database.board
# blackCount = Database.blackPieceCount
# whiteCount = Database.whitePieceCount
# whiteObjectCount = 0
# blackObjectCount = 0

#database
# a1 a2/ a3 a4/ a5 a6/ a7 a8/
# b1/ b2 b3/ b4 b5/ b6 b7/ b8     Blacks
# c1 c2/ c3 c4/ c5 c6/ c7 c8/
# d1 d2 d3 d4 d5 d6 d7 d8        / to the right means a piece 
# e1 e2 e3 e4 e5 e6 e7 e8
# f1/ f2 f3/ f4 f5/ f6 f7/ f8     Whites
# g1 g2/ g3 g4/ g5 g6/ g7 g8/
# h1/ h2 h3/ h4 h5/ h6 h7/ h8

class board(object):
	def __init__(self):
		self.board = [{"a1":None, "a2":None, "a3":None, "a4":None, "a5":None, "a6":None, "a7":None, "a8":None}, 
					{"b1":None, "b2":None, "b3":None, "b4":None, "b5":None, "b6":None, "b7":None, "b8":None},
					{"c1":None, "c2":None, "c3":None, "c4":None, "c5":None, "c6":None, "c7":None, "c8":None}, 
					{"d1":None, "d2":None, "d3":None, "d4":None, "d5":None, "d6":None, "d7":None, "d8":None},
					{"e1":None, "e2":None, "e3":None, "e4":None, "e5":None, "e6":None, "e7":None, "e8":None}, 
					{"f1":None, "f2":None, "f3":None, "f4":None, "f5":None, "f6":None, "f7":None, "f8":None},
					{"g1":None, "g2":None, "g3":None, "g4":None, "g5":None, "g6":None, "g7":None, "g8":None},
					{"h1":None, "h2":None, "h3":None, "h4":None, "h5":None, "h6":None, "h7":None, "h8":None}]
		self.blackCount = 0
		self.whiteCount = 0
		self.totalCount = 0
		self.turn = "White"

	def __str__(self):
		return "{0}\n{1}\n{2}\n{3}\n{4}\n{5}\n{6}\n{7}".format(*self.board)

	def __repr__(self):
		return "{}".format(self.board)

	def playerTurn(self):
		pass

	def checkWin(self):
		if (self.blackCount == 0) and (totalCount > 1):
			return 'White Wins!'
		elif (self.whiteCount == 0) and (totalCount > 1):
			return 'Black Wins!'

	def insert(self, piece):
		for row in self.board:
			if piece.position in row:
				self.incCount(piece.colour)
				row[piece.position] = piece.colour

	def delete(self, position):
		for row in self.board:
			for positions, piece in row.items():
				if piece != None:
					piece = None
				else:
					print("No object there!")

	def isEmpty(self, position):
		for row in self.board:
			for positions, piece in row.items():
				if position == positions:
					if piece == None:
						return True
					else:
						return position

	def getColour(self, position):
		for row in self.board:
			for positions, piece in row.items():
				if position == positions:
					return piece

	def incCount(self, colour):
		"""increment the piece count when called"""
		if colour == "White":
			self.whiteCount += 1
			self.totalCount += 1
		elif colour == "Black":
			self.blackCount += 1
			self.totalCount += 1

	def setNewGame(self):
		"""make a list containing the instances of the pieces then insert them into the board"""
		pieces = []
		for index, whiteLine in enumerate(['f', 'g', 'h']):
			if index % 2 == 0:
				for odd in range(1, 9, 2):
					pieces.append(piece(whiteLine + str(odd), "White", False))
			else:
				for even in range(2, 10, 2):
					pieces.append(piece(whiteLine + str(even), "White", False))

		for index, blackLine in enumerate(['a', 'b', 'c']):
			if index % 2 == 0:
				for even in range(2, 10, 2):
					pieces.append(piece(blackLine + str(even), "Black", False))
			else:
				for odd in range(1, 9, 2):
					pieces.append(piece(blackLine + str(odd), "Black", False))

		for eachPiece in pieces:
			self.insert(eachPiece)

class piece(board):
	def __init__(self, position, colour, king):
		"""instantiate the objects attributes"""
		board.__init__(self)
		self.position, self.colour, self.king = position, colour, king


	def __repr__(self):
		"""return a string of the details of the instance"""
		return("{}{}{}".format(self.position, self.colour, self.king))

	def __str__(self):
		"""return a formatted string of the details of the instance"""
		return("{}, {}, {}".format(self.position, self.colour, self.king))

	def move(self, newPosition):
		"""move the position if isvalidmove returns True"""
		if self.isValidMove(newPosition):
			if self.kingPiece(newPosition):
				self.king = True
			self.position = newPosition
		else:
			return False

	def canTake(self):
		"""check if there is an enemy instance in moving distance, if so, check if the opposite side is taken, if so"""
		pass

	def take(self, newPosition, takenPosition):
		"""take the instance"""
		self.position = newPosition
		self.delete(takenPosition)

	def isValidMove(self, newMove):
		"""make sure the piece can move to a valid position"""
		position = self.position
		if self.isEmpty(newMove) != None:
			if self.getColour(newMove) == self.colour:
				return False
			elif self.getColour(newMove) != self.colour:
				if (int(newMove[1]) == int(self.position[1]) + 1):
					takenPosition = str(ord((self.position[0])) + 1) + str(int(self.position[1]) + 1)
					takePosition = str(ord((self.position[0])) + 2) + str(int(self.position[1]) + 2)
				elif (int(newMove[1]) == int(self.position[1]) - 1):
					takenPosition = str(ord((self.position[0]) - 1)) + str(int(self.position[1] - 1))
					takePosition = str(ord((self.position[0]) - 2)) + str(int(self.position[1] - 2))
				if self.isEmpty(takePosition):
					self.take(takePosition, takenPosition)
		elif self.isEmpty(newMove):
			if self.king == False:
				if self.colour == "Black":
					if (ord(newMove[0]) == ord(position[0]) + 1): #check if y position is correct for black
						if (int(newMove[1]) == (int(position[1]) + 1)) or (int(newMove[1]) == (int(position[1]) - 1)):
							return True							  #check if x position is correct for white
				elif self.colour == "White":
					if (ord(newMove[0]) == ord(position[0]) - 1):
						if (int(newMove[1]) == (int(position[1]) + 1)) or (int(newMove[1]) == (int(position[1]) - 1)):
							return True
			elif self.king == True:
				if ((ord(newMove[0]) == ord(position[0]) + 1) or (ord(newMove[0]) == ord(position[0]) - 1)):
					if (int(newMove[1]) == (int(position[1]) + 1)) or (int(newMove[1]) == (int(position[1]) - 1)):
						return True


	def kingPiece(self, newPosition):
		"""sets the king attribute to True"""
		if (self.colour == "Black") and (newPosition[0] == 'h'):
			return True
		elif (self.colour == "White") and (newPosition[0] == 'a'):
			return True
		else:
			return False

def main():
	newBoard = board()
	newBoard.setNewGame()
	print(newBoard)
	# print(newBoard)
	# newBoard = board()
	# newPiece = piece("f3", "White", False)
	# print(newPiece.__repr__())
	# newPiece.move("e4")
	# print(newPiece.__repr__())
	# # newPiece.move("")

	# print(newBoard.__str__())
	# newBoard.insert(newPiece)
	# print('')
	# print(newBoard.__str__())
	# setupBoard()
	# print(ord("c"), ord("d"))
	# print(Database.board)
	# print(piece.board)

if __name__ == '__main__':
	main()

#Notes
#

#set up unit tests asap

#format the board so it is readable

#check if the piece is moving off the map make sure input is between a-h and 1-8

#allow insertion into the board

#check if a piece can take another     .b1..
#									   ..w1.
#									   ...w2 <-- b1 cant take w1 because w2 is in the way

#check if white is on a row and check if black is on h row for a king

#create a gui to display the board once the logic is 'flawless'

