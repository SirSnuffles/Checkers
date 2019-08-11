# import Logic


# Logic.main()



# blacks 

board = [{"a1":None, "a2":"Black", "a3":None, "a4":"Black", "a5":None, "a6":"Black", "a7":None, "a8":"Black"}, 
		{"b1":"Black", "b2":None, "b3":"Black", "b4":None, "b5":"Black", "b6":None, "b7":"Black", "b8":None},
		{"c1":None, "c2":"Black", "c3":None, "c4":"Black", "c5":None, "c6":"Black", "c7":None, "c8":"Black"}, 
		{"d1":None, "d2":None, "d3":None, "d4":None, "d5":None, "d6":None, "d7":None, "d8":None},
		{"e1":None, "e2":None, "e3":None, "e4":None, "e5":None, "e6":None, "e7":None, "e8":None}, 
		{"f1":"White", "f2":None, "f3":"White", "f4":None, "f5":"White", "f6":None, "f7":"White", "f8":None},
		{"g1":None, "g2":"White", "g3":None, "g4":"White", "g5":None, "g6":"White", "g7":None, "g8":"White"},
		{"h1":"White", "h2":None, "h3":"White", "h4":None, "h5":"White", "h6":None, "h7":"White", "h8":None}, 
		]

blackPieceCount = 0
whitePieceCount = 0

for k in board:
	for i, j in k.items():
		# print(i,j)
		if j == "Black":
			blackPieceCount += 1
		elif j == "White":
			whitePieceCount += 1

print(ord("f"), ord("h"))
# print(blackPieceCount, whitePieceCount)