# model architecture will be defined here
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import (
    LSTM, 
    Activation, 
    Dropout, 
    Dense, 
    RepeatVector, 
    Reshape, 
    Embedding,
    Input,
    BatchNormalization,
    Add)
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import L2
from tensorflow.keras.losses import CategoricalCrossentropy as cce_loss
from tensorflow.keras.metrics import CategoricalCrossentropy as cce_metric, CategoricalAccuracy
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

import numpy as np

if __name__ == "__main__":
    # hyperparameters
    m = 20000
    T_x = 100
    n_unique = 57
    n_a = 64
    emb_dim = 32
    dense_layers_dims = [n_unique]
    lambda_ = 0.8
    drop_prob = 0.4
    learning_rate = 1e-3
    epochs = 100
    batch_size = 512
    normalize = False

    # note X becomes (m, T_x, n_features) when fed to embedding layer
    X = np.random.randint(0, n_unique, size=(m, T_x))

    # we have to match the output of the prediction of our 
    # model which is a list of (100, 26) values. So instead of a 3D matrixc
    # we create a list fo 2D matrices of shape (100, 26)
    Y = [np.random.rand(m, n_unique) for _ in range(T_x)]

    # one hot encode our dummy (T_y, m, n_unique) probabilities
    Y = [tf.one_hot(tf.argmax(y, axis=1), depth=n_unique) for y in Y]
    
    # test for computing loss with (m, T_y, n_unique) predictions
    Y_true = tf.reshape(Y, shape=(m, T_x, n_unique))
    dummy_logits = np.random.randn(m, T_x, n_unique)
    loss = cce_loss(from_logits=True)(dummy_logits, Y_true)
    print(f"computed test loss: {loss}")

    # initialize hidden and cell states to shape (m, n_units)
    h_0 = np.zeros(shape=(m, n_a))
    c_0 = np.zeros(shape=(m, n_a))

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
    
    # history = model.fit([X, h_0, c_0], Y_true, 
    #     epochs=epochs,
    #     batch_size=batch_size, 
    #     callbacks=callbacks,
    #     validation_split=0.3,
    #     verbose=2,)
    
    # save model
    # model.save_weights('../saved/weights/test_model_gen_philo_text.h5', save_format='h5')
    # model.save('../saved/models/test_model_b.h5', save_format='h5')
    