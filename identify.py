from PIL import Image
from openpyxl import Workbook
from pprint import pprint
Image.LOAD_TRUNCATED_IMAGES = True
FILENAME='C64-palette.png' #image can be in gif jpeg or png format 
im=Image.open(FILENAME).convert('RGB')
pix=im.load()
w=im.size[0]
h=im.size[0]
#file=open("imagevalue","w")
#wb=Workbook()
#ws=wb.active
values={}
xycoord=[]
print "processing"
for i in range(w):
  for j in range(h):
	
	coord=i,j
	pix_val=pix[i,j]
	values.update({coord:pix[i,j]})
	xycoord.append(coord)
	

#print(xycoord[0])
#print type(xycoord[0])	
x=0
y=0

xy=[]
for value in sorted(values):
	pixel=values[value]
	r= range(135,137)
	g=range(56,58)
	b=range(49,51)

	red=pixel[0]
	green=pixel[1]
	blue=pixel[2]
	
	
	if red in r and green in g and blue in b :
		xy.append(value)
	x=x+1
	y=y+1

points= set(xycoord) & set(xy)
for point in points :
	xint=int(point[0])
	yint=int(point[1])
	pix[xint,yint] = (224, 170, 138) # set the colour accordingly
im.show()
im.save("identified-%s" %(FILENAME))
