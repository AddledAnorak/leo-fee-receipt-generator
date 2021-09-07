from PIL import Image, ImageDraw, ImageFont
  

def run(data, save=False, show=False):
	original_img = Image.open('template.png')

	path = f"receipt#{data['receipt-id']}.png"

	original_img.save(path)
	img = Image.open(path)

	i = ImageDraw.Draw(img)

	font_35 = ImageFont.truetype('Open_Sans/OpenSans-Light.ttf', 50)
	font_29 = ImageFont.truetype('Open_Sans/OpenSans-Bold.ttf', 42)
	
	i.text((798, 414), data['name'], font=font_35, fill=(0,0,0))
	i.text((798, 864), data['date'], font=font_35, fill=(0,0,0))
	i.text((798, 1003), data['payment-method'], font=font_35, fill=(0,0,0))
	i.text((798, 1152), data['trans-id'], font=font_35, fill=(0,0,0))

	i.text((1765, 209), data['receipt-id'], font=font_29, fill=(255,255,255))

	if show:
		img.show()

	if save:
		img.save(path)
	
	return path



if __name__ == '__main__':
	run(
		{
			'receipt-id': '001',
			'name': 'SHOAN RAJ',
			'date': '07/09/2021',
			'payment-method': 'Online (GPay)',
			'trans-id': 'T4357809493578945837'
		},
		save=True,
		show=False
	)
