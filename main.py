'''
importing the required modules for the operation.
importing TKinter to build a front end window using widgets.
importing PIL aka pillow for backend operations.
importing filedialog to save the operation carried out.
import os-This module provides a portable way of using operating system dependent functionality.
image,imageTk for adding images for the operation.

'''
from tkinter import * 
from tkinter.filedialog import *
from app import *
from PIL import Image,ImageTk
import os
from PIL import ImageOps

""" Creating a new path for the temporary images"""
newpath = r'C:/__editedpics__'

"""If the path doesn't exist it creates a new path"""

if not os.path.exists(newpath):
	os.makedirs(newpath)
location="C:/__editedpics__"

"""Global variables used in the funtions"""

File=None
save_file=None
img1=None
p=None
img2=None

"""Master acts as a parent window variable through which the Tkinter functions are derived"""

master = Tk()

"""Create two new lists for appending and popping the temporary images"""

history=[]
address=[]

"""Creating a canvas for the image imported"""

def main_image():

	canvas.delete("all")
	canvas.create_image(150,150, image=img1)

"""Creating a canvas for previewing the edits done"""

def preview_image():

	      
	canvas1.delete("all")
	canvas1.create_image(150,150, image=img2)


"""Open the image you want using askopenfilename() and append it to the address list as a new list element.
Convert this image to PhotoImage so that it can be accessed by Tkinter.
Append this image to the history list  to import it in the first canvas"""

def open_image(): 
	global open_file
	open_file= askopenfilename() 
	print(open_file)
	global img1
	address.append(open_file)
	image = Image.open(open_file)
	img1 =ImageTk.PhotoImage(image)
	address.append(open_file)
	history.append(img1)
	main_image()

"""To apply changes"""

def applied():
	global img2
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)

"""To save the image in the directory specified by the user.
The recently appended image in the list gets saved"""

def close_image():
	global fullpath
	global p	
	pil_image=p.pop()
	fullpath = os.path.join(askdirectory(), "p" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)


"""Function for previewing the Black and White image in the second canvas.
bw() is a function defined by app.py that converts the latest appended color image into Black and White.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_bw():
	path=address[-1]
	global img2
	global p
	global fullpath
	p=bw(path)
	q=bw(path)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	print(type(pil_image))
	address.append(fullpath)
	history.append(img2)

"""Applies the given contrast value to the lately appended image"""


def apply_contrast(value):
	path=address[-1]
	global img1
	p=adjust_contrast(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)

"""Function for previewing the contrast changed image in the second canvas.
adjust_contrast() is a function defined by app.py that changes the contrast value of the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""	
	
def preview_contrast(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		global p
		p=adjust_contrast(path,val)
		q=adjust_contrast(path,val)
		img2=q.pop()
		preview_image()

		pil_image=q.pop()
		fullpath = os.path.join(location, "sszz" + '.' + "png")
		pil_image.save(fullpath)
		address.append(fullpath)
		history.append(img2)

""" Function that is used to get the value from user to which the contrast has to be changed.
This input from user is then converted to the variable form """

def set_contrast():
	v=int(var.get())
	if v==0:
		pass
	else:
		apply_contrast(int(var.get()))
		pil_image=p.pop()
		fullpath = os.path.join(location, "sszz" + '.' + "png")
		pil_image.save(fullpath)
		address.append(fullpath)
		history.append(img2)

"""Variable that is used to call the user specified contrast value in the buttons"""

var=DoubleVar()

"""Take the user input in the form of length and width for which the image has to be cropped.
resize() is a function defined by app.py that resizes the image according to the input.
Save this in the list for the next operations to carry on"""

def resized():
	length=int(pix.get())
	width=int(pix.get())
	path=address[-1]
	global img2
	global p
	p=resize(path,length,width)
	q=resize(path,length,width)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)

"""Applies the given brightness value to the lately appended image"""


def apply_brightness(value):
	path=address[-1]
	global img1
	p=adjust_brightness(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)

""" Function that is used to get the value from user to which the brightness has to be changed.
This input from user is then converted to the variable form """	

def set_brightness():
	global img2
	global p
	v=int(var1.get())
	if v==0:
		pass
	else:
		apply_brightness(int(var1.get()))
		
"""Function for previewing the brightness changed image in the second canvas.
adjust_brighntess() is a function defined by app.py that changes the brighntess value of the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_brightness(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		global p
		p=adjust_brightness(path,val)
		q=adjust_brightness(path,val)
		img2=q.pop()
		preview_image()
		pil_image=q.pop()
		fullpath = os.path.join(location, "sszz" + '.' + "png")
		pil_image.save(fullpath)
		address.append(fullpath)
		history.append(img2)

		

var1=DoubleVar()

"""Applies the given sharpness value to the lately appended image"""

def apply_sharpness(value):
	path=address[-1]
	global img1
	p=adjust_contrast(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)

""" Function that is used to get the value from user to which the sharpness has to be changed.
This input from user is then converted to the variable form """

def set_sharpness():
	v=int(var.get())
	if v==0:
		pass
	else:
		apply_sharpness(int(var2.get()))
		
"""Function for previewing the sharpness changed image in the second canvas.
adjust_sharpnesss() is a function defined by app.py that changes the sharpness value of the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_sharpness(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		global p
		p=adjust_sharpness(path,val)
		q=adjust_sharpness(path,val)
		img2=q.pop()
		preview_image()
		pil_image=q.pop()
		fullpath = os.path.join(location, "sszz" + '.' + "png")
		pil_image.save(fullpath)
		address.append(fullpath)
		history.append(img2)
		

var2=DoubleVar()

""" Function that is used to get the value from user to which the rotation axis has to be changed.
This input from user is then converted to the variable form """

def set_rotate():
	v=int(var3.get())
	if v==0:
		pass
	else:
		preview_rotate(int(var3.get()))
		global img2
		global p
		pil_image=p.pop()
		global fullpath
		fullpath = os.path.join(location, "sszz" + '.' + "png")
		pil_image.save(fullpath)
		address.append(fullpath)
		history.append(img2)

"""Function for previewing the sharpness changed image in the second canvas.
adjust_rotate() is a function defined by app.py that changes the rotataion value of the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_rotate(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		global p
		p=adjust_rotate(path,val)
		img2=p.pop()
		preview_image()

var3=DoubleVar()

"""Function for previewing the denoised image in the second canvas.
noise() is a function defined by app.py that reduces noise  value of the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_noise():
	path=address[-1]
	global img2
	global p
	p=noise(path)
	q=noise(path)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	global fullpath
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)
	
"""Function for previewing the sharpness changed image in the second canvas.
extra_hue() is a function defined by app.py that acts as a filter and changes the image values defined in the function.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_extrahue():
	path=address[-1]
	global img2
	global p
	p=extra_hue(path)
	q=extra_hue(path)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	global fullpath
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)

"""Function for previewing the sharpness changed image in the second canvas.
extra_dark() is a function defined by app.py that acts as a filter and changes the image values defined in the function.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_extradark():
	path=address[-1]
	global img2
	global p
	p=extra_dark(path)
	q=extra_dark(path)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	global fullpath
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)

"""Applies the given saturation value to the lately appended image"""

def apply_saturation(value):
	path=address[-1]
	global img1
	p=adjust_saturation(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)

""" Function that is used to get the value from user to which the saturation has to be changed.
This input from user is then converted to the variable form """

def set_saturation():
	v=int(var4.get())
	if v==0:
		pass
	else:
		apply_saturation(int(var1.get()))
	
"""Function for previewing the saturation changed image in the second canvas.
adjust_saturation() is a function defined by app.py that changes the sharpness value of the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""

def preview_saturation(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		global p
		p=adjust_saturation(path,val)
		q=adjust_saturation(path,val)
		img2=q.pop()
		preview_image()
		pil_image=q.pop()
		fullpath = os.path.join(location, "sszz" + '.' + "png")
		pil_image.save(fullpath)
		address.append(fullpath)
		history.append(img2)
		

"""Applies the given blur value to the lately appended image"""

def apply_blur(value):
	path=address[-1]
	global img1
	global p
	p=adjust_blur(path,value)
	img1=p.pop()
	main_image()
	pil_image=p.pop()
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	print(fullpath)
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img1)	

""" Function that is used to get the value from user to which the blurness has to be changed.
This input from user is then converted to the variable form """

def set_blur():
	v=int(var5.get())
	if v==0:
		pass
	else:
		apply_blur(int(var5.get()))


"""Function for previewing the blurness changed image in the second canvas.
adjust_blur() is a function defined by app.py that changes the sharpness value of the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""
		
def preview_blur(val):
	v=int(val)
	if v==0:
		pass
	else:
		path=address[-1]
		global img2
		global p
		p=adjust_blur(path,val)
		q=adjust_blur(path,val)
		img2=q.pop()
		preview_image()
		pil_image=q.pop()
		fullpath = os.path.join(location, "sszz" + '.' + "png")
		pil_image.save(fullpath)
		address.append(fullpath)
		history.append(img2)


"""Function for previewing the left-to-right flipped image in the second canvas.
left_right() is a function defined by app.py that flips the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""
		
		
def preview_flip1():
	path=address[-1]
	global img2
	global p
	p=left_right(path)
	q=left_right(path)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	global fullpath
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)


"""Function for previewing the top-to-bottom flipped image in the second canvas.
top_bottom() is a function defined by app.py that flips the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""


def preview_flip2():
	path=address[-1]
	global img2
	global p
	p=top_bottom(path)
	q=top_bottom(path)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	global fullpath
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)


"""Function for previewing the negtaive filter image in the second canvas.
negative() is a function defined by app.py that flips the image in the second canvas.
Temporarily this image gets saved in the previosuly specified location we defined previously"""


def preview_negative():
	path=address[-1]
	global img2
	global p
	p=negative1(path)
	q=negative1(path)
	img2=q.pop()
	preview_image()
	pil_image=q.pop()
	global fullpath
	fullpath = os.path.join(location, "sszz" + '.' + "png")
	pil_image.save(fullpath)
	address.append(fullpath)
	history.append(img2)


"""This function undoes any changes made previously which is not necessary to the user.
It just pops the latest image stored and appends the list with the last but one image."""

def undo_button():
	if len(history)== 0  :
		pass
	else:
		global img2
		img2=history.pop()
		address.pop()
		preview_image()


background=PhotoImage(file="speckbit.gif")
bg=Label(master,bg="pink")
bg.place(x=0,y=0,relwidth=1,relheight=1)
speck=Label(master,image=background)
speck.place(x=30,y=30)


"""
Dividing the front end window into set of different frames helps us to use different geometery methods.
Two different geometrical methods cannot be used at a time with single parent window,thus we divide the parent window into different frames.
The Frame widget is very important for the process of grouping and organizing other widgets in a somehow friendly way. 
It works like a container, which is responsible for arranging the position of other widgets.

"""
'''
Dividing the main master(parent) window into 6 different frames for wisdgets placement.

master-Parent window
we use "side" attribute to determine the placement of the frames in parent winodow

frame1-packed at the TOP of the master window with specified geometery as below.   
           we use this frame to place a button widget named IMPORT, which uses pack() method

frame2-packed at the BOTTOM of the master window with specified geometery as below.
           we use this frame to place a buttons widget named SAVE and APPLY, which uses pack() method

frame3-packed at the LEFT of the master window with specified geometery as below.
           we use this frame to place all button widgets required for filter operation,using grid() method

frame4-packed at the RIGHT of the master window with specified geometery as below.
           we use this frame to place all scale widgets required for scaling images using grid() method.

frame5-packed next to the frame3 with specified geometery as below. 
           we use this frame to place canvas used to view the original image using pack() method. 

frame6-packed next to the frame5 with specified geometery as below. 
           we use this frame to place canvas used to view the editing image using pack() method. 


'''


frame1 = Frame(master,bd=5, width = 12, height =10,bg="pink")
frame1.pack(side=TOP)

frame2 = Frame(master ,bd=5, width = 12, height=10,bg="pink")
frame2.pack(side=BOTTOM)


frame3 = Frame(master,bd=2, width = 500, height =500,bg="pink")
frame3.pack(side=LEFT)

frame4= Frame(master ,bd=5,width = 100, height =1080,bg="pink")
frame4.pack(side=RIGHT)

frame5 = Frame(master,bd=2, width = 500, height =500,bg="pink")
frame5.pack(side=LEFT, expand = 1)

frame6 = Frame(master,bd=2, width = 500, height =500,bg="pink")
frame6.pack(side=LEFT,expand=1)



'''
open button widget:- placed in frame1 with text in display as "IMPORT",having font color as "black" and border width=5pxls & box width=15pxls.
                     command in line with this button is "open_image". It uses pack() method for geometrical placement.

close button widget:- placed in frame2 with text in display as "SAVE",having font color as "black" and border width=5pxls & box width=15pxls.
                      command in line with this button is "close_image". It uses pack() method for geometrical placement.

pack() method-This geometry manager organizes widgets in blocks before placing them in the parent widget.
'''
Open= Button(frame1, text="IMPORT", fg="black",width=15,bd=5,command=open_image)
Open.pack()

close = Button(frame2, text="SAVE", fg="black",width=15,bd=5,command=close_image)
close.pack()

undo = Button(frame1, text="Undo", fg="black",bg="white",command=undo_button)
undo.pack( pady=10)

'''
Here all the filter related operations are clubbed together and placed in frame3 using grid() method. 

grid() method-This geometry manager organizes widgets in a table-like structure in the parent widget.

All filter operations are displayed using Button widget.

b2w button widget:-text in display as "B/W",having font color as "black",border width="5pxls",command in line with this button is "preview_bw".
                   grid() method used to place the button at row=0,column=3. padx=30 & pady=10 (in pxls) is used to leave extra spaces along x & y axis.

xthue button widget:-text in display as "EXTRA HUE",having font color as "black",border width="5pxls",command in line with this button is "preview_extrahue".
                   grid() method used to place the button at row=0,column=5. padx=30 & pady=10 (in pxls) is used to leave extra spaces along x & y axis.

xtdark button widget:-text in display as "EXTRA DARK",having font color as "black",border width="5pxls",command in line with this button is "preview_extradark".
                   grid() method used to place the button at row=4,column=3. padx=30 & pady=10 (in pxls) is used to leave extra spaces along x & y axis.

noisebut button widget:-text in display as "NOISE",having font color as "black",border width="5pxls",command in line with this button is "preview_noise".
                   grid() method used to place the button at row=3,column=3. padx=30 & pady=10 (in pxls) is used to leave extra spaces along x & y axis.

negative button widget:-text in display as "NEGATIVE",having font color as "black",border width="5pxls",command in line with this button is "preview_negative".
                   grid() method used to place the button at row=3,column=5. padx=30 & pady=10 (in pxls) is used to leave extra spaces along x & y axis.

lftflip button widget:-text in display as "LEFT-RIGHT FLIP",having font color as "black",border width="5pxls",command in line with this button is "preview_flip1".
                   grid() method used to place the button at row=2,column=3. padx=30 & pady=10 (in pxls) is used to leave extra spaces along x & y axis.

rightflip button widget:-text in display as "TOP-BOTTOM FLIP",having font color as "black",border width="5pxls",command in line with this button is "preview_flip2".
                   grid() method used to place the button at row=2,column=5. padx=30 & pady=10 (in pxls) is used to leave extra spaces along x & y axis.

''' 

#BLACK/WHITE FILTER

b2w = Button(frame3, text="B/W", fg="black",bd=5,command=preview_bw)
b2w.grid(column=3,row=0,padx=30, pady=10)

#EXTRA HUE FILTER

xthue = Button(frame3, text="EXTRA HUE", fg="black",bd=5,command=preview_extrahue)
xthue.grid(column=5,row=0,padx=30, pady=10)

#EXTRA DARK FILTER

xtdark = Button(frame3, text="EXTRA DARK",fg="black",bd=5, command=preview_extradark)
xtdark.grid(column=3,row=4,padx=30, pady=10)

#NOISE REDUCTION FILTER

noisebut = Button(frame3, text="NOISE", fg="black",bd=5,command=preview_noise)
noisebut.grid(column=3,row=3,padx=30, pady=10)

#NEGATIVE FILTER

negative = Button(frame3, text="NEGATIVE", fg="black",bd=5,command=preview_negative)
negative.grid(column=5,row=3,padx=30, pady=10)

#LEFT FLIP BUTTON

lftflip = Button(frame3, text="LEFT-RIGHT FLIP",  fg="black",bd=5,command=preview_flip1)
lftflip.grid(column=3,row=2,padx=30, pady=10)

#RIGHT FLIP BUTTON

rightflip = Button(frame3, text="TOP-BOTTOM FLIP", fg="black",bd=5,command=preview_flip2)
rightflip.grid(column=5,row=2,padx=30, pady=10)

'''
Sliders used for scaling the image according to the requirements is grouped under the frame4 using the grid() method.

Scale() widget is used to get the sliding operation and scaling accordingly.

All scaling operations are displayed using sliders.

contrast:- placed under frame4 with command in line ass "contrast1" and scaling resolution of 2.

brightness:- placed under frame4 with command in line ass "preview_brightness"  and scaling resolution of 1.

sharpness:- placed under frame4 with command in line ass "preview_sharpness"  and scaling resolution of 2.

saturation:- placed under frame4 with command in line ass "preview_saturation"  and scaling resolution of 2.

blur:- placed under frame4 with command in line ass "preview_blur" and scaling resolution of 2.

rotation:- placed under frame4 with command in line ass "preview_rotate" and scaling resolution of 1.

'''
#CONTRAST BUTTON AND SLIDER
Label(frame4, text = "CONTRAST",bg="black",fg="white").grid(column=2,row=29)
contrast = Scale( frame4 , from_=-100, to=100,resolution=2,variable = var, command=preview_contrast,bg="pink")
contrast.grid(column=2, row=30)
#setcon = Button(frame4, text="DONE",bd=4,command=set_contrast)
#setcon.grid(column=2,row=31)

#BRIGHTNESS BUTTON AND SLIDER

Label(frame4, text = "BRIGHTNESS",bg="black",fg="white").grid(column=4,row=29)
brightness = Scale( frame4, from_=100, to=0,resolution=1,variable = var1,command=preview_brightness,bg="pink")
brightness.grid(column=4, row=30)
#setbri = Button(frame4, text="DONE",bd=4, command=set_brighntess )
#setbri.grid(column=4,row=31)

#SHARPNESS BUTTON AND SLIDER
Label(frame4, text = "SHARPNESS",bg="black",fg="white").grid(column=2,row=39,pady=8)
sharpness = Scale( frame4, from_=25, to=-25,resolution=2,variable = var2,command=preview_sharpness,bg="pink")
sharpness.grid(column=2, row=40)
#setsha = Button(frame4, text="DONE",bd=4, command=set_sharpness)
#setsha.grid(column=2,row=41)

#SATURATION BUTTON AND SLIDER

Label(frame4, text = "SATURATION",bg="black",fg="white").grid(column=4,row=39,pady=8)
var4= DoubleVar()
saturation = Scale( frame4, from_=100, to=-100,resolution=2,variable = var4,command=preview_saturation,bg="pink")
saturation.grid(column=4, row=40)
#setsat = Button(frame4, text="DONE",bd=4,command=set_saturation)
#setsat.grid(column=4,row=41)


#BLURR BUTTON AND SLIDER

Label(frame4, text = "BLUR",bg="black",fg="white").grid(column=2,row=59,pady=8)
var5= DoubleVar()
blurr = Scale( frame4, from_=100, to=-100,resolution=2,variable = var5,command=preview_blur,bg="pink")
blurr.grid(column=2, row=60)
#setblr = Button(frame4, text="DONE",bd=4,command=set_blur)
#setblr.grid(column=2,row=61)


#ROATION AND SLIDER


Label(frame4, text = "ROTATION",bg="black",fg="white").grid(column=4,row=59,pady=8)
rotation = Scale( frame4, from_=-180, to=180,resolution=1,variable = var3,orient=HORIZONTAL, command=preview_rotate,bg="pink")
rotation.grid(column=4, row=60)
#setsat = Button(frame4, text="DONE",bd=4, command=set_rotate)
#setsat.grid(column=4,row=61)

'''
To take the resize values from the user, we use "Entry" widget where we can input our desired values.
once the required scales are given to perform the resize operation we have placed a Button "Resize"
This Entry widget and Button is placed using grid() method in frame3. 

'''
#CROP AND FLIP BUTTONS


pix=Entry(frame3, width = 10)
pix.grid(column=3,row=20) 


Label(frame3, text = "x").grid(column = 4, row = 20) 
pix=Entry(frame3, width = 10)
pix.grid(column=5,row=20)

resize = Button(frame3, text="Resize", fg="brown",command=resized)
resize.grid(column=6,row=20, pady=10)


#window to import image for editing

"""frame5 = Frame(master,bd=2, width = 800, height =800)
frame5.pack(side=LEFT, expand = 1)

canvas = Canvas(frame5, width = 600, height = 600,bg="black")
canvas.pack()"""
'''
For displaying the original image imported and to preview the changes commited by the user, we use 2 canvas widget.
"canvas" with background color black, dimension of 300 x 300 pixels is placed in frame5 by the label "My Image" using pack() method.
"canvas1" with background color black, dimension of 300 x 300 pixels is placed in frame6 by the label "Prview" using pack() method.

'''
Label(frame5, text = "My Image",bg="pink",font="times 26 bold").pack()
Label(frame5).pack()

canvas = Canvas(frame5, width = 300, height = 300,bg="black")
canvas.pack()

Label(frame6, text = "Preview",bg="pink",font="times 26 bold").pack()
Label(frame6).pack()

canvas1 = Canvas(frame6, width = 300, height = 300,bg="black")      
canvas1.pack()

'''
mainloop() is used when you are ready for the application to run. 
mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event till the window is not closed.
parent window.mainloop() is the syntax used here to run the program continuously or we can simply write mainloop(). 
'''
master.mainloop()