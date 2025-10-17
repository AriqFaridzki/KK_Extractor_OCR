from PIL import Image;
import cv2;
import pytesseract;

im = Image.open("KK/halaman_1_kk.png")
img = cv2.imread("KK/halaman_1_kk.png")


# 2. Define the Cropping Boxes (left, upper, right, lower)

# A. KK Number

box_member_list = img[400:1050, 1:4500]
# B. Household

# left, upper, right, lower
box_household = img[220:400, 394:4500]

# C. List Anggota
box_kk_number = img[110:230, 952:2500]

# D. Additional Info
box_additional_info = img[1000:1700, 1:4500]

# E. Publish Date
box_publish_date = img[1750:1850, 1:1000]

# kk_number = im.crop((box_kk_number))
# list_anggota = im.crop((box_list_anggota))
# additional_info = im.crop((box_additional_info))
# publish_date = im.crop((box_publish_date))

# publish_date.show()
 
# select image region to crop ( GUI )
# roi = cv2.selectROI("Select ROI", img, False)
# cropped_img = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
# cv2.imwrite("Cropped.png", cropped_img)
def previewImage(coordinates):
    # resize_img = cv2.resize(coordinates, (1380, 720))
    # cv2.imshow("Test window", resize_img)
    cv2.imshow("Publish Date", coordinates)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
kk_number_text = pytesseract.image_to_string(box_kk_number, lang='ind', config='--psm 6')
print("\n--- OCR Result for KK Number ---")
    
# previewImage(box_publish_date)
# previewImage(box_household)
# previewImage(box_additional_info)
# previewImage(box_member_list)
# previewImage(box_kk_number)
