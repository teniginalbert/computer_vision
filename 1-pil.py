from pathlib import Path
p = Path("python3.4").resolve()
str(p)

from PIL import Image
import os

pil_im = Image.open('/home/alberttenigin/Pictures/Wallpapers/118509.jpg').\
    convert('L')
    
#converting to jpg    
for infile in filelist:
    outrile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print("не могу преобразовать", infile)
 
#returns all names of jpg files in catalogue  
def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path)
                                  if f.endswith('.jpg')]

#miniature
pil_im.thumbnail((128,128))

#copying and cropping
box = (100, 100, 400, 400) #left, up, right, down
region = pil_im.crop(box)

#rotating and placing to the box
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)

#resize and rotate
out = pil_im.resize((128, 128))
out = pil_im.rotate(45)