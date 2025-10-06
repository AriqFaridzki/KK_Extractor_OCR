from PIL import Image;
import cv2 as cv

im = Image.open("KK/halaman_1_kk.png")

# 2. Define the Cropping Boxes (left, upper, right, lower)

# A. KK Number
box_kk_number = (1165, 120, 2420, 210)

# B. Household

# left, upper, right, lower

box_household = (458, 220, 3000, 394)

# C. List Anggota
box_list_anggota = (88, 390, 3472, 1052)

# D. Additional Info
box_additional_info = (84, 1034, 3476, 1718)

# E. Publish Date
box_publish_date = (102, 1797, 920, 1847)

kk_number = im.crop((box_kk_number))
list_anggota = im.crop((box_list_anggota))
additional_info = im.crop((box_additional_info))
publish_date = im.crop((box_publish_date))

publish_date.show()