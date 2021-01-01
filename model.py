import tensorflow as tf
from tensorflow import keras

class Speed_Model(keras.Model):
    def __init__(self):
        super(Speed_Model, self).__init__()

        self.conv_layer = keras.Sequential(
            [
                keras.layers.Conv2D(32, 3, activation="relu", input_shape=(255,255,3)),
                keras.layers.MaxPooling2D(),
                keras.layers.Conv2D(32, 3, activation="relu"),
                keras.layers.MaxPooling2D(),
                keras.layers.Conv2D(32, 3, activation="relu"),
                keras.layers.MaxPooling2D(),
                keras.layers.Flatten(),
            ]
        )

        self.recurrent_layer = keras.layers.LSTM(1)

    def call(input):
        img_1 = input[0]
        img_2 = input[1]

        conv_img_1 = self.conv_layer(img_1)
        conv_img_2 = self.conv_layer(img_2)

        recurrent_input = tf.stack(
            [
                tf.reshape(conv_img_1, (conv_img_1.shape[-1],)),
                tf.reshape(conv_img_2, (conv_img_2.shape[-1],)),
            ]
        )

        return self.recurrent_layer(recurrent_input)