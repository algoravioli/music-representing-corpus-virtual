import tensorflow as tf
import numpy as np


class Creator:
    def __init__(self):
        pass

    def createDenseModelForNeuralNet2(
        self, n_layers, layer_size, input_output_size, activation="tanh"
    ):
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
            dropoutFlag = np.random.randint(0, 2)
            if dropoutFlag == 1:
                model.add(tf.keras.layers.Dropout(0.5))
            model.add(tf.keras.layers.Dense(layer_size, activation=activation))
        model.add(tf.keras.layers.Dense(input_output_size, activation="tanh"))

        model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mse"])
        model.build()
        model.summary()
        return model

    def createGRUModelForNeuralNet2(
        self, n_layers, layer_size, input_output_size, activation="tanh"
    ):
        # This model uses an RNN

        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(input_output_size,)))
        model.add(tf.keras.layers.Reshape((1, input_output_size)))
        for _ in range(n_layers):
            model.add(
                tf.keras.layers.GRU(
                    layer_size, return_sequences=True, activation=activation
                )
            )
        model.add(tf.keras.layers.Dense(input_output_size, activation="tanh"))

        model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mse"])
        model.build()
        model.summary()
        return model

    def createCNNModelForNeuralNet2(
        self, n_layers, layer_size, input_output_size, activation="tanh"
    ):
        # This model uses a CNN
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(input_output_size,)))
        model.add(tf.keras.layers.Reshape((input_output_size, 1)))
        for _ in range(n_layers):
            model.add(
                tf.keras.layers.Conv1D(
                    kernel_size=layer_size,
                    filters=layer_size,
                    activation=activation,
                    dilation_rate=layer_size,
                )
            )
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(input_output_size, activation="tanh"))

        model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mse"])
        model.build()
        model.summary()
        return model

    #########################
    #########################
    #########################
    #########################
    #########################

    def createModelForNeuralNet3(self, n_layers, n_inputs, activation="tanh"):
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(n_inputs,)))
        model.add(tf.keras.layers.Reshape((1, n_inputs)))
        for _ in range(n_layers):
            model.add(
                tf.keras.layers.GRU(
                    n_inputs, return_sequences=True, activation=activation
                )
            )
        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(1, activation="tanh"))

        model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mse"])
        model.build()
        model.summary()
        return model

    #########################
    #########################
    #########################
    #########################
    #########################

    def createDenseModelForNeuralNet4(
        self, n_layers, layer_size, input_size, output_size
    ):
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(input_size,)))
        model.add(tf.keras.layers.Reshape((1, input_size)))
        for _ in range(n_layers):
            model.add(tf.keras.layers.Dense(layer_size, activation="tanh"))
        model.add(tf.keras.layers.Dense(output_size, activation="tanh"))

        model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mse"])
        model.build()
        model.summary()
        return model

    #########################
    #########################
    #########################
    #########################
    #########################

    def createEarlyStopper(self):
        self.callback = tf.keras.callbacks.EarlyStopping(
            monitor="loss", min_delta=0.0001, patience=5, verbose=1, mode="auto"
        )
        return self.callback
