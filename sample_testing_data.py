from generate_data import Generate_Trainning_Data, Generate_Testing_Data
from model import Get_Trained_Model
from utilities import Load_Sampled_Data
import tensorflow as tf
import numpy as np

#Getting Training Data and training model
X, Y  = Generate_Trainning_Data()
speed_model = Get_Trained_Model(X, Y)

#Getting Testing Data and sampling from model
X = Generate_Testing_Data()
Y = tf.reshape(speed_model(X), [-1])

Y = tf.make_ndarray(tf.make_tensor_proto(Y))
Y = Y.tolist()
Y = [Y[0]] + Y

#Loading Sampled Data
Load_Sampled_Data(Y)