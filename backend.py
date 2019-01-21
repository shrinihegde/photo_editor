from PIL import Image
import cv2

def black_white(input_image,output_image):
	color_image=Image.open(input_image)
	bw=color_image.convert('L')
	bw.save(output_image)

input_image=input("Enter the image name:")
output_image=input("Enter the name of the image to be saved as:")
black_white(input_image,output_image)



img = cv2.imread('images.jpg')
img1=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img1[:,:,0] = cv2.equalizeHist(img1[:,:,0])
col=cv2.cvtColor(img1,cv2.COLOR_YUV2BGR)
cv2.imwrite('new.jpg',col)
