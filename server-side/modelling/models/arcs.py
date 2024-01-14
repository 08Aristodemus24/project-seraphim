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

import numpy as np


def load_model_a(conv_layers_options, pool_layers_options, padding, dense_layers_dims, lambda_, drop_prob, learning_rate, normalize=False):
    
    # define architecture
    model = Sequential()

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

    # build fully connected layers
    n_dense_layers = len(dense_layers_dims)
    for dl in range(n_dense_layers) - 1:
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
    
    

if __name__ == "__main__":
    # hyperparameters
    m = 20000
    height = 256
    width = 256
    n_channels = 256
    n_unique = 8
    
    
    conv_layers_options = [
        {'n_filters': 32, 'kernel_size': (5, 5), 'kernel_strides': (1, 1)},
        {'n_filters': 64, 'kernel_size': (5, 5), 'kernel_strides': (1, 1)},
        
    ]
    pool_layers_options = [
        {'pool_size': (2, 2), 'pool_strides': (2, 2)},
        {'pool_size': (2, 2), 'pool_strides': (1, 1)},
    ]
    dense_layers_dims = [64, 32, n_unique]
    padding = 'same'

    lambda_ = 0.8
    drop_prob = 0.4
    learning_rate = 1e-3
    epochs = 100
    batch_size = 512
    normalize = False

    # create dummy (m, height, width, n_channels) dataset
    X = np.random.uniform(0, 256, size=(m, height, width, n_channels))

    # create an array of labels of 8 unique values representing our
    # different categories/classes of image of m length
    Y = np.random.randint(0, n_unique, size=(m,))

    # one hot encode our dummy labels 
    Y = tf.one_hot(Y, depth=Y.shape[0])


    # instantiate custom model
    # model = GenPhiloTextB(emb_dim=emb_dim, n_a=n_a, n_unique=n_unique, T_x=T_x, dense_layers_dims=dense_layers_dims, lambda_=lambda_, drop_prob=drop_prob, normalize=normalize)

    # define loss, optimizer, and metrics then compile
    opt = Adam(learning_rate=learning_rate, beta_1=0.9, beta_2=0.999)
    loss = cce_loss(from_logits=True)
    metrics = [CategoricalAccuracy(), cce_metric(from_logits=True)]    
    model.compile(optimizer=opt, loss=loss, metrics=metrics)
    model(X)
    # model([X, h_0, c_0])
    model.summary()

    # define checkpoint and early stopping callback to save
    # best weights at each epoch and to stop if there is no improvement
    # of validation loss for 10 consecutive epochs
    weights_path = f"../saved/weights/test_{model.name}" + "_{epoch:02d}_{val_loss:.4f}.h5"
    checkpoint = ModelCheckpoint(weights_path, monitor='val_loss', verbose=1, save_best_only=True, save_weights_only=True, mode='min')
    stopper = EarlyStopping(monitor='val_loss', patience=10)
    callbacks = [checkpoint, stopper]

    # begin training test model
    history = model.fit(X, Y_true, 
        epochs=epochs,
        batch_size=batch_size, 
        callbacks=callbacks,
        validation_split=0.3,
        verbose=2,)
    