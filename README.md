Parkinson's disease is a condition that has a wide global distribution and is more difficult to diagnose upfront. This project is a code that aims to apply deep learning to the early diagnosis of Parkinson's disease. Due to the excellent performance of CNN models in image processing, this project compares the training effect of NEAT and Alissa CNN with the same input data.

In the preprocessing folder is a series of processes performed on the data, which includes converting the initial time series data into image form and increasing the amount of data by Augmentation and changing the number of pixels in the image by resize. Changes can also be made to the Create Add headers to data to decide whether to add zero-pressure information.

The Alissa CNN and NEAT folders are the main part of the training code, which is used to obtain the final training results after pre-processing the data and to analyse them for comparison.
