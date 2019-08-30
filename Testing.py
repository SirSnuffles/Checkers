import tkinter as tk

class Piece(object):
	def __init__(self, colour, position, king=False, selected = False):
		self.colour = colour
		self.king = king
		self.position = position
		self.positionX = position[0]
		self.positionY = position[1]
		self.selected = selected

	def possibleTakeMove(self):
		if not self.king:
			if self.colour == 'white':
				return ((self.positionX + 2, self.positionY - 2), (self.positionX - 2, self.positionY - 2),)
			elif self.colour == 'red':
				return ((self.positionX + 2, self.positionY + 2), (self.positionX - 2, self.positionY + 2),)
		if self.king:
			return ((self.positionX + 2, self.positionY - 2), (self.positionX - 2, self.positionY - 2),(self.positionX + 2, self.positionY + 2), (self.positionX - 2, self.positionY + 2),)

	def possibleStandardMove(self):
		if not self.king:
			if self.colour == 'white':
				return ((self.positionX + 1, self.positionY - 1), (self.positionX - 1, self.positionY - 1),)
			elif self.colour == 'red':
				return ((self.positionX + 1, self.positionY + 1), (self.positionX - 1, self.positionY + 1),)
		if self.king:
			return ((self.positionX + 1, self.positionY - 1), (self.positionX - 1, self.positionY - 1),(self.positionX + 1, self.positionY + 1), (self.positionX - 1, self.positionY + 1),)

class WhitePiece():
	def __init__(self):
		pass

	def possibleMoves(self):
		pass

class RedPiece():
	def __init__(self):
		pass

	def possibleMove(self):
		pass


class Checkers():
	def __init__(self):
		self.board = [[None for i in range(8)]for j in range(8)]
		self.setupPieces()
		self.handlePlayers()

	def __repr__(self):
		formattedBoard = [[]for i in range(8)]
		count = 0
		for indi, i in enumerate(self.board):
			for j in i:
				if j != None:
					formattedBoard[indi].append(j.colour)
				if j == None:
					formattedBoard[indi].append(None)
		for i in formattedBoard:
			print(i)

	def handlePlayers(self):
		redPlayer = Player(True, 'red')
		whitePlayer = Player(False, 'white')

	def movePiece(self, x, y, newx, newy):
		pieceToMove = self.selectPiece(x,y)
		if pieceToMove:
			for move in pieceToMove.possibleStandardMove():
				if move == (newx,newy):

					print(pieceToMove.positionX, newx)
					print(pieceToMove.positionY, newy)
					pieceToMove.positionX = newx
					pieceToMove.positionY = newy
					self.board[pieceToMove.positionY][pieceToMove.positionX], self.board[pieceToMove.positionY][pieceToMove.positionX] = self.board[newy][newx], None

	def selectPiece(self, x, y):
		"""select a piece from the board"""
		return self.board[y][x]

	def setupPieces(self):
		"""changes the values and pictures of self.board and self.button to 
		be in the setup position"""
		whiteCount = 0
		redCount = 0
		for indpositionY in range(3):
			for indpositionX, i in enumerate(self.board[indpositionY]):
				if indpositionY % 2 == 0:
					if indpositionX % 2 == 0:
						self.board[indpositionY][indpositionX] = Piece('red', (indpositionX, indpositionY))
						redCount += 1
						# print(self.board[indpositionY][indpositionX].colour, ' added')
				if indpositionY % 2 == 1:
					if indpositionX % 2 == 1:
						self.board[indpositionY][indpositionX] = Piece('red', (indpositionX, indpositionY))
						redCount += 1
						# print(self.board[indpositionY][indpositionX].colour, ' added')
		for indpositionY in range(5,8):
			for indpositionX, i in enumerate(self.board[indpositionY]):
				if indpositionY % 2 == 0:
					if indpositionX % 2 == 0:
						self.board[indpositionY][indpositionX] = Piece('white', (indpositionX, indpositionY))
						whiteCount += 1
						# print(self.board[indpositionY][indpositionX].colour, ' added')
				if indpositionY % 2 == 1:
					if indpositionX % 2 == 1:
						self.board[indpositionY][indpositionX] = Piece('white', (indpositionX, indpositionY))
						whiteCount += 1
						# print(self.board[indpositionY][indpositionX].colour, ' added')
		print(redCount, whiteCount)

class CheckersGui(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		#setup tkinter frame
		tk.Frame.__init__(self, parent, *args, **kwargs)
		parent = parent
		print('this')
		newBoard.__repr__()

class Player(object):
	def __init__(self, turn, colour):
		self.turn = turn
		self.colour = colour

def main():
	root = tk.Tk()
	root.geometry('950x690')
	CheckersGui(root).pack(side="top", fill="both", expand=True)
	root.mainloop()
	# newBoard.__repr__()

	newBoard = Checkers()
	piece = newBoard.selectPiece(5,5)
	piece.king = False
	print(piece)
	newBoard.movePiece(5,5,4,4)
	print(piece.king)
	print(piece.positionX, piece.positionY)
	print(newBoard.selectPiece(4,4))
	# newBoard.__repr__()

if __name__ == '__main__':
	main()