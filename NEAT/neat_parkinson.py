# -*- coding: utf-8 -*-
"""NEAT_Parkinson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fgTeaOIUJLHJuEb2qlQuxfn-9pciQBCE
"""

import sys
sys.path.append('/content/drive/MyDrive/neat-python-master/examples/xor')
import os
import cv2
import numpy as np
import matplotlib
# !pip uninstall numpy
# !pip install numpy==1.16
from sklearn.model_selection import train_test_split

!pip install neat-python

import neat
import visualize

# Load data
data = []
label = []
patient_path = "/content/drive/MyDrive/pentagon_data_pic/without pressure/32×32/patient"
control_path = "/content/drive/MyDrive/pentagon_data_pic/without pressure/32×32/control"
for filename in os.listdir(patient_path):
  image = cv2.imread(os.path.join(patient_path, filename), cv2.IMREAD_GRAYSCALE)
  image = cv2.resize(image, (32, 32))
  data.append(image.flatten())
  # data.append(image)
  label.append(0)

for filename in os.listdir(control_path):
  image = cv2.imread(os.path.join(control_path, filename), cv2.IMREAD_GRAYSCALE)
  image = cv2.resize(image, (32, 32))
  data.append(image.flatten())
  # data.append(image)
  label.append(1)


data = np.array(data)
label = np.array(label)

x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.2, random_state=None)
# Random number seed to be applied to shuffle the data before splitting. Can be int, RandomState instance or None.
#The default value = None. set to a fixed value means that for the same dataset, only the first run is random, 
#and subsequent splits will have the same result as long as the rondom_state is the same.
x_train = x_train / 255.0
x_test = x_test / 255.0


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = 0.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(x_train, y_train):
            output = net.activate(xi)
         
            # genome.fitness -= (output[0] - xo[0]) ** 2
            if output[0]-xo == 0:
              genome.fitness+=1
            else:
              genome.fitness-=1

def run(config_file):
    # Load configuration.
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(eval_genomes,18)

    # Display the winning genome.
    print('\nBest genome:\n{!s}'.format(winner))

    # Show output of the most fit genome against training data.
    print('\nOutput:')
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    correct = 0
    total = 0
    for xi, xo in zip(x_test, y_test):
        output = winner_net.activate(xi)
        prediction = round(output[0])
        if prediction == xo:
          correct += 1
        total += 1
        print("correct=%f"%correct)
        print("total=%f"%total)
        print("Accuracy: {}%".format((correct/total)*100))
        print('----------')
     
       
    node_names = {-1: 'input', -2: 'output'}
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.draw_net(config, winner, True, node_names=node_names)
    visualize.plot_stats(stats, ylog=False, view=True)
    visualize.plot_species(stats, view=True)

    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-4')
    p.run(eval_genomes, 18)


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname("/content/drive/MyDrive/neat-python-master/examples/xor/config-feedforward")
    config_path = os.path.join(local_dir, 'config-feedforward')
    run(config_path)

from google.colab import drive
drive.mount('/content/drive')