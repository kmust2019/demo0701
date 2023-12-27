import sys
for path in sys.path:
    print (path)

from phone.apple import iphone6
from phone.apple import iphone7
from phone.samsung.note import  galaxy_note8
from phone.samsung.s import  galaxy_s7

iphone6.askPrice()
iphone7.askPrice()
galaxy_note8.askPrice()
galaxy_s7.askPrice()