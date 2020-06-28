import tensorflow as tf
import tensorflow_datasets as tfds

dataset, info = tfds.load(name="mnist", with_info=True, as_supervised=True)
mnist_train, mnist_test = dataset['train'], dataset['test']

BUFFER_SIZE = 10
BATCH_SIZE = 64
NUM_EPOCHS = 5

def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255

    return image, label

train_data = mnist_train.map(scale).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
test_data = mnist_test.map(scale).batch(BATCH_SIZE)

STEPS_PER_EPOCH = 5

train_data = train_data.take(STEPS_PER_EPOCH)
test_data = test_data.take(STEPS_PER_EPOCH)

image_batch, label_batch = next(iter(train_data))

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation="relu",
                           kernel_regularizer=tf.keras.regularizers.l2(0.02),
                           input_shape=(28, 28, 1)),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(10, activation="softmax")
])

model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

model.fit(train_data, epochs=NUM_EPOCHS)
loss, acc = model.evaluate(test_data)

print("Loss {}, Accuary {}".format(loss, acc))