import pytesseract
from PIL import Image

#Check Available Languages
print(pytesseract.get_languages(config=''))

#testing
im_test=Image.open("indonesian_text.png")
box_test= (0,0,500,500)
test = im_test.crop((box_test))
# test.show()

# print(pytesseract.get_languages(config=''))


# pre_image = cv2.imread("KK/halaman_1_kk.png")
# image_gray = cv2.cvtColor(pre_image, cv2.COLOR_BGR2GRAY)
# im = cv2.GaussianBlur(image_gray, (5, 5), 0)

# im = Image.open("KK/halaman_1_kk.png")

im = Image.open("KK/halaman_1_kk.png")
im_gray = im.convert("L")
# 2. Define the Cropping Boxes (left, upper, right, lower)

kk_coords = {
    "box_kk_number": (1165, 120, 2420, 210),
    "box_household": (458, 220, 3000, 394),
    "box_list_anggota_1": (88, 390, 3472, 1052),
    "box_list_anggota_2": (88, 390, 1736, 1052),
    "box_additional_info": (84, 1034, 3476, 1718),
    "box_publish_date": (102, 1797, 920, 1847)
    }


kk_number = im_gray.crop(kk_coords["box_kk_number"])
household = im_gray.crop(kk_coords["box_household"])
list_anggota_1 = im_gray.crop(kk_coords["box_list_anggota_1"])
list_anggota_2 = im_gray.crop(kk_coords["box_list_anggota_2"])
additional_info = im_gray.crop(kk_coords["box_additional_info"])
publish_date = im_gray.crop(kk_coords["box_publish_date"])

kk_cropped_images = {
    "fix_kk_number": kk_number,
    "fix_household": household,
    "fix_list_anggota_1": list_anggota_1,
    "fix_list_anggota_2": list_anggota_2,
    "fix_additional_Info": additional_info,
    "fix_publish_Date": publish_date
}

print("\n--- OCR Result for KK Number ---")
kk_cropped_images["fix_list_anggota_1"].show()
# print(pytesseract.image_to_string(kk_cropped_images["List_Anggota"], lang='ind'))

# for cropped_image in kk_cropped_images.items():
#     print(f"\n--- OCR Result for {cropped_image[0]} ---")
#     print(pytesseract.image_to_string(cropped_image[1], lang='ind'))

# print(pytesseract.image_to_string(Image.open("indonesian_text.png"), lang='ind'))

#show me to handle cropped after processed by PIL and use tesseract to read the text
#for loop to read all cropped images
# for key, cropped_image in 
#     print(f"\n--- OCR Result for {key} ---")
#     print(pytesseract.image_to_string(cropped_image, lang='ind'))
# # print(pytesseract.image_to_string(publish_date, lang='ind'))
