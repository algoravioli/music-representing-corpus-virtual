import tensorflow as tf
import numpy as np


class Creator:
    def __init__(self):
        pass

    def create_model(self, n_layers, layer_size, input_output_size, activation="tanh"):
        # The input shape will always be 1000
        # The output shape will also always be 1000
        # The number of layers and the size of each layer will be determined by the user
        # The activation function will also be determined by the user

        model = tf.keras.models.Sequential()
        for i in range(n_layers):
            if i == 0:
                model.add(
                    tf.keras.layers.Dense(
                        layer_size,
                        activation=activation,
                        input_shape=(input_output_size,),
                    )
                )
            model.add(tf.keras.layers.Dense(layer_size, activation=activation))
        model.add(tf.keras.layers.Dense(input_output_size, activation="tanh"))

        model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mse"])
        model.build()
        model.summary()
        return model
