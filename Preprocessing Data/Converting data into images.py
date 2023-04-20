

#Converting data into images
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import requests
import io
from sklearn.metrics import mean_squared_error
import operator
import csv
import datetime

#to make sequre images
matplotlib.rcParams['figure.figsize'] = (4, 4)



#create list of new files name 
import glob, os
filesNames_NewCubeControl=[]
os.chdir("/content/drive/MyDrive/cube_data_num/without pressure/patient")
for file in glob.glob("*.txt"):
    filesNames_NewCubeControl.append(file)



#link of the images folder
#draw and save the CubeControl images

for name in filesNames_NewCubeControl:
    x = pd.read_csv(    name, sep=',',usecols=[1]    )
    y = pd.read_csv(    name, sep=',',usecols=[2]    )
    plt.scatter(x, y)
    plt.axis('off')
    plt.savefig('/content/drive/MyDrive/cube_data_pic/without pressure/patient/{}.png'.format(name))
    plt.close()



filesNames_CubePatients=[]
os.chdir('/content/drive/MyDrive/cube_data_num/with pressure/patient')
for file in glob.glob("*.txt"):
    filesNames_CubePatients.append(file)


#draw and save the CubePatients images
for name in filesNames_CubePatients:
    x = pd.read_csv(    name, sep=',',usecols=[1]    )
    y = pd.read_csv(    name, sep=',',usecols=[2]    )
    plt.scatter(x, y)
    plt.axis('off')
    plt.savefig('/content/drive/MyDrive/cube_data_pic/with pressure/patient/{}.png'.format(name))
    plt.close()



filesNames_PentagonControl=[]
os.chdir('/content/drive/MyDrive/pentagon_data_num/with pressure/control')
for file in glob.glob("*.txt"):
    filesNames_PentagonControl.append(file)



#draw and save the PentagonControl images
for name in filesNames_PentagonControl:
    x = pd.read_csv(    name, sep=',',usecols=[1]    )
    y = pd.read_csv(    name, sep=',',usecols=[2]    )
    plt.plot(x, y)
    plt.axis('off')
    plt.savefig('/content/drive/MyDrive/pentagon_data_pic/with pressure/control/{}.png'.format(name))
    plt.close()


filesNames_PentagonPatient=[]
os.chdir('//content/drive/MyDrive/pentagon_data_num/with pressure/patient')
for file in glob.glob("*.txt"):
    filesNames_PentagonPatient.append(file)

#draw and save the PentagonPatient images

for name in filesNames_PentagonPatient:
    x = pd.read_csv(    name, sep=',',usecols=[1]    )
    y = pd.read_csv(    name, sep=',',usecols=[2]    )
    plt.plot(x, y)
    plt.axis('off')
    plt.savefig('/content/drive/MyDrive/pentagon_data_pic/with pressure/patient/{}.png'.format(name))
    plt.close()

