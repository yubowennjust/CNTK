# Flappy Bird using Keras and Reinforcement Learning

In CNTK 203 tutorial, we have introduced the basic concepts of reinforcement
learning. In this tutorial, we show an easy way to train a popular game called
FlappyBird using Deep Q Network (DQN). This tutorial draws heavily on the
[original work](https://yanpanlau.github.io/2016/07/10/FlappyBird-Keras.html)
by Ben Lau on training the FlappyBird game with Keras frontend. This tutorial
used the CNTK backend and with very little change (commenting out a few specific
  references to TensorFlow) in the original code.

![](animation1.gif)

# Goals

The key objective behind this example is to show how to:
- Use CNTK backend API with Keras frontend
- Interchangeably use models trained between TensorFlow and CNTK via Keras
- Train and test (evaluate) the FlappyBird game using a simple DQN implementation.

# Pre-requisite

This example takes a dependency on the following python packages:
- keras
- pygame
- scikit-learn

These packages need to be installed by running `pip install <pkgname>`.

Additionally, one need to point Keras to use CNTK as the backend engine.


# How to run?

From the example directory, run:

```
python FlappyBird_with_keras_DQN.py -m "Run"
```

Note: if you run the game first time in "Run" mode a pre-trained model is
locally downloaded. Note, this model was trained with TensorFlow backend.

If you want to train the network from beginning, delete the locally cached
`FlappyBird_model.h5` (if you have a locally cached file) and run

```
python FlappyBird_with_keras_DQN.py -m "Train"
```

# Brief recap

The code has 4 steps:

1. Receive the image of the game screen as pixel array
2. Process the image
3. Use a Deep Convolutional Neural Network (CNN) to predict the best action
(flap up or down)
4. Train the network (millions of times) to maximize flying time

The details of the explanation can be found in Ben Lau's
[original work](https://yanpanlau.github.io/2016/07/10/FlappyBird-Keras.html)
