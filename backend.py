from PIL import Image

def black_white(input_image,output_image):
	color_image=Image.open(input_image)
	bw=color_image.convert('L')
	bw.save(output_image)

def main():
	input_image=input("Enter the image name:")
	output_image=input("Enter the name of the image to be saved as:")
	black_white(input_image,output_image)

main()