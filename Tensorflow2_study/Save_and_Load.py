from __future__ import absolute_import, division, print_function, unicode_literals, unicode_literals

import os

import tensorflow as tf
from tensorflow import keras

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

train_labels = train_labels[:1000]
test_labels = test_labels[:1000]

train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

def create_model():
  model = tf.keras.models.Sequential([
    keras.layers.Dense(512, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10, activation='softmax')
  ])

  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model

model = create_model()
model.summary()


#체크포인트 콜백 사용하기
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

model = create_model()

model.fit(train_images, train_labels,  epochs = 10,
          validation_data = (test_images,test_labels),
          callbacks = [cp_callback])  # 훈련 단계에 콜백을 전달합니다

model = create_model()

loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
print("훈련되지 않은 모델의 정확도: {:5.2f}%".format(100*acc))

model.load_weights(checkpoint_path)
loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))


#체크포인트 콜백 매개변수
checkpoint_path = "training_2/cp-{epoch:04d}.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path, verbose=1, save_weights_only=True, period=5)

model = create_model()
model.save_weights(checkpoint_path.format(epoch=0))
model.fit(train_images, train_labels,
          epochs = 50, callbacks = [cp_callback],
          validation_data = (test_images,test_labels), verbose=0)

latest = tf.train.latest_checkpoint(checkpoint_dir)

model = create_model()
model.load_weights(latest)
loss, acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))


#수동으로 가중치 저장하기
model.save_weights('./checkpoints/my_checkpoint')

model = create_model()
model.load_weights('./checkpoints/my_checkpoint')

loss,acc = model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))


#HDF5 파일로 저장하기
model = create_model()

model.fit(train_images, train_labels, epochs=5)

model.save('my_model.h5')

new_model = keras.models.load_model('my_model.h5')
new_model.summary()

loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))


# saved_model을 사용하기
# Tensorflow Core v2.2.0 버전 기준 load_from_saved_model의 지원이 중단됨
# Load_from_saved_model based on Sensorflow Core v2.2.0 version is discontinued
# model = create_model()
#
# model.fit(train_images, train_labels, epochs=5)
#
# import time
# saved_model_path = "./saved_models/{}".format(int(time.time()))
#
# tf.keras.experimental.export_saved_model(model, saved_model_path)
#
# new_model = tf.keras.experimental.load_from_saved_model(saved_model_path)
# new_model.summary()
#
# model.predict(test_images).shape
#
# new_model.compile(optimizer=model.optimizer, # 복원된 옵티마이저를 사용합니다.
#                   loss='sparse_categorical_crossentropy',
#                   metrics=['accuracy'])
#
# loss, acc = new_model.evaluate(test_images,  test_labels, verbose=2)
# print("복원된 모델의 정확도: {:5.2f}%".format(100*acc))