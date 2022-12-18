from keras.preprocessing.image import ImageDataGenerator
from keras.models import save_model, Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dropout, Dense

# Image data generator
training_generator = ImageDataGenerator(
    rescale=1/255,
    rotation_range=40,
    width_shift_range=0.3,
    height_shift_range=0.3,
    zoom_range=0.3,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest')
validation_generator = ImageDataGenerator(rescale=1/255)


# Image Directory
training_directory = "training_dataset"
testing_directory = "testing_dataset"
validation_directory = "validation_dataset"

# Generate Preprocessed Augmented Data
training_augmented = training_generator.flow_from_directory(
    training_directory,
    target_size=(180, 180)
)
validation_augmented = validation_generator.flow_from_directory(
    validation_directory,
    target_size=(180, 180)
)

sequence = [
    Conv2D(64, (3, 3), activation='relu', input_shape=(180, 180, 3)),
    MaxPool2D(2, 2)
]
sequence += [
    Conv2D(64, (3, 3), activation='relu'),
    MaxPool2D(2, 2),
] * 3
sequence += [
    Flatten(),
    Dropout(0.5),
    Dense(512, activation='relu'),
    Dense(2, activation='sigmoid')
]
model = Sequential(sequence)

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

fit_history = model.fit(
    training_augmented,
    epochs=5,
    verbose=True
)

model.save('model.h5')
