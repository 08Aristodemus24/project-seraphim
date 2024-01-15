import tensorflow as tf
from tensorflow.keras.regularizers import L2
from tensorflow.keras.layers import Dense, Dropout, LSTM, Bidirectional, Activation, Embedding
from tensorflow.keras import Model, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy as cce_loss
from tensorflow.keras.metrics import CategoricalAccuracy, CategoricalCrossentropy as cce_metric
from tensorflow.keras.initializers import GlorotNormal, GlorotUniform
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping


def init_embedding_layer(vocab_len, emb_matrix):
    emb_dim = emb_matrix.shape[1]
    embedding_layer = Embedding(vocab_len, emb_dim, trainable=False)
    embedding_layer.build((None,))
    embedding_layer.set_weights([emb_matrix])

    return embedding_layer


def load_lstm_model(input_shape, vocab_len, emb_matrix):
    """
    Define architecture of LSTM model then return for later training

    Takes in also the embedding layer with weights/coefficients set
    to the pre-trained GloVe embeddings
    """
    print(f'input shape: {input_shape}')

    seqs_padded = Input(shape=(input_shape, ), dtype='int64')
    embeddings = init_embedding_layer(vocab_len, emb_matrix)(seqs_padded)
    A1 = Bidirectional(LSTM(units=16, return_sequences=True))(embeddings)
    D1 = Dropout(0.5)(A1)
    A2 = Bidirectional(LSTM(units=16, return_sequences=False))(D1)
    D2 = Dropout(0.5)(A2)
    Z3 = Dense(units=4)(D2)
    A3 = Activation('softmax')(Z3)

    model = Model(inputs=seqs_padded, outputs=A3, name='hate-speech-lstm')

    return model

def compile_model(raw_model, X, learning_rate):
    raw_model.compile(
        loss=cce_loss(),
        optimizer=Adam(learning_rate=learning_rate),
        metrics=[cce_metric(), CategoricalAccuracy()]
    )
    raw_model(X)
    raw_model.summary()

    return raw_model

def train_model(compiled_model, X, Y, epochs, batch_size):
    # define checkpoint and early stopping callback to save
    # best weights at each epoch and to stop if there is no improvement
    # of validation loss for 10 consecutive epochs
    weights_path = f"../saved/models/test_{compiled_model.name}" + "_{epoch:02d}_{val_categorical_accuracy:.2f}.h5"
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
    history = compiled_model.fit(X, Y,
        epochs=epochs,
        batch_size=batch_size, 
        callbacks=callbacks,
        validation_split=0.3,
        verbose=2,)
    
    return history