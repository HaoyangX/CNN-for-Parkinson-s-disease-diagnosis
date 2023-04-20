
#4-augmentation images
from keras.preprocessing.image import ImageDataGenerator,image_utils
#  array_to_img, , load_img



datagen = ImageDataGenerator(
        rotation_range=40,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')



# create list of  files name 
import glob, os
filesNames_CubeControl=[]

os.chdir("/content/drive/MyDrive/pentagon_data_pic/without pressure/64×64/control")

for file in glob.glob("*.png"):
    filesNames_CubeControl.append(file)


#augmentation process for control
path="/content/drive/MyDrive/pentagon_data_pic/without pressure/64×64/Augmentation/control"
for imageName in filesNames_CubeControl:
    img = image_utils.load_img(imageName)  # this is a PIL image
    x = image_utils.img_to_array(img) 
    x = x.reshape((1,) + x.shape)
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                          save_to_dir=path, save_prefix='Aug', save_format='png'):
        i += 1
        if i > 22:
            break  # otherwise the generator would loop indefinitely


# create list of  files name 
import glob, os
filesNames_CubePatient=[]
os.chdir("/content/drive/MyDrive/cube_data_pic/without pressure/64×64/patient")

for file2 in glob.glob("*.png"):
    filesNames_CubePatient.append(file2)



#augmentation process for paitents

path2="/content/drive/MyDrive/cube_data_pic/without pressure/64×64/Augmentation/patient"
for imageName2 in filesNames_CubePatient:
    img2 = image_utils.load_img(imageName2)  # this is a PIL image
    x2 = image_utils.img_to_array(img2) 
    x2 = x2.reshape((1,) + x2.shape)
    i2 = 0
    for batch2 in datagen.flow(x2, batch_size=1,
                          save_to_dir=path2, save_prefix='Aug', save_format='png'):
        i2 += 1
        if i2 > 10:
            break  # otherwise the generator would loop indefinitely
