import pytesseract
from PIL import Image

print(pytesseract.get_languages(config=''))

im_test=Image.open("indonesian_text.png")
box_test= (0,0,500,500)
test = im_test.crop((box_test))
test.show()

print(pytesseract.image_to_string(test, lang='ind'))