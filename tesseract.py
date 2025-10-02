import pytesseract as tess
from PIL import Image

#Check Available Languages
print(tess.get_languages(config=''))

print(tess.image_to_string(Image.open("indonesian_text.png"), lang='ind'))
