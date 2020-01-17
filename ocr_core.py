# Importing 'Image' from the 'Pillow' library and the 'pytesseract' library
try:
	from PIL import Image
except ImportError:
	import Image

import pytesseract



def ocr_core(filename):
	'''
	This function will handle the the core OCR processing of images and returns
	the text stored in the image
	'''

	# Using Pillow's Image class to open the image and pytesseract to detect 
	# the string in the image
	text = pytesseract.image_to_string(Image.open(filename));
	return text;

# print(ocr_core('images/google.png'))





'''
# Keep count of each kind of book that's being shelved into respective areas 
category_Count = {
	'gen_stacks': 0,
	'juv': 0,
	'ref': 0,
	'film': 0,
	'magazines': 0,
	'videos': 0,
}

print('Category Count Object: ', category_Count);
'''