from PIL import Image
# im = Image.open("indonesian_text.png")
im = Image.open("KK/halaman_1_kk.png")

width, height = im.size
# left, upper, right, lower

# get the middle point
mid_x = width // 2
mid_y = height // 2

# determine which area to crop
box_s1 = (0,0, mid_x, mid_y)
box_s2 = (mid_x,0, width, mid_y)
box_s3 = (0, mid_y, mid_x, height)
box_s4 = (mid_x, mid_y, width, height)

# crop
s1=im.crop(box_s1)
s2=im.crop(box_s2)
s3=im.crop(box_s3)
s4=im.crop(box_s4)

# print(im.format, width, im.mode)
s1.show()