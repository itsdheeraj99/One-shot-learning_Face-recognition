# Siamese Neural Network for One-shot Image Recognition

## Project Description:

One-shot image recognition is a challenging computer vision task where the goal is to recognize or classify objects with minimal training examples – often just a single example per class. This project presents a powerful solution using Siamese Neural Networks, a deep learning architecture specifically designed for one-shot learning scenarios.

### Key Features:

**Siamese Neural Network:** This project implements a Siamese neural network, a unique architecture that learns to differentiate between pairs of images efficiently.

**One-shot Learning:** Conventional deep learning models require extensive training data for each class, but our Siamese network excels in recognizing new classes with very few examples.

**Customizable:** The codebase is highly customizable, allowing users to adapt it to various one-shot learning tasks.

**Evaluation Metrics:** Comprehensive evaluation metrics have been performed to assess the model's performance, including accuracy, precision, recall, and F1-score.

## Usage
- Install the required dependencies ```pip install -r requirements.txt```
- Load the model ```FaceID_model = tf.keras.models.load_model('Final_FACEID_model')```
- Create a folder ``application_data`` 
- further create two folders ``input_images`` and ``verification_images`` within this folder. 
- Store the verifying image against which the input image has to be validated in the ``verification_images`` folder.
- Run the code contained in the ``Testing.py``  
- When the webcam gets activated press the key ``v`` to capture the image and key ``q`` to close the image capturing window. 


## Overview: 
The core methodology employed in this project is based on Siamese Neural Networks, a specialized type of neural network architecture designed for one-shot image recognition tasks. One-shot learning is a challenging problem where the objective is to recognize new objects or classes with very limited training examples, often just one per class. Siamese networks excel in this context by learning to measure the similarity or dissimilarity between pairs of input images.

![Network](https://github.com/itsdheeraj99/One-shot-learning_Face-recognition/assets/141077081/81d6be07-cd73-49ad-9202-f8b9c9e12f47)

### Siamese Neural Networks:

The fundamental concept of Siamese networks is to use two identical subnetworks (hence the name "Siamese") that share the same architecture and weights. These subnetworks take two input images, often referred to as the "anchor" and the "comparison" images, and produce embeddings (feature vectors) for each input. The embeddings are then compared using a distance metric to determine the similarity between the two images.

### Training:

During the training phase, the Siamese network learns to minimize the distance between embeddings of similar images (images of the same class) while maximizing the distance between embeddings of dissimilar images (images of different classes). This process helps the network learn to discriminate between different classes, even with minimal training data.

### Inference:

In the inference phase, the trained Siamese network can be used for one-shot image recognition. Given a new image and a set of reference images, the network computes embeddings for each of them and selects the reference image with the closest embedding (lowest distance) to the new image as the recognized class or object.

## References
Siamese Neural Networks for One-shot Image Recognition Paper published in 2015
