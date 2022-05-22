# Importing Image and ImageFilter module from PIL package
from PIL import Image, ImageFilter

# creating a image object
im1 = Image.open(r"max.png")

# applying the max filter
im2 = im1.filter(ImageFilter.MaxFilter(size = 5))
im1.show()

im2.show()
