import numpy as np
from value import Value
from loss import CrossEntropyLoss
from utils import load_mnist, download_mnist

class MLP:
    def __init__(self, nin, nouts):
        self.layers = []
        sz = [nin] + nouts
        for i in range(len(nouts)):
            self.layers.append([Value(np.random.randn()) for _ in range(sz[i] * sz[i+1])])

    def __call__(self, x):
        for layer in self.layers:
            x = [sum((x[i] * layer[i * len(layer) // len(x) + j] for i in range(len(x))), start=Value(0)).relu() for j in range(len(layer) // len(x))]
        return x

download_mnist()

(x_train, y_train), (x_test, y_test) = load_mnist()

model = MLP(28*28, [128, 64, 10])
loss_fn = CrossEntropyLoss()

epochs = 5
learning_rate = 0.001
for epoch in range(epochs):
    epoch_loss = 0
    for i in range(len(x_train)):
        x = [Value(x_train[i][j]) for j in range(len(x_train[i]))]
        y = [Value(y_train[i][j]) for j in range(len(y_train[i]))]
        logits = model(x)
        loss = loss_fn(logits, y)
        epoch_loss += loss.data

        loss.backward()
        for param in model.layers:
            for p in param:
                p.data -= learning_rate * p.grad

        for param in model.layers:
            for p in param:
                p.grad = 0

    print(f'第 {epoch+1} 輪, 損失: {epoch_loss/len(x_train)}')
