from tkinter import * 

master=Tk()

#ADDING OPEN AND CLOSE BUTTONS

frame1 = Frame(master,bd=5, width = 12, height =10)
frame1.pack(side=TOP)
Open= Button(frame1, text="IMPORT", fg="black",width=15,bd=5)
Open.pack()

frame2 = Frame(master ,bd=5, width = 12, height=10)
frame2.pack(side=BOTTOM)
close = Button(frame2, text="SAVE", fg="black",width=15,bd=5)
close.pack()

# ADDING FILTERS TO THE WINDOW

frame3 = Frame(master,bd=2, width = 500, height =500)
frame3.pack(side=LEFT)

#BLACK/WHITE FILTER

b2w = Button(frame3, text="B/W", fg="black",bd=5)
b2w.grid(column=3,row=0,padx=30, pady=10)

#EXTRA HUE FILTER

xthue = Button(frame3, text="EXTRA HUE", fg="black",bd=5)
xthue.grid(column=5,row=0,padx=30, pady=10)

#EXTRA DARK FILTER

xtdark = Button(frame3, text="EXTRA DARK",fg="black",bd=5)
xtdark.grid(column=3,row=2,padx=30, pady=10)

#BETA FILTER

beta = Button(frame3, text="BETA", fg="black",bd=5)
beta.grid(column=5,row=2,padx=30, pady=10)

#ADDING LIGHT SETTINGS TO THE WINDOW
#ADDING SLIDERS TO THE WINDOWS


frame4= Frame(master ,bd=5,width = 100, height =1080)
frame4.pack(side=RIGHT)

#CONTRAST BUTTON AND SLIDER
contra = DoubleVar()
Label(frame4, text = "CONTRAST",bg="black",fg="white").grid(column=2,row=29)
contrast = Scale( frame4 , from_=100, to=-100,resolution=2,variable = contra)
contrast.grid(column=2, row=30)
setcon = Button(frame4, text="DONE",bd=4)
setcon.grid(column=2,row=31)

#BRIGHTNESS BUTTON AND SLIDER

Label(frame4, text = "BRIGHTNESS",bg="black",fg="white").grid(column=4,row=29)
bright= DoubleVar()
brightness = Scale( frame4, from_=100, to=-100,resolution=2,variable = bright)
brightness.grid(column=4, row=30)
setbri = Button(frame4, text="DONE",bd=4 )
setbri.grid(column=4,row=31)

#SHARPNESS BUTTON AND SLIDER
Label(frame4, text = "SHARPNESS",bg="black",fg="white").grid(column=2,row=39,pady=8)
sharp= DoubleVar()
sharpness = Scale( frame4, from_=100, to=-100,resolution=2,variable = sharp)
sharpness.grid(column=2, row=40)
setsha = Button(frame4, text="DONE",bd=4)
setsha.grid(column=2,row=41)

#SATURATION BUTTON AND SLIDER

Label(frame4, text = "SATURATION",bg="black",fg="white").grid(column=4,row=39,pady=8)
saturate= DoubleVar()
saturation = Scale( frame4, from_=100, to=-100,resolution=2,variable = saturate)
saturation.grid(column=4, row=40)
setsat = Button(frame4, text="DONE",bd=4)
setsat.grid(column=4,row=41)


#BLURR BUTTON AND SLIDER

Label(frame4, text = "BLUR",bg="black",fg="white").grid(column=2,row=59,pady=8)
blur= DoubleVar()
blurr = Scale( frame4, from_=100, to=-100,resolution=2,variable = blur)
blurr.grid(column=2, row=60)
setblr = Button(frame4, text="DONE",bd=4)
setblr.grid(column=2,row=61)


#ROATION AND SLIDER


Label(frame4, text = "ROTATION",bg="black",fg="white").grid(column=4,row=59,pady=8)
rotate= DoubleVar()
rotation = Scale( frame4, from_=-180, to=180,resolution=1,variable = rotate,orient=HORIZONTAL)
rotation.grid(column=4, row=60)
setsat = Button(frame4, text="DONE",bd=4)
setsat.grid(column=4,row=61)

#CROP AND FLIP BUTTONS


p1=Entry(frame3, width = 10)
p1.grid(column=3,row=20) 


Label(frame3, text = "x").grid(column = 4, row = 20) 
p2=Entry(frame3, width = 10)
p2.grid(column=5,row=20)

crop = Button(frame3, text="Crop", fg="brown")
crop.grid(column=6,row=20, pady=10)

lftflip = Button(frame3, text="LEFT FLIP",  fg="black",bd=5)
lftflip.grid(column=3,row=3,padx=30, pady=10)

rightflip = Button(frame3, text="RIGHT FLIP", fg="black",bd=5)
rightflip.grid(column=5,row=3,padx=30, pady=10)


#window to import image for editing

frame5 = Frame(master,bd=2, width = 800, height =800)
frame5.pack(side=LEFT, expand = 1)

canvas = Canvas(frame5, width = 600, height = 600,bg="black")
canvas.pack()



mainloop()