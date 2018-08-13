import sys

from PIL import Image


if len(sys.argv) > 1:
    filename = sys.argv[1]

img = Image.open(filename)
area1 = (960, 290, 1180, 650)
area2 = (930, 610, 1250, 700)
crop1 = img.crop(area1)
crop2 = img.crop(area2)

crop1.show()
crop2.show()


if filename.endswith('1st.jpg'):
    filename = filename[:-7]

newpath1 = (filename + "/" + "ph.jpg")

crop1.save(newpath1)

newpath2 = (filename + "/" + "sgn.jpg")

crop2.save(newpath2)




