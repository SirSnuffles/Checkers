
board = [{"a1":None, "a2":None, "a3":None, "a4":None, "a5":None, "a6":None, "a7":None, "a8":None}, 
		{"b1":None, "b2":None, "b3":None, "b4":None, "b5":None, "b6":None, "b7":None, "b8":None},
		{"c1":None, "c2":None, "c3":None, "c4":None, "c5":None, "c6":None, "c7":None, "c8":None}, 
		{"d1":None, "d2":None, "d3":None, "d4":None, "d5":None, "d6":None, "d7":None, "d8":None},
		{"e1":None, "e2":None, "e3":None, "e4":None, "e5":None, "e6":None, "e7":None, "e8":None}, 
		{"f1":None, "f2":None, "f3":None, "f4":None, "f5":None, "f6":None, "f7":None, "f8":None},
		{"g1":None, "g2":None, "g3":None, "g4":None, "g5":None, "g6":None, "g7":None, "g8":None},
		{"h1":None, "h2":None, "h3":None, "h4":None, "h5":None, "h6":None, "h7":None, "h8":None}, 
		]

for i in board:
	for key, value in i.items():
		if key == 'g7':
			print(value)
