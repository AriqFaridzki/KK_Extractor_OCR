from PIL import Image
# import cv2 
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# print(pytesseract.get_languages(config=''))


# pre_image = cv2.imread("KK/halaman_1_kk.png")
# image_gray = cv2.cvtColor(pre_image, cv2.COLOR_BGR2GRAY)
# im = cv2.GaussianBlur(image_gray, (5, 5), 0)

# im = Image.open("KK/halaman_1_kk.png")

im = Image.open("KK/halaman_1_kk.png")
im_gray = im.convert("L")
# 2. Define the Cropping Boxes (left, upper, right, lower)


# A. KK Number
box_kk_number = (1165, 120, 2420, 210)

# B. Household
box_household = (458, 220, 3000, 394)

# C. List Anggota
box_list_anggota = (88, 390, 3472, 1052)

# D. Additional Info
box_additional_info = (84, 1034, 3476, 1718)

# E. Publish Date
box_publish_date = (102, 1797, 920, 1847)

kk_number = im_gray.crop((box_kk_number))
list_anggota = im_gray.crop((box_list_anggota))
additional_info = im_gray.crop((box_additional_info))
publish_date = im_gray.crop((box_publish_date))

# A. OCR for KK Number
print(pytesseract.image_to_string(kk_number, lang='ind'))
# print("\n--- OCR Result for KK Number ---")
# print(kk_number_text) # .strip() removes potential leading/trailing whitespace

# B. OCR for List Anggota
# Use 'lang' parameter if your text is in a specific language (e.g., 'ind' for Indonesian)
# anggota_text = pytesseract.image_to_string(list_anggota, lang='ind') 
# print("\n--- OCR Result for List Anggota ---")
# print(anggota_text)

# list_anggota.show()

# print(kk_number)