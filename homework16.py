'bu bytes datasını UTF-16 ilə decode edib, ekranda göstərin.'
# name =  b'\xff\xfef\x00e\x00r\x00m\x00a\x00' 
# print(name.decode('utf-16'))


png = open('hide-image.rar', 'rb')
png_source = png.read()
# png_source = png_source[::-1]
print(png_source)