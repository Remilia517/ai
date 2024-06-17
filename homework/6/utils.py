import requests
import gzip
import numpy as np
import os

def download_mnist():
    base_url = "http://yann.lecun.com/exdb/mnist/"
    files = ["train-images-idx3-ubyte.gz", "train-labels-idx1-ubyte.gz",
             "t10k-images-idx3-ubyte.gz", "t10k-labels-idx1-ubyte.gz"]
    for file in files:
        response = requests.get(base_url + file, stream=True)
        with open(file, 'wb') as f:
            f.write(response.content)

def load_mnist(path=""):
    def load_images(filename):
        with gzip.open(filename, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=16)
            data = data.reshape(-1, 28*28)
        return data

    def load_labels(filename):
        with gzip.open(filename, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=8)
        return data

    x_train = load_images(path + 'train-images-idx3-ubyte.gz') / 255.0
    y_train = load_labels(path + 'train-labels-idx1-ubyte.gz')
    x_test = load_images(path + 't10k-images-idx3-ubyte.gz') / 255.0
    y_test = load_labels(path + 't10k-labels-idx1-ubyte.gz')
    
    y_train_one_hot = np.eye(10)[y_train]
    y_test_one_hot = np.eye(10)[y_test]

    return (x_train, y_train_one_hot), (x_test, y_test_one_hot)
