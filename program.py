from PIL import Image
import time
from pprint import pprint

Image.LOAD_TRUNCATED_IMAGES = True
#file=open("imagevalue","w")
#wb=Workbook()
#ws=wb.active
values={}
xycoord=[]
x=0
y=0
xy=[]
def merge_images(file1, file2, file3,file4):
	"""Merge  images into one, displayed side by side
	:param file1: path to first image file
	:param file2: path to second image file
	:return: the merged Image object
	"""
	image1 = Image.open(file1)
	image2 = Image.open(file2)
	image3 = Image.open(file3)
	image4 = Image.open(file4)
	(width1, height1) = image1.size
	(width2, height2) = image2.size
	(width3, height3) = image3.size
	(width4, height4) = image4.size
	

	result_width = width1 + width2 
	result_height = height1 * 2 

	result = Image.new('RGB', (result_width, result_height))
	result.paste(im=image1, box=(0, 0))
	result.paste(im=image2, box=(width1, 0))
	result.paste(im=image3, box=(0, height1))
	result.paste(im=image4, box=(width3 , height3 ))
	return result
merged = merge_images("images/1.png","images/2.png","images/3.png","images/4.png") 
print "Intializing Merging photo ..."
time.sleep(2)
merged.save( "Full.png" )
print "full.png Saved...."
time.sleep(1)
print "Opening Full.png..."
time.sleep(1)
merged.show()

FILENAME='Full.png' #image can be in gif jpeg or png format 
im=Image.open(FILENAME).convert('RGB')
pix=im.load()
w=im.size[0]
h=im.size[0]
print "Intializing Image Proccessing...."
for i in range(w):
  for j in range(h):
	
	coord=i,j
	pix_val=pix[i,j]
	values.update({coord:pix[i,j]})
	xycoord.append(coord)
	
rmin= input("from where do you want your RED value to Start? ")
rmax= input("To where do you want your RED value to End?")
gmin= input("from where do you want your GREEN value to Start? ")
gmax= input("To where do you want your GREEN value to Start? ")
bmin= input("from Where do you want your BLUE value to Start? ")
bmax= input("from Where do you want your BLUE value to Start? ")
rchanged=input("Set the new RED Value... ")
gchanged=input("Set the new GREEN Value... ")
bchanged=input("Set the new BLUE Value... ")

#print(xycoord[0])
#print type(xycoord[0])	
for value in sorted(values):
	pixel=values[value]
	r= range(rmin,rmax)
	g=range(gmin,gmax)
	b=range(bmin,bmax)

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
	pix[xint,yint] = (rchanged, gchanged, bchanged) # set the colour accordingly
print "Image Highlighted Successfuly..."
time.sleep(0.5)
print "Saving and Opening the Image..."
time.sleep(1)
im.save("identified-%s" %(FILENAME))
im.show()

