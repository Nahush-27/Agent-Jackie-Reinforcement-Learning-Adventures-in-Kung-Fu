from keras.models import Model, load_model, Sequential
from keras.layers import Input, Dense, LSTM, Reshape, Dropout, Conv2D, Flatten
from keras.optimizers import Adam
import tensorflow as tf


def CartPole(input_shape, action_space):
    X_input = Input(input_shape)
    X = X_input

    # 'Dense' is the basic form of a neural network layer
    # Input Layer of state size(4) and Hidden Layer with 512 nodes
    X = Dense(512, input_shape=input_shape, activation="relu")(X)
    X = Dropout(0.5)(X)

    # Hidden layer with 256 nodes
    X = Dense(256, activation="relu")(X)
    X = Dropout(0.5)(X)
    
    # Hidden layer with 64 nodes
    X = Dense(64, activation="relu")(X)
    X = Dropout(0.5)(X)
    
    # Output Layer with # of actions: 2 nodes (left, right)
    X = Dense(action_space, activation="linear")(X)

    model = Model(inputs = X_input, outputs = X, name='CartPole_model')
    model.compile(loss='mse', optimizer=Adam())
    
    return model

def KungFu(self):
    model = Sequential()
    model.add(Input((84,84,4)))
    model.add(Conv2D(filters = 32,kernel_size = (8,8),strides = 4,data_format="channels_last", activation = 'relu',kernel_initializer = tf.keras.initializers.VarianceScaling(scale=2)))
    model.add(Conv2D(filters = 64,kernel_size = (4,4),strides = 2,data_format="channels_last", activation = 'relu',kernel_initializer = tf.keras.initializers.VarianceScaling(scale=2)))
    model.add(Conv2D(filters = 64,kernel_size = (3,3),strides = 1,data_format="channels_last", activation = 'relu',kernel_initializer = tf.keras.initializers.VarianceScaling(scale=2)))
    model.add(Flatten())
    model.add(Dense(512,activation = 'relu', kernel_initializer = tf.keras.initializers.VarianceScaling(scale=2)))
    model.add(Dense(len(self.possible_actions), activation = 'linear'))
    optimizer = Adam(self.learn_rate)
    model.compile(optimizer, loss=tf.keras.losses.Huber())