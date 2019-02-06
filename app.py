'''
importing the required modules for the operation.
importing PIL aka pillow for backend operations.
importing ImageFilter and ImageEnhance for the the filter operations.
image,imageTk for adding images for the operation.

'''

from PIL import Image,ImageTk
from PIL import ImageFilter,ImageEnhance
from PIL import ImageOps

"""This function converts the color image to Black and White.
im.convert('L') is an inbuilt function in the library Image.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def bw(i):
	p=[]
	im=Image.open(i)
	bw=im.convert('L')
	image_tk=ImageTk.PhotoImage(bw)
	p.append(bw)
	p.append(image_tk)
	return p

"""This function chnages the contrast of the image.
ImageEnhance.Contrast() is an inbuilt function in the library ImageEnhance.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def adjust_contrast(i, factor):
	factor=int(factor)
	p=[]
	image = Image.open(i)
	enhancer_object = ImageEnhance.Contrast(image)
	out = enhancer_object.enhance(factor)
	out_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(out_tk)
	return p

"""This function resizes the image.
Collect the size to which the image has to be shrinked from user.
.thumbnail() is a function that changes the image size according to the parameters mentioned.
Append this image to the list p"""

def resize(i,length,width):
	p=[]
	size=(length,width)
	image=Image.open(i)
	image.thumbnail(size)
	image_tk=ImageTk.PhotoImage(image)
	p.append(image)
	p.append(image_tk)
	return p

"""This function chnages the brighntess of the image.
ImageEnhance.Brightness() is an inbuilt function in the library ImageEnhance.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def adjust_brightness(i, factor):
	factor=int(factor)
	p=[]
	image = Image.open(i)
	enhancer_object = ImageEnhance.Brightness(image)
	out = enhancer_object.enhance(factor)
	out_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(out_tk)
	return p

"""This function chnages the sharpness of the image.
ImageEnhance.Sharpness() is an inbuilt function in the library ImageEnhance.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""


def adjust_sharpness(i, factor):
	factor=int(factor)
	p=[]
	image = Image.open(i)
	enhancer_object = ImageEnhance.Sharpness(image)
	out = enhancer_object.enhance(factor)
	out_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(out_tk)
	return p

"""This function adjusts the rotation axis of the image.
.rotate() is an inbuilt function in the library Image.
The degree of rotation can be mentioned as parameters to this inbuilt function.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def adjust_rotate(i,degrees):
	degrees=int(degrees)
	p=[]
	image=Image.open(i)
	rotated=image.rotate(degrees)
	out_tk=ImageTk.PhotoImage(rotated)
	p.append(rotated)
	p.append(out_tk)
	return p

"""This function reduces the noise of the image.
Create a new array of 9*9 with only zeros. Obtain the pixel value of evry element.
Store the current pixel value and the adjacent values.Comapre and sort it using sort()
Form a new image by apppeding the actual vlaue with sorted value
Conver the image to Tkimage."""

def noise(i):
	p=[]
	img = Image.open(i)
	width,height=img.size 
	members = [(0,0)] * 9
	newimg = Image.new("RGB",(width,height),"white")
	for i in range(1,width-1):
		for j in range(1,height-1):
			members[0] = img.getpixel((i-1,j-1))
			members[1] = img.getpixel((i-1,j))
			members[2] = img.getpixel((i-1,j+1))
			members[3] = img.getpixel((i,j-1))
			members[4] = img.getpixel((i,j))
			members[5] = img.getpixel((i,j+1))
			members[6] = img.getpixel((i+1,j-1))
			members[7] = img.getpixel((i+1,j))
			members[8] = img.getpixel((i+1,j+1))
			members.sort()
			newimg.putpixel((i,j),(members[4]))
	out_tk=ImageTk.PhotoImage(newimg)
	p.append(newimg)
	p.append(out_tk)
	return p

"""This function gives a image that has extra hue than the original.
It used two functions Brighntess and Color.
These two paramters are changed and a new filter is obtained.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def extra_hue(i):
	p=[]
	im=Image.open(i)
	coverter=ImageEnhance.Color(im)
	imag=coverter.enhance(2)
	enhancer=ImageEnhance.Brightness(imag)
	out=enhancer.enhance(0.5)
	image_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(image_tk)
	return p

"""This function gives a image that has extra dark than the original.
It used two functions contrast and Sharpness.
These two paramters are changed and a new filter is obtained.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def extra_dark(i):
	p=[]
	im=Image.open(i)
	coverter=ImageEnhance.Contrast(im)
	imag=coverter.enhance(5)
	enhancer=ImageEnhance.Sharpness(imag)
	out=enhancer.enhance(1)
	image_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(image_tk)
	return p

"""This function chnages the saturation of the image.
ImageEnhance.Color() is an inbuilt function in the library ImageEnhance.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def adjust_saturation(i, factor):
	factor=int(factor)
	p=[]
	image = Image.open(i)
	enhancer_object = ImageEnhance.Color(image)
	out = enhancer_object.enhance(factor)
	out_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(out_tk)
	return p

"""This function chnages the sharpness of the image.
ImageEnhance.Sharpness() is an inbuilt function in the library ImageEnhance.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def adjust_blur(i, factor):
	factor=int(factor)
	p=[]
	image = Image.open(i)
	out = image.filter(ImageFilter.GaussianBlur(factor))
	out_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(out_tk)
	return p

"""This function chnages the filps the image left-to-right.
.transpose() is an inbuilt function in the library Image.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def left_right(i):
	p=[]
	im=Image.open(i)
	flipped_image=im.transpose(Image.FLIP_LEFT_RIGHT)
	image_tk=ImageTk.PhotoImage(flipped_image)
	p.append(flipped_image)
	p.append(image_tk)
	return p

"""This function chnages the filps the image top-to-bottom.
.transpose() is an inbuilt function in the library Image.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def top_bottom(i):
	p=[]
	im=Image.open(i)
	flipped_image=im.transpose(Image.FLIP_TOP_BOTTOM)
	image_tk=ImageTk.PhotoImage(flipped_image)
	p.append(flipped_image)
	p.append(image_tk)
	return p

"""This function gives the negative of image.
ImageOps.invert() is an inbuilt function in the library ImageOps.
Convert the pil image to PhotoImage by using ImageTk.
Append this image to the list p"""

def negative1(i):
	p=[]
	im=Image.open(i)
	out=ImageOps.invert(im)
	image_tk=ImageTk.PhotoImage(out)
	p.append(out)
	p.append(image_tk)
	return p
	

