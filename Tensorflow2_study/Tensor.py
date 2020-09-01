import tensorflow as tf
import numpy as np

Ndarray = np.ones([3, 3])

# 텐서플로우 연산은 자동적으로 Numpy 배열을 텐서로 변환
Tensor = tf.multiply(Ndarray, 42)
print(Tensor)

# Numpy 연산은 자동적으로 텐서를 Numpy 배열로 변환
print(np.add(Tensor, 1))

# .numpy() 메서드는 텐서를 넘파이 배열로 변환
print(Tensor.numpy())

X = tf.random.uniform([3, 3])

# GPU 사용여부 확인
# tf.test.is_gpu_available() -> tf.config.list_physical_devices("GPU") in TF Core v2.3.0
print("TF GPU Available:", tf.config.list_physical_devices("GPU"))
# print("TF GPU Available:", tf.test.is_gpu_available())

# Tensor가 GPU #0에 있는지 여부
print("Tensor in GPU #0:", X.device.endswith('GPU:0'))