import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split

#This is the definition of the model. It's
#basically several convolutional layers
#applied on two consecutive frames in order
#to extract relevant features from each
#and an LSTM network that reads the concatenated
#vectors in order to finally compute the speed
#at the given frame

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

def Get_Trained_Model(X, Y):
    print("Get_Trained_Model: Breaking data down into training and validation")
    X_Train, X_Valid, Y_Train, Y_Valid = train_test_split(X, Y, test_size=0.2)
    
    print("Get_Trained_Model: Instantiating model, compiling, and fitting")
    model = Speed_Model()
    model.compile(loss="mean_squared_error", optimizer="adam", metrics=["accuracy"])
    model.fit(X_Train, Y_Train, epochs=10, validation_data=(X_Valid, Y_Valid))
    return model