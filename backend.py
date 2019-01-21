from PIL import Image
from PIL import ImageEnhance

def black_white(input_image,output_image):
	color_image=Image.open(input_image)
	bw=color_image.convert('L')
	bw.save(output_image)


input_image=input("Enter the image name:")
output_image=input("Enter the name of the image to be saved as:")
black_white(input_image,output_image)


 
def adjust_contrast(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)
 

input_image=input("Enter the image name:")
output_image=input("Enter the name of the image to be saved as:")
factor=float(input("Enter the amount of contrast required:"))
adjust_contrast(input_image,output_image,factor)

