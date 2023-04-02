import tensorflow as tf
import numpy as np


class Creator:
    def __init__(self):
        pass

    #########################
    #########################
    #########################
    #########################
    #########################

    def createModelForNeuralNet1(self, memory, params_multiplier=10):
        # This model is preset to have 4 different types of Inputs:
        # 1. startTimes
        # 2. ptiches
        # 3. velocities
        # 4. durations
        # The model will have 4 different outputs:
        # 1. startTimes
        # 2. pitches
        # 3. velocities
        # 4. durations

        startTimes = tf.keras.Input(shape=(memory,), name="startTimes")
        pitches = tf.keras.Input(shape=(memory,), name="pitches")
        velocities = tf.keras.Input(shape=(memory,), name="velocities")
        durations = tf.keras.Input(shape=(memory,), name="durations")

        # The model will concat each pair of inputs together and pass them to a dense network of 2 layers
        # sT+p, sT+v, sT+d, p+v, p+d, v+d
        # The first layer will have 128 neurons and the second layer will have 64 neurons
        # The activation function will be ReLU
        # The output of the dense network will be passed to a dropout layer with a 50% dropout rate
        # The output of the dropout layer will be passed to a dense layer with 32 neurons and a ReLU activation function

        x1 = tf.keras.layers.concatenate([startTimes, pitches])
        x1 = tf.keras.layers.Reshape((1, memory * 2))(x1)
        x1 = tf.keras.layers.GRU(128, activation="relu")(x1)
        x1 = tf.keras.layers.Flatten()(x1)
        x1 = tf.keras.layers.Dense(64 * params_multiplier, activation="relu")(x1)
        x1 = tf.keras.layers.Dropout(0.5)(x1)
        x1 = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(x1)

        x2 = tf.keras.layers.concatenate([startTimes, velocities])
        x2 = tf.keras.layers.Reshape((1, memory * 2))(x2)
        x2 = tf.keras.layers.GRU(128, activation="relu")(x2)
        x2 = tf.keras.layers.Flatten()(x2)
        x2 = tf.keras.layers.Dense(64 * params_multiplier, activation="relu")(x2)
        x2 = tf.keras.layers.Dropout(0.5)(x2)
        x2 = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(x2)

        x3 = tf.keras.layers.concatenate([startTimes, durations])
        x3 = tf.keras.layers.Reshape((1, memory * 2))(x3)
        x3 = tf.keras.layers.GRU(128, activation="relu")(x3)
        x3 = tf.keras.layers.Flatten()(x3)
        x3 = tf.keras.layers.Dense(64 * params_multiplier, activation="relu")(x3)
        x3 = tf.keras.layers.Dropout(0.5)(x3)
        x3 = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(x3)

        x4 = tf.keras.layers.concatenate([pitches, velocities])
        x4 = tf.keras.layers.Reshape((1, memory * 2))(x4)
        x4 = tf.keras.layers.GRU(128, activation="relu")(x4)
        x4 = tf.keras.layers.Flatten()(x4)
        x4 = tf.keras.layers.Dense(64 * params_multiplier, activation="relu")(x4)
        x4 = tf.keras.layers.Dropout(0.5)(x4)
        x4 = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(x4)

        x5 = tf.keras.layers.concatenate([pitches, durations])
        x5 = tf.keras.layers.Reshape((1, memory * 2))(x5)
        x5 = tf.keras.layers.GRU(128, activation="relu")(x5)
        x5 = tf.keras.layers.Flatten()(x5)
        x5 = tf.keras.layers.Dense(64 * params_multiplier, activation="relu")(x5)
        x5 = tf.keras.layers.Dropout(0.5)(x5)
        x5 = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(x5)

        x6 = tf.keras.layers.concatenate([velocities, durations])
        x6 = tf.keras.layers.Reshape((1, memory * 2))(x6)
        x6 = tf.keras.layers.GRU(128, activation="relu")(x6)
        x6 = tf.keras.layers.Flatten()(x6)
        x6 = tf.keras.layers.Dense(64 * params_multiplier, activation="relu")(x6)
        x6 = tf.keras.layers.Dropout(0.5)(x6)
        x6 = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(x6)

        xSTSum = tf.keras.layers.concatenate([x1, x2, x3])
        xST = tf.keras.layers.Reshape((1, -1))(xSTSum)
        xST = tf.keras.layers.GRU(128, activation="relu")(xST)
        xST = tf.keras.layers.Dropout(0.5)(xST)
        xST = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(xST)
        xST = tf.keras.layers.Flatten()(xST)
        xST = tf.keras.layers.Dense(1, activation="relu", name="outputStartTimes")(xST)

        xPitchSum = tf.keras.layers.concatenate([x1, x4, x5])
        xP = tf.keras.layers.Reshape((1, -1))(xPitchSum)
        xP = tf.keras.layers.GRU(128, activation="relu")(xP)
        xP = tf.keras.layers.Dropout(0.5)(xP)
        xP = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(xP)
        xP = tf.keras.layers.Flatten()(xP)
        xP = tf.keras.layers.Dense(1, activation="relu", name="outputPitches")(xP)

        xVelocitySum = tf.keras.layers.concatenate([x2, x4, x6])
        xV = tf.keras.layers.Reshape((1, -1))(xVelocitySum)
        xV = tf.keras.layers.GRU(128, activation="relu")(xV)
        xV = tf.keras.layers.Dropout(0.5)(xV)
        xV = tf.keras.layers.Dense(32 * params_multiplier, activation="relu")(xV)
        xV = tf.keras.layers.Flatten()(xV)
        xV = tf.keras.layers.Dense(1, activation="relu", name="outputVelocities")(xV)

        xDurationSum = tf.keras.layers.concatenate([x3, x5, x6])
        xD = tf.keras.layers.Reshape((1, -1))(xDurationSum)
        xD = tf.keras.layers.GRU(128, activation="tanh")(xD)
        xD = tf.keras.layers.Dropout(0.5)(xD)
        xD = tf.keras.layers.Dense(64 * params_multiplier, activation="tanh")(xD)
        xD = tf.keras.layers.Flatten()(xD)
        xD = tf.keras.layers.Dense(64 * params_multiplier, activation="tanh")(xD)
        xD = tf.keras.layers.Dense(1, activation="tanh", name="outputDurations")(xD)

        model = tf.keras.models.Model(
            inputs=[startTimes, pitches, velocities, durations],
            outputs=[xST, xP, xV, xD],
        )

        model.summary()
        tf.keras.utils.plot_model(model, show_shapes=True)
        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=1.0e-3),
            loss="mse",
        )

        return model

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
