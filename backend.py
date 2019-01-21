from PIL import Image
import cv2
from PIL import ImageEnhance

def black_white(input_image,output_image):
	color_image=Image.open(input_image)
	bw=color_image.convert('L')
	bw.save(output_image)



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

