#! /usr/bin/env python3
import tensorflow as tf
tf.enable_eager_execution()
tf.add(1, 2).numpy()
hello = tf.constant('Hello, TensorFlow!')
print(hello.numpy())
