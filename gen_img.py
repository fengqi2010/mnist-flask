import tensorflow as tf
import os
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
if not os.path.exists('img'):
    os.makedirs('img')
for i in range(10):
    image = train_images[i]
    label = train_labels[i]
    image_path = os.path.join('img', f'mnist_{i}.png')

    # 使用matplotlib保存图像
    plt.imsave(image_path, image, cmap='gray')
    print(f'Saved image {i} with label {label} to {image_path}')
