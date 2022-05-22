from tkinter import *
from tkinter.font import Font
# from typing import Counter
from PIL import Image,ImageTk,ImageFilter
from tkinter import filedialog as fd
import cv2
import numpy as np
#importing local python file
# import mimage_sharpen

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x720")
        self.resizable(width=True, height=False)
        self.title("PixelMod")
        # self.configure(background="black")
        
        #Creating top frame
        self.topframe = Frame(self,height=100,bd=5,bg="black")
        self.topframe.pack(fill=X)
        
        #creating mainframe
        self.mainframe = Frame(self)
        self.mainframe.pack(fill=BOTH,expand=True)
        
        #Creating left and right frame under mainframe
        self.leftframe = Frame(self.mainframe,bd=10,width=600)
        self.leftframe.pack(fill=Y,side=LEFT)
        
        self.rightframe = Frame(self.mainframe,bd=10, width=600)
        self.rightframe.pack(fill=Y,side=RIGHT)
        
        #creating button and dropdown menu for top frame
        self.uploadButton = Button(
            self.topframe, text="Upload image", command=self.uploadfile,fg="white",width=7, bg="#40bf90", bd=0)
        self.uploadButton.pack(side=LEFT,ipadx=15,ipady=15,padx=20,pady=5)
        
        # self.saveButton = Button(self.topframe,text="Save",command=self.save_image,fg="white",width=7,bg="#40bf90",bd=0)
        # self.saveButton.pack(side=LEFT,ipadx=15,padx=20,pady=5)
        #Dropdown options
        options = [
            "Negative Image",
            # "Filtering with morphological operators",
            # "Histogram equalization",
            "Smoothing filter",
            # "Linear contrast adjustment",
            "Denoising",
            "Sharpening",
            "Log Transformation",
            # "Unsharp mask filtering",
            "Image sharpening"
        ]
        #variable selected options
        self.clicked = StringVar()
        self.clicked.set(options[0])
        drop = OptionMenu(self.topframe,self.clicked, *options)
        drop.place(relx=0.5,rely=0.5,anchor=CENTER)
        # print(clicked.get())
        
        #Apply button
        self.applyButton = Button(
            self.topframe, text="Apply", command=self.callfilter, fg="white",width=7, bg="#40bf90", bd=0)
        self.applyButton.pack(side=RIGHT,ipadx=15,ipady=15,padx=20,pady=5)
    
    #Creating new window for smoothing filter
    
        
    #Methods for Implementation
    def uploadfile(self):
        self.name = fd.askopenfilename()
        self.image = Image.open(self.name)
        self.image = self.image.resize((600, 600), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        #clear frame before entering new image.
        for item in self.leftframe.winfo_children():
            item.destroy()
        image_label1 = Label(self.leftframe, image=self.photo)
        image_label1.pack()
        print(self.name)
    
    #for showing output
    def showOutput(self,img=None):
        
        for item in self.rightframe.winfo_children():
            print(item)
            item.destroy()
        img =cv2.resize(img,(600,600))
        self.photo1 = ImageTk.PhotoImage(Image.fromarray(img))
        image_label2 = Label(self.rightframe, image=self.photo1)
        image_label2.pack()
        
    def callfilter(self):
        print(self.clicked.get())
        if(self.clicked.get() == "Histogram equalization"):
            self.histogram()
        if(self.clicked.get() == "Filtering with morphological operators"):
            pass
        if(self.clicked.get() == "Smoothing filter"):
            #calling new window
            self.smoothing_window()
        
        if(self.clicked.get() == "Linear contrast adjustment"):
            pass
        if(self.clicked.get() == "Sharpening"):
            self.sharpening_window()
        
        if(self.clicked.get() == "Log Transformation"):
            self.logtransformation()
            
        if(self.clicked.get() == "Image sharpening"):
            self.imageSharpen()
        if(self.clicked.get()== "Negative Image"):
            self.imagenegative()
        
        if(self.clicked.get() == "Denoising"):
            self.denoisingimage()
            
    
    def smoothing_window(self):
        # print("window called")
        top = Toplevel()
        top.geometry("200x200")
        top.resizable(width=False, height=False)
        top.configure(background="#768979")
        box_btn = Button(top, text="Box filtering", command=self.boxfilter,
                         width=13, bd=0, bg="#28ee11").pack(pady=5, ipadx=5, ipady=2)
        gau_btn = Button(top, text="Gaussian filtering",
                         command=self.gaussianfilter, width=13, bd=0, bg="#28ee11").pack(pady=5, ipadx=5, ipady=2)
        med_btn = Button(top, text="Median filtering",
                         command=self.medianfiltering, width=13, bd=0, bg="#28ee11").pack(pady=5, ipadx=5, ipady=2)
        # max_btn = Button(top, text="Max filtering",
                        #  command=self.maxfilter, width=13,bd=0).pack(pady=5,ipadx=5,ipady=2)
        avg_btn = Button(top, text="Averaging filter",
                         command=self.averagingfilter, width=13, bd=0, bg="#28ee11").pack(pady=5, ipadx=5, ipady=2)
        # exit_btn = Button(top, text="Exit", width=13,bd=0).pack(pady=5,ipadx=5,ipady=2)  # TODO:working
    
    def sharpening_window(self):
        top = Toplevel()
        top.geometry("200x200")
        top.resizable(width=False, height=False)
        Button(top, text="cannyalgorithm", command=self.cannyalgo,
               width=13, bd=0).pack(pady=5, ipadx=8, ipady=8)
        
    
    
        
    
    def histogram(self):
        print("histogram function worked.")

    def imageSharpen(self):
        images = np.array(Image.open(f"{self.name}"))
        gaussian_blur = cv2.GaussianBlur(images, (7, 7), 2)

        #sharpening using addweighted()
        sharpend1 = cv2.addWeighted(images, 3.5, gaussian_blur, -2.5, 0)
        # sharpenImage = mimage_sharpen.sharpenImage(self.name)
        self.showOutput(sharpend1)
    
    #image negative
    def imagenegative(self):
        img = cv2.imread(f"{self.name}")
        img1 = 255-img
        self.showOutput(img1)
    #log transformation
    def logtransformation(self):
        # Read an image
        image = cv2.imread(f"{self.name}")
        # Apply log transformation method
        c = 255 / np.log(1 + np.max(image))
        log_image = c * (np.log(image + 1))
        # Specify the data type so that
        # float value will be converted to int
        log_image = np.array(log_image, dtype=np.uint8)
        self.showOutput(log_image)
        
    def denoisingimage(self):
        img = cv2.imread(f"{self.name}")
        # denoising of image saving it into dst image
        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
        self.showOutput(dst)
        
    #Smoothing using Box filter function
    def boxfilter(self):
        img = cv2.imread(f"{self.name}")
        blur = cv2.blur(img, (3, 3))
        self.showOutput(blur)
    
    def gaussianfilter(self):
        img = cv2.imread(f"{self.name}")
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        self.showOutput(blur)

    def medianfiltering(self):
        img = cv2.imread(f"{self.name}")
        median = cv2.medianBlur(img, 5)
        self.showOutput(median)
        
    # def maxfilter(self):
    #     im1 = Image.open(rf"{self.name}") #TODO:correction
    #     # applying the max filter
    #     im2 = im1.filter(ImageFilter.MaxFilter(size=5))
    #     self.showOutput(im2)
    
    def averagingfilter(self):
        img = cv2.imread(f"{self.name}")
        kernel = np.ones((3, 3), np.float32)/9
        dst = cv2.filter2D(img, -1, kernel)
        self.showOutput(dst)
    
    # def minfilter(self):
    #     pass
    #     #TODO:
    
    def cannyalgo(self):
        img = cv2.imread(f"{self.name}")
        # Convert to graycsale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Blur the image for better edge detection
        img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
        # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        self.showOutput(edges)
        
    # def laplacianfilter(self):
    #     #TODO:
    #     img = f"{self.name}"
    #     print(self.name)
    #     image = Image.open(img)
    #     # # print(image)
    #     # # Converting the image to grayscale, as edge detection
    #     # # requires input image to be of mode = Grayscale (L)
    #     image = image.convert("L")

    #     # # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
    #     image = image.filter(ImageFilter.FIND_EDGES)
    #     self.showOutput(image)
    
    # def save_image(self):
    #     save_image = self.photo1
    #     image_filename = self.name
    #     cv2.imwrite(image_filename, save_image)
    
if __name__ == '__main__':
    #for full screen 
    # root.state('zoomed') 
    window = GUI()
    window.mainloop()
