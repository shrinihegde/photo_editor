from PIL import Image
 backend_1_#1









import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
 develop
from PIL import ImageEnhance
import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def black_white(input_image,output_image):
	color_image=Image.open(input_image)
	bw=color_image.convert('L')
	bw.save(output_image)
 
def adjust_contrast(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)
 

def cropped(input_image,co,output_image):
	image=Image.open(input_image)
	values=input('Enter:')
	lists=(values).split(" ")
	co=tuple(map(int,lists))
	cropped_image=image.crop(co)
	cropped_image.save(output_image)



def filter1(input_image,output_image):
	img = cv2.imread(inp)

	kernel = np.ones((3,3),np.float32) * (-1)
	kernel[1,1] = 8
	dst = cv2.filter2D(img,-1,kernel)

	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Filters')
	plt.xticks([]), plt.yticks([])
	plt.show()


def filter2(input_image,output_image):

	img = Image.open(input_image)
	width,height=img.size
	newimg = Image.new("RGB", (width,height), "white")
	for x in range(1, width-1):  # ignore the edge pixels for simplicity (1 to width-1)
    	for y in range(1, height-1): # ignore edge pixels for simplicity (1 to height-1)

        	# initialise Gx to 0 and Gy to 0 for every pixel
        	Gx = 0
        	Gy = 0

        	# top left pixel
        	p = img.getpixel((x-1, y-1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	# intensity ranges from 0 to 765 (255 * 3)
        	intensity = r + g + b

        	# accumulate the value into Gx, and Gy
        	Gx += -intensity
        	Gy += -intensity

        	# remaining left column
        	p = img.getpixel((x-1, y))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += -2 * (r + g + b)

        	p = img.getpixel((x-1, y+1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += -(r + g + b)
        	Gy += (r + g + b)

        	# middle pixels
        	p = img.getpixel((x, y-1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gy += -2 * (r + g + b)

        	p = img.getpixel((x, y+1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gy += 2 * (r + g + b)

        	# right column
        	p = img.getpixel((x+1, y-1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += (r + g + b)
        	Gy += -(r + g + b)

 backend_1_#1
 
def adjust_contrast(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)
 

def cropped(input_image,co,output_image):
	image=Image.open(input_image)
	values=input('Enter:')
	lists=(values).split(" ")
	co=tuple(map(int,lists))
	cropped_image=image.crop(co)
	cropped_image.save(output_image)



def filter1(input_image,output_image):
	img = cv2.imread(inp)

	kernel = np.ones((3,3),np.float32) * (-1)
	kernel[1,1] = 8
	dst = cv2.filter2D(img,-1,kernel)

	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Filters')
	plt.xticks([]), plt.yticks([])
	plt.show()


def filter2(input_image,output_image):

	img = Image.open(input_image)
	width,height=img.size
	newimg = Image.new("RGB", (width,height), "white")
	for x in range(1, width-1):  # ignore the edge pixels for simplicity (1 to width-1)
    	for y in range(1, height-1): # ignore edge pixels for simplicity (1 to height-1)

        	# initialise Gx to 0 and Gy to 0 for every pixel
        	Gx = 0
        	Gy = 0

        	# top left pixel
        	p = img.getpixel((x-1, y-1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	# intensity ranges from 0 to 765 (255 * 3)
        	intensity = r + g + b

        	# accumulate the value into Gx, and Gy
        	Gx += -intensity
        	Gy += -intensity

        	# remaining left column
        	p = img.getpixel((x-1, y))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += -2 * (r + g + b)

        	p = img.getpixel((x-1, y+1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += -(r + g + b)
        	Gy += (r + g + b)

        	# middle pixels
        	p = img.getpixel((x, y-1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gy += -2 * (r + g + b)

        	p = img.getpixel((x, y+1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gy += 2 * (r + g + b)

        	# right column
        	p = img.getpixel((x+1, y-1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += (r + g + b)
        	Gy += -(r + g + b)


 develop
        	p = img.getpixel((x+1, y))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += 2 * (r + g + b)

        	p = img.getpixel((x+1, y+1))
        	r = p[0]
        	g = p[1]
        	b = p[2]

        	Gx += (r + g + b)
        	Gy += (r + g + b)

        	# calculate the length of the gradient (Pythagorean theorem)
        	length = math.sqrt((Gx * Gx) + (Gy * Gy))

        	# normalise the length of gradient to the range 0 to 255
        	length = length / 4328 * 255

        	length = int(length)

        	# draw the length in the edge image
        	#newpixel = img.putpixel((length,length,length))
        	newimg.putpixel((x,y),(length,length,length))
	newimg.save(output_image)

def invert(input_image,output_image):
	img1 = cv2.imread(input_image)
	img=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

	kernel = np.ones((3,3),np.float32) * (-1)
	kernel[1,1] = 8

	dst = cv2.filter2D(img,-1,kernel)

	plt.subplot(121),plt.imshow(img),plt.title('Original')
	plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.title('Filters')
	plt.xticks([]), plt.yticks([])
	plt.show()
	dst.save(output_image)

def noise(input_image,output_image):
	img = cv2.imread(input_image)
	img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	dst = cv2.fastNlMeansDenoisingColored(img1,None,10,10,7,21)

	plt.subplot(121),plt.imshow(img1),plt.xticks([]),plt.yticks([])
	plt.subplot(122),plt.imshow(dst),plt.xticks([]),plt.yticks([])
	plt.show()
	dst.save(output_image)

def rotate(input_image,degrees,output_image):

	image=Image.open(input_image)
	rotated=image.rotate(degrees)
	rotated.save(output_image)



def sharpness(input_image,out_image,factor):
	image=Image.open(input_image)
	enhancer_object=ImageEnhance.Sharpness(image)
	out=enhancer_object.enhance(factor)
	out.save(out_image)

  
def negative():

	img = cv2.imread('images.jpg')
	img1=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
	img1[:,:,0] = cv2.equalizeHist(img1[:,:,0])
	col=cv2.cvtColor(img1,cv2.COLOR_YUV2BGR)
	cv2.imwrite('new.jpg',col)

def flip_settings(input_image,flip_side,output_image):
	im=Image.open(input_image)
	if flip_side==2:
		flipped_image=im.transpose(Image.FLIP_LEFT_RIGHT)
	else:
		flipped_image=im.transpose(Image.FLIP_TOP_BOTTOM)
	flipped_image.save(output_image)

	im=input('enter the name of the image')
	print("1.top_down    2.left_rigt" )
	flip_side=int(input("enter the choice"))
	flip_settings(im,flip_side,"flipped_image.jpg")


def extra_hue(img):
	im=Image.open(img)
	coverter=ImageEnhance.Color(im)
	imag=coverter.enhance(2)
	enhancer=ImageEnhance.Brightness(imag)
	out=enhancer.enhance(0.5)
	out.save('filtered_image.jpg')

def extra_dark(img):
	im=Image.open(img)
	coverter=ImageEnhance.Contrast(im)
	imag=coverter.enhance(5)
	enhancer=ImageEnhance.Sharpness(imag)
	out=enhancer.enhance(1)
	out.save('filtered_image.jpg')

def saturation_settings(input_image,factor,output_image):
	im=Image.open(input_image)
	coverter=ImageEnhance.Color(im)
	img=coverter.enhance(factor)
	img.save(output_image)


def blur_settings(input_image):
	image=Image.open(input_image)
	blurred=image.filter(ImageFilter.BLUR)
	blurred.save('blurred1.jpg')

def bright(input_image, output_image, factor):
	image=Image.open(input_image)
	enhancer=ImageEnhance.Brightness(image)
	out=enhancer.enhance(factor)
	out.save(output_image)


