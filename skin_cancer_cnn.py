import numpy             as np
import pandas            as pd
import tensorflow        as tf
import matplotlib.pyplot as plt
import seaborn           as sns
import os

from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator
from keras._tf_keras.keras.models              import Sequential
from keras._tf_keras.keras.layers              import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from keras._tf_keras.keras.optimizers          import Adam
from keras._tf_keras.keras.callbacks import ModelCheckpoint   



os.system('cls' if os.name == 'nt' else 'clear')
epoch_val = int(input("Enter epoch value: "))





# make sure you're in DermaScan directory when executing this
data_dir = "../../ham10000/HAM10000_images/"
metadata = pd.read_csv("../../ham10000/HAM10000_metadata.csv")
metadata['image_id'] = metadata['image_id'] + '.jpg'
#print(metadata.head())
#print(os.path.exists(data_dir))

# define image parameters
IMG_SIZE = 128  # Resize images to 128x128
BATCH_SIZE = 32

data_gen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    horizontal_flip=True,
    rotation_range=15
)

train_data = data_gen.flow_from_dataframe(
    dataframe=metadata,
    directory=data_dir,
    x_col="image_id",
    y_col="dx",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='training'
)

val_data = data_gen.flow_from_dataframe(
    dataframe=metadata,
    directory=data_dir,
    x_col="image_id",
    y_col="dx",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
    
)











# Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)),
    MaxPooling2D(2, 2),
    BatchNormalization(),
    
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    BatchNormalization(),
    
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    BatchNormalization(),
    
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(len(train_data.class_indices), activation='softmax')
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])



checkpoint = ModelCheckpoint(
    'model_checkpoint.h5', 
    monitor='val_loss', 
    save_best_only=True, 
    verbose=1
)


# Train the model
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=epoch_val
)

# Evaluate model
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epoch_val)
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()


#tf.keras._tf_keras.keras.backend.clear_session()
del train_data
del val_data
del model
import gc
gc.collect()