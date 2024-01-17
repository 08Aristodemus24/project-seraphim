# model architecture will be defined here
import tensorflow as tf
from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import (
    Activation, 
    Dropout, 
    Dense, 
    BatchNormalization,
    Conv2D, 
    MaxPooling2D, 
    Flatten)
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import L2
from tensorflow.keras.losses import CategoricalCrossentropy as cce_loss
from tensorflow.keras.metrics import CategoricalCrossentropy as cce_metric, CategoricalAccuracy
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

import keras_tuner as kt

import numpy as np


def load_baseline_a(n_classes):
    # define architecture
    model = Sequential([
        # build conv and poollayers
        Conv2D(filters=8,
            kernel_size=(5, 5),
            strides=(1, 1),
            kernel_regularizer=L2(0.8)),
        Activation(activation=tf.nn.relu),
        MaxPooling2D(pool_size=(2, 2),
            strides=(2, 2),
            padding='same'),
        Conv2D(filters=16,
            kernel_size=(5, 5),
            strides=(1, 1),
            kernel_regularizer=L2(0.8)),
        Activation(activation=tf.nn.relu),
        MaxPooling2D(pool_size=(2, 2),
            strides=(1, 1),
            padding='same'),

        # flatten pooled layers
        Flatten(),

        # build fully connected layers
        Dense(units=32),
        BatchNormalization(),
        Activation(activation=tf.nn.relu),
        Dense(units=n_classes),

    ], name='architecture-A')

    return model

def compile_model(raw_model, data, learning_rate):
    # define loss, optimizer, and metrics then compile
    opt = Adam(learning_rate=learning_rate, beta_1=0.9, beta_2=0.999)
    loss = cce_loss(from_logits=True)
    metrics = [CategoricalAccuracy(), cce_metric(from_logits=True)]    
    raw_model.compile(optimizer=opt, loss=loss, metrics=metrics)
    raw_model(data)
    raw_model.summary()

    return raw_model

def train_model(compiled_model, training_data, validation_data, epochs, batch_size):
    # define checkpoint and early stopping callback to save
    # best weights at each epoch and to stop if there is no improvement
    # of validation loss for 10 consecutive epochs
    weights_path = f"./saved/models/test_{compiled_model.name}" + "_{epoch:02d}_{val_categorical_accuracy:.2f}.h5"
    checkpoint = ModelCheckpoint(
        weights_path,
        monitor='val_categorical_accuracy',
        verbose=1,
        save_best_only=True,

        # used if model subclass is used
        # save_weights_only=True,
        mode='max')
    stopper = EarlyStopping(monitor='val_categorical_accuracy', patience=10)
    callbacks = [checkpoint, stopper]

    # begin training test model
    history = compiled_model.fit(training_data,
        epochs=epochs,
        batch_size=batch_size, 
        callbacks=callbacks,
        validation_data=validation_data,
        verbose=2,)
    
    return history
    
def main():
    # hyperparameters
    m = 20
    height = 256
    width = 256
    n_channels = 256
    n_unique = 8
    
    
    conv_layers_options = [
        {'n_filters': 8, 'kernel_size': (5, 5), 'kernel_strides': (1, 1)},
        {'n_filters': 16, 'kernel_size': (5, 5), 'kernel_strides': (1, 1)},
        
    ]
    pool_layers_options = [
        {'pool_size': (2, 2), 'pool_strides': (2, 2)},
        {'pool_size': (2, 2), 'pool_strides': (1, 1)},
    ]
    dense_layers_dims = [32, 16, n_unique]
    padding = 'same'

    lambda_ = 0.8
    drop_prob = 0.4
    normalize = False
    learning_rate = 1e-3
    epochs = 30
    batch_size = 512
    

    # create dummy (m, height, width, n_channels) dataset
    X = (np.random.randint(0, 256, size=(m, height, width, n_channels)) * 1.0) / 255

    # create an array of labels of 8 unique values representing our
    # different categories/classes of image of m length
    Y = np.random.randint(0, n_unique, size=(m,))

    # one hot encode our dummy labels 
    Y = tf.one_hot(Y, depth=n_unique)

    # instantiate custom model
    raw_model = load_baseline_a(
        conv_layers_options=conv_layers_options, 
        pool_layers_options=pool_layers_options,
        dense_layers_dims=dense_layers_dims,
        padding=padding,
        lambda_=lambda_,
        normalize=False
    )

    compiled_model = compile_model(
        raw_model=raw_model,
        X=X,
        learning_rate=learning_rate
    )

    history = train_model(
        compiled_model,
        X, 
        Y,
        epochs=epochs,
        batch_size=batch_size
    )

class MOClassifierHyperModel(kt.HyperModel):
    def __init__(self, name=None, tunable=True):
        super().__init__(name, tunable)

    def build(self, hp):
         # define architecture
        model = Sequential(name='architecture-A')

        # build conv and poollayers
        n_conv_layers = len(conv_layers_options)
        for cl in range(n_conv_layers):
            model.add(Conv2D(
                filters=conv_layers_options[cl]['n_filters'],
                kernel_size=conv_layers_options[cl]['kernel_size'],
                strides=conv_layers_options[cl]['kernel_strides'],
                kernel_regularizer=L2(lambda_)
            ))
            model.add(Activation(activation=tf.nn.relu))
            model.add(MaxPooling2D(
                pool_size=pool_layers_options[cl]['pool_size'],
                strides=pool_layers_options[cl]['pool_strides'],
                padding=padding
            ))

        # flatten pooled layers
        model.add(Flatten())

        # build fully connected layers, excluding final layer
        n_dense_layers = len(dense_layers_dims) - 1
        for dl in range(n_dense_layers):
            model.add(Dense(
                units=dense_layers_dims[dl],
                kernel_regularizer=L2(lambda_)
            ))

            # pass dense through normalization layer if true
            if normalize == True:
                model.add(BatchNormalization())

            # pass dense or batch normalized layer
            model.add(Activation(activation=tf.nn.relu))

        # add final dense layer with final dimension of
        # the dense_layers_dims value
        model.add(Dense(
            units=dense_layers_dims[-1],
            kernel_regularizer=L2(lambda_)
        ))

        return model


    
    