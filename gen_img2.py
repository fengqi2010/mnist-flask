import tensorflow as tf
import os
import matplotlib.pyplot as plt


def mkdir(p):
    if not os.path.exists(p):
        os.makedirs(p)


(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

mkdir('img2')
for i in range(1000):
    label_path = f'img2/{i % 10}'
    mkdir(label_path)
    if len(os.listdir(label_path)) >= 10:
        continue
    image = train_images[i]
    label = train_labels[i]
    image_path = os.path.join(label_path, f'mnist_{i}.png')

    # 使用matplotlib保存图像
    plt.imsave(image_path, image, cmap='gray')
    print(f'Saved image {i} with label {label} to {image_path}')
