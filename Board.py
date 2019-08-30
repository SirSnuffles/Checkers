import tkinter as tk
from PIL import Image, ImageTk

class CheckersGui(tk.Frame):
	def __init__(self, parent, *args, **kwargs):
		"""setup the buttons, cliboard, tkinter frame, and images to be used
		in the game of checkers"""
		self.player1 = Player('alex', True, 'r', False, 500, 12)

		self.player2 = Player('bob', False, 'w', False, 500, 12)

		self.button = [[''for x in range(8)] for y in range(8)]
		self.board = [['' for x in range(8)] for y in range(8)]

		self.taken = False

		self.selectedButton = ()
		self.buttonPushed = ''
		self.nextButton = ()

		#setup tkinter frame
		tk.Frame.__init__(self, parent, *args, **kwargs)
		parent = parent
		#call setup functions
		self.setupButtonImages()
		self.setupBoard()
		self.setupPieces()

	def setupButtonImages(self):
		#Open the images that are saved locally
		black = Image.open("bb.png")
		self.BlackImage = ImageTk.PhotoImage(black)

		white = Image.open("wb.png")
		self.WhiteImage = ImageTk.PhotoImage(white)

		blue = Image.open("sbb.png")
		self.BlueImage = ImageTk.PhotoImage(blue)
		
		redCounter = Image.open("rpbb.png")
		self.redCounterImage = ImageTk.PhotoImage(redCounter)

		selectedRedCounter = Image.open("srpbb.png")
		self.selectedRedCounterImage = ImageTk.PhotoImage(selectedRedCounter)

		whiteCounter = Image.open("wpbb.png")
		self.whiteCounterImage = ImageTk.PhotoImage(whiteCounter)

		selectedWhiteCounter = Image.open("swpbb.png")
		self.selectedWhiteCounterImage = ImageTk.PhotoImage(selectedWhiteCounter)

		possibleMove = Image.open("pm.png")
		self.possibleMoveImage = ImageTk.PhotoImage(possibleMove)

		redKingCounter = Image.open("rpkbb.png")
		self.redKingCounterImage = ImageTk.PhotoImage(redKingCounter)

		selectedRedKingCounter = Image.open("srpkbb.png")
		self.selectedRedKingCounterImage = ImageTk.PhotoImage(selectedRedKingCounter)

		whiteKingCounter = Image.open("wpkbb.png")
		self.whiteKingCounterImage = ImageTk.PhotoImage(whiteKingCounter)

		selectedWhiteKingCounter = Image.open("swpkbb.png")
		self.selectedWhiteKingCounterImage = ImageTk.PhotoImage(selectedWhiteKingCounter)
	
	def setupPieces(self):
		"""changes the values and pictures of self.board and self.button to 
		be in the setup position"""
		for indy in range(3):
			for indx, i in enumerate(self.board[indy]):
				if indy % 2 == 0:
					if indx % 2 == 0:
						self.board[indy][indx] = 'rp'
						self.button[indy][indx].config(image=self.redCounterImage)
				if indy % 2 == 1:
					if indx % 2 == 1:
						self.board[indy][indx] = 'rp'
						self.button[indy][indx].config(image=self.redCounterImage)

		for indy in range(5,8):
			for indx, i in enumerate(self.board[indy]):
				if indy % 2 == 0:
					if indx % 2 == 0:
						self.board[indy][indx] = 'wp'
						self.button[indy][indx].config(image=self.whiteCounterImage)
				if indy % 2 == 1:
					if indx % 2 == 1:
						self.board[indy][indx] = 'wp'
						self.button[indy][indx].config(image=self.whiteCounterImage)

	def setupBoard(self):
		"""Sets up the grid of alternating black and white buttons"""
		self.player1NameLabel = tk.Label(self, text = self.player1.name)
		self.player1NameLabel.grid(row = 0, column = 9)

		self.player1TimeLabel = tk.Label(self, text="", width=10)
		self.player1TimeLabel.grid(row = 1, column = 9)

		self.player1PieceCountLabel = tk.Label(self, text=self.player1.numberOfPieces)
		self.player1PieceCountLabel.grid(row = 2, column = 9)

		self.player2NameLabel = tk.Label(self, text = self.player2.name)
		self.player2NameLabel.grid(row = 5, column = 9)

		self.player2TimeLabel = tk.Label(self, text="", width=10)
		self.player2TimeLabel.grid(row = 6, column = 9)

		self.player2PieceCountLabel = tk.Label(self, text=self.player2.numberOfPieces)
		self.player2PieceCountLabel.grid(row = 7, column = 9)

		self.whoseTurnLabel = tk.Label(self, text="")
		self.whoseTurnLabel.grid(row = 4, column = 10)

		self.countdown()

		for x in range(8):
			for y in range(8):
				if x % 2 == 0:
					if y % 2 == 0:
						self.button[x][y] = tk.Button(self, image=self.BlackImage, command=lambda x = x, y = y: self.recordInput(y,x))
						self.board[x][y] = 'b'
						self.button[x][y].grid(row=x, column=y)
					elif y % 2 == 1:
						self.button[x][y] = tk.Button(self, image=self.WhiteImage, command=lambda x = x, y = y: self.recordInput(y,x))
						self.board[x][y] = 'w'
						self.button[x][y].grid(row=x, column=y)
				if x % 2 == 1:
					if y % 2 == 1:
						self.button[x][y] = tk.Button(self, image=self.BlackImage, command=lambda x = x, y = y: self.recordInput(y,x))
						self.board[x][y] = 'b'
						self.button[x][y].grid(row=x, column=y)
					elif y % 2 == 0:
						self.button[x][y] = tk.Button(self, image=self.WhiteImage, command=lambda x = x, y = y: self.recordInput(y,x))
						self.board[x][y] = 'w'
						self.button[x][y].grid(row=x, column=y)
	
	def countdown(self):
		if self.player1.timeRemaining <= 0:
			self.player1TimeLabel.configure(text="time's up!")
		if self.player2.timeRemaining <= 0:
			self.player2TimeLabel.configure(text="time's up!")
		else:
			if self.player1.turn == True:
				self.player1.timeRemaining -= 1
			elif self.player2.turn == True:
				self.player2.timeRemaining -= 1
			self.player1TimeLabel.configure(text="%d" % self.player1.timeRemaining)
			self.player2TimeLabel.configure(text="%d" % self.player2.timeRemaining)
			self.after(1000, self.countdown)

	def recordInput(self, x, y):
		moveMade = False
		if not moveMade:
			if self.selectedButton == (): # initial button push
				
				self.selectedButton = (x, y)

				if self.board[y][x] == 'rp' and self.player1.turn == True:
					#set selected image
					self.board[y][x] = 'srp'
					#for red pieces
					for indexpair in self.getBackwardIndices(x,y):
						self.board[indexpair[1]][indexpair[0]] = 'p'

				elif self.board[y][x] == 'wp' and self.player2.turn == True:
					#set selected image
					self.board[y][x] = 'swp'
					#for white pieces
					for indexpair in self.getForwardIndices(x,y):
						self.board[indexpair[1]][indexpair[0]] = 'p'

				elif self.board[y][x] == 'rpk' and self.player1.turn == True:
					#set selected image
					self.board[y][x] = 'srpk'
					#for red king pieces
					for indexpair in self.getBackwardIndices(x,y):
						self.board[indexpair[1]][indexpair[0]] = 'p'
					for indexpair in self.getForwardIndices(x,y):
						self.board[indexpair[1]][indexpair[0]] = 'p'

				elif self.board[y][x] == 'wpk' and self.player2.turn == True:
					#set selected image
					self.board[y][x] = 'swpk'
					#for white king pieces
					for indexpair in self.getBackwardIndices(x,y):
						self.board[indexpair[1]][indexpair[0]] = 'p'
					for indexpair in self.getForwardIndices(x,y):
						self.board[indexpair[1]][indexpair[0]] = 'p'

				# self.updateBoard()
			elif self.selectedButton != (x, y) and self.board[y][x] == 'p': 
				#if a different button is pushed
				self.board[self.selectedButton[1]][self.selectedButton[0]] = self.board[self.selectedButton[1]][self.selectedButton[0]].replace('s', ''))
				self.nextButton = (x, y)
				self.move(self.selectedButton[1],self.selectedButton[0], self.nextButton[1],self.nextButton[0])
				moveMade = True
				self.selectedButton = ()
				# self.updateBoard()
			elif self.selectedButton == (x, y):
				#if the same button is pushed
				for indx, moveCol in enumerate(self.board):
					for indy, move in enumerate(moveCol):
						if move == 'p':
							self.board[indx][indy] = 'b'
				self.selectedButton = ()
			self.updateBoard()

	def getForwardIndices(self, x, y):
		"""Standard White move"""
		returningIndices = ()
		if x in range(7) and y != 0:
			if self.board[y-1][x+1] == 'b':
				#add right take move to returning index
				returningIndices += ((x + 1, y - 1),)
			# returningIndices += self.getForwardTakeIndices(x, y)
		if x in range(1,8) and y != 0:
			if self.board[y-1][x-1] == 'b':
				#add left move to returning index
				returningIndices += ((x - 1, y - 1),)
		returningIndices += self.getForwardTakeIndices(x, y)
		return returningIndices

	def getForwardTakeIndices(self, x, y):
		self.returningTakeIndices = ()
		self.taken = ()
		if x in range(6) and y not in range(0,2):
			if self.board[y-1][x+1] in ('rp', 'rpk', 'wpk'):
				if self.board[y-2][x+2] == 'b':
					self.taken += ((x + 1, y - 1),)
					#add right take move to returning index
					self.returningTakeIndices += ((x + 2, y - 2),)

		if x in range(2,8) and y not in range(0,2):
			if self.board[y-1][x-1] in ('rp', 'rpk', 'wpk'):
				if self.board[y-2][x-2] == 'b':
					self.taken += ((x-1,y-1),)
					#add left take move to returning index
					self.returningTakeIndices += ((x-2, y-2),)
		if len(self.taken) > 0:
			self.returningTakeIndices += self.getForwardTakeIndices(x+2,y-2)
			self.returningTakeIndices += self.getForwardTakeIndices(x-2,y-2)

		return self.returningTakeIndices

	def getBackwardIndices(self, x, y):
		"""Standard red move"""
		returningIndices = ()
		if x in range(7) and y != 7:
			if self.board[y+1][x+1] == 'b':
				#add right take move to returning index
				returningIndices += ((x + 1, y + 1),)
			# returningIndices += self.getBackwardTakeIndices(x, y)
		if x in range(1,8) and y != 7:
			if self.board[y+1][x-1] == 'b':
				#add left take move to returning index
				returningIndices += ((x - 1, y + 1),)
		returningIndices += self.getBackwardTakeIndices(x, y)
		return returningIndices

	def getBackwardTakeIndices(self, x, y):
		self.returningTakeIndices = ()
		taken = ()

		if x in range(6) and y not in range(6,8):
			if self.board[y+1][x+1] in ('wp', 'wpk'):
				if self.board[y+2][x+2] == 'b':
					taken += ((x+1, y+1),)
					self.returningTakeIndices += ((x + 2, y + 2),)
					#add right take move to returning index
					print(x + 2, y + 2, "right")
		if x in range(2,8) and y not in range(6,8):
			if self.board[y+1][x-1] in ('wp', 'wpk'):
				if self.board[y+2][x-2] == 'b':
					#add left take move to returning index
					print(x-2, y + 2, "left")
					taken += ((x-2,y+2),)
					self.returningTakeIndices += ((x-2, y+2),)
		if len(taken) > 0:
			print(x, y)
			self.returningTakeIndices += self.getBackwardTakeIndices(x+2, y + 2)
			self.returningTakeIndices += self.getBackwardTakeIndices(x-2,y+2)
		print('got here red', self.returningTakeIndices)
		return self.returningTakeIndices

	def move(self, curx, cury, nexx, nexy):
		if self.board[nexx][nexy] == 'p':
			if self.board[curx][cury] == 'wp' and nexx == 0:
				self.board[curx][cury] = 'wpk'
			elif self.board[curx][cury] == 'rp' and nexx == 7:
				self.board[curx][cury] = 'rpk'
			#check to see if any possible moves are left on the board and remove them.
			for indx, row in enumerate(self.board):
				#check to see if any pieces should be kinged

				for indy, item in enumerate(row):
					if item == 'p':
						self.board[indx][indy] = 'b'

			#find index of the taken piece

			#move the piece
			self.board[nexx][nexy] = self.board[curx][cury]
			self.board[curx][cury] = 'b'

			#delete all pieces in self.deletedPieces

			midx = ((curx-nexx)/2 + nexx)
			midy = ((cury-nexy)/2 + nexy)
			if midx.is_integer() and midy.is_integer():
				
				self.taken = True
			midx, midy = int(midx), int(midy)
			if self.taken == True:
				#destroy the piece taken
				if self.board[midx][midy] == 'wp' or self.board[midx][midy] == 'wpk':
					self.player2.numberOfPieces -= 1
					#take player piece away from count
				elif self.board[midx][midy] == 'rp' or self.board[midx][midy] == 'rpk':
					self.player1.numberOfPieces -= 1
					#take player piece away from count
				self.board[midx][midy] = 'b'
				self.taken = False


			#update turn of players
			if self.player1.turn == True:
				self.player1.turn = False
				self.player2.turn = True
			elif self.player2.turn == True:
				self.player2.turn = False
				self.player1.turn = True

			#reset the button Pushed to not pushed
			self.selectedButton = ()

			#update Label with piece numbers of each player
			self.player1PieceCountLabel.configure(text="%d" % self.player1.numberOfPieces)
			self.player2PieceCountLabel.configure(text="%d" % self.player2.numberOfPieces)
			
			#set a message stating whose turn it is
			if self.player1.turn == True:
				message = self.player1.name + "'s turn!"
			elif self.player2.turn == True:
				message = self.player2.name + "'s turn!"
			self.whoseTurnLabel.configure(text=message)

			#update button images with new cli settings (could use optimization)
			self.updateBoard()

	def updateBoard(self):
		# update buttons with images of self.board
		for indx, x in enumerate(self.board):
			for indy, y in enumerate(x):
				if y == 'wp':
					self.button[indx][indy].config(image=self.whiteCounterImage)
				elif y == 'rp':
					self.button[indx][indy].config(image=self.redCounterImage)
				elif y == 'b':
					self.button[indx][indy].config(image=self.BlackImage)
				elif y == 'w':
					self.button[indx][indy].config(image=self.WhiteImage)
				elif y == 'p':
					self.button[indx][indy].config(image=self.possibleMoveImage)
				elif y == 'rpk':
					self.button[indx][indy].config(image=self.redKingImage)
				elif y == 'wpk':
					self.button[indx][indy].config(image=self.whiteKingImage)
				elif y == 'srp':
					self.button[indx][indy].config(image=self.selectedRedCounterImage)
				elif y == 'swp':
					self.button[indx][indy].config(image=self.selectedWhiteCounterImage)
				elif y == 'srpk':
					self.button[indx][indy].config(image=self.selectedRedKingCounterImage)
				elif y == 'swpk':
					self.button[indx][indy].config(image=self.selectedWhiteKingCounterImage)
				elif y == 'sb':
					self.button[indx][indy].config(image=self.BlueImage)



class Player(CheckersGui):
	def __init__(self, name, turn, colour, winStatus, timeRemaining = 500, numberOfPieces = 12):
		self.name = name
		self.turn = turn
		self.colour = colour
		self.winStatus = winStatus
		self.timeRemaining = timeRemaining
		self.numberOfPieces = numberOfPieces

class Piece(CheckersGui):
	def __init__(self, colour):
		self.colour = colour
		self.king = False


def main():
	newBoard = CheckersBoard()

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('950x690')
	CheckersGui(root).pack(side="top", fill="both", expand=True)
	root.mainloop()		

#NOTES:

#Allow multiple taking (deletion of middle pieces)
#implement king movement methods (cant take backwards?)
#Could implement Piece class???
#need to optimise updateBoard to only update images that have changed

#issues:

#pieces lag on the 7th row for some reason; probably needs optimizing
#	This may be due to

#cant take 2 pieces at once??
