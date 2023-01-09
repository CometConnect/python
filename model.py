from numpy import array
from keras.models import Sequential
from keras.layers import Dense, Dropout

from preprocess import create


def main():
    bow, intents = create()
    np_bow = array(list(map(lambda x: array(x), bow)))
    np_intents = array(intents)

    sequence = [
        Dense(128, activation='relu', input_shape=(len(bow[0]),)),
        Dropout(0.5),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(len(intents[0]), activation='softmax')
    ]
    model = Sequential(sequence)

    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    history = model.fit(np_bow, np_intents, epochs=200, batch_size=5, verbose=True)
    model.save('model.h5', history)
