# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"max.png")

# applying the min filter
im2 = im1.filter(ImageFilter.MinFilter(size = 5))



im2.show()
