
#4-resize image 

from PIL import Image
!pip install python-resize-image
from resizeimage import resizeimage




# create list of  files name 
import glob, os
filesNames_CubeControl=[]

os.chdir("/content/drive/MyDrive/pentagon_data_pic/without pressure/patient")

for file in glob.glob("*.png"):
    filesNames_CubeControl.append(file)



#reszie process for control



for imagee in filesNames_CubeControl:
    with open(imagee, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_contain(image, [64,64])
            cover.save("/content/drive/MyDrive/pentagon_data_pic/without pressure/64×64/patient/{}.png".format(imagee),image.format)



# create list of  files name 
import glob, os
filesNames_CubePatient=[]

os.chdir("/content/drive/MyDrive/pentagon_data_pic/without pressure/control")
for file in glob.glob("*.png"):
    filesNames_CubePatient.append(file)


#resize process for patients


for imagee in filesNames_CubePatient:
    with open(imagee, 'r+b') as f:
        with Image.open(f) as image:
            cover = resizeimage.resize_contain(image, [64,64])
            cover.save("/content/drive/MyDrive/pentagon_data_pic/without pressure/64×64/control/{}.png".format(imagee), image.format)