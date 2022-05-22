from PIL import Image, ImageEnhance

#read the image
im = Image.open("noise.jpg")

#image brightness enhancer
enhancer = ImageEnhance.Brightness(im)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.show('original-image.png')

factor = 0.5 #darkens the image
im_output = enhancer.enhance(factor)
im_output.show('darkened-image.png')

factor = 1.5 #brightens the image
im_output = enhancer.enhance(factor)
im_output.show('brightened-image.png')