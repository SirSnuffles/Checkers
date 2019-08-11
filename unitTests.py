#unit tests

import unittest
import Logic

class TestBoard(unittest.TestCase):

	def setUp(self):
		self.newBoard = Logic.board()


	def tearDown(self):
		pass

	def testsetNewGame(self):
		#check making a newBoard starts with nothing in it
		for line in self.newBoard.board:
			for position, piece in line.items():
				self.assertEqual(piece, None)
		self.assertEqual(self.newBoard.totalCount, 0)
		self.assertEqual(self.newBoard.whiteCount, 0)
		self.assertEqual(self.newBoard.blackCount, 0)
		self.newBoard.setNewGame()
		self.assertEqual(self.newBoard.totalCount, 24)
		self.assertEqual(self.newBoard.whiteCount, 12)
		self.assertEqual(self.newBoard.blackCount, 12)
		# self.



class TestPiece(unittest.TestCase):

	def setUp(self):
		# self.emp2 = Employee_class.Employee('Sue', 'twat', 10000)
		newBoard = Logic.board()
		self.piece1 = Logic.piece("f3", "White", False)
		self.piece2 = Logic.piece("b3", "Black", False)
		self.piece3 = Logic.piece("c2", "Black", True)
		self.piece4 = Logic.piece("g2", "White", True)

	def tearDown(self):
		pass

	def testMove(self):
		#testing a White piece
		self.assertEqual(self.piece1.position, "f3")
		self.piece1.move("e4")
		self.assertEqual(self.piece1.position, "e4")
		self.piece1.move("d3")
		self.assertEqual(self.piece1.position, "d3")
		self.piece1.move("e2")
		self.assertEqual(self.piece1.position, "d3")
		self.piece1.move("e4")
		self.assertEqual(self.piece1.position, "d3")

		#testing a Black piece
		self.assertEqual(self.piece2.position, "b3")
		self.piece2.move("c4")
		self.assertEqual(self.piece2.position, "c4")
		self.piece2.move("b5")
		self.assertEqual(self.piece2.position, "c4")
		self.piece2.move("d3")
		self.assertEqual(self.piece2.position, "d3")
		self.piece2.move("c2")
		self.assertEqual(self.piece2.position, "d3")

		#testing a Black king
		self.assertEqual(self.piece3.position, "c2")
		self.piece3.move("d3")
		self.assertEqual(self.piece3.position, "d3")
		self.piece3.move("c4")
		self.assertEqual(self.piece3.position, "c4")
		self.piece3.move("b3")
		self.assertEqual(self.piece3.position, "b3")
		self.piece3.move("c2")
		self.assertEqual(self.piece3.position, "c2")
		self.piece3.move("a1")
		self.assertEqual(self.piece3.position, "c2")

		#testing a White king
		self.assertEqual(self.piece4.position, "g2")
		self.piece4.move("f1")
		self.assertEqual(self.piece4.position, "f1")
		self.piece4.move("e2")
		self.assertEqual(self.piece4.position, "e2")
		self.piece4.move("f3")
		self.assertEqual(self.piece4.position, "f3")
		self.piece4.move("g2")
		self.assertEqual(self.piece4.position, "g2")
		self.piece4.move("f2")
		self.assertEqual(self.piece4.position, "g2")
		self.piece4.move("t10")
		self.assertNotEqual(self.piece4.position, "t10")



if __name__ == '__main__':
	unittest.main()