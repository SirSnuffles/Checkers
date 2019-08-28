from PIL import Image, ImageTk
import os

basewidth = 80
for file in os.listdir('/home/snuffles/Programs/PersonalPrograms/PersonalPrograms/PythonScripts/Checkers'):
	if file.endswith('.png'):
		filename = file
		img = Image.open(filename)


		wpercent = (basewidth/float(img.size[0]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((basewidth,hsize), Image.ANTIALIAS)
		img.save(filename) 