import pyqrcode
import random

r = lambda: random.randint(0,255)

print('Ваш текст:')
text = input()
url = pyqrcode.create(str(text))
url.svg('qr.svg', scale=8, background='#%02X%02X%02X' % (r(),r(),r()), module_color='#%02X%02X%02X' % (r(),r(),r()))
print(url.terminal(quiet_zone=1))