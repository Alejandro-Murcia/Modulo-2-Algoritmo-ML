import numpy as np
import matplotlib.pyplot as plt

# ---- Elección del Modelo ----
# Elegí la regresión logística como modelo porque estamos tratando un problema de clasificación binaria:
# clasificar pacientes como diabéticos o no diabéticos. La regresión logística es especialmente adecuada para 
# este tipo de tareas ya que produce una probabilidad que un dato pertenezca a una categoría, y es capaz 
# de establecer un límite de decisión entre las categorías.

# ---- Estructura del Código A----
# El código se divide en funciones principales: 
# 1. sigmoid_function: Función sigmoide que se utiliza como hipótesis de la regresión logística.
# 2. log_regression: Donde se lleva a cabo el entrenamiento usando el gradiente descendente.
# Además, se carga un conjunto de datos, se entrena el modelo y finalmente se realizan y evalúan las predicciones.

# ---- Procedimiento ----
# El conjunto de datos se carga y se normalizan sus características. El modelo se entrena mediante el algoritmo 
# de gradiente descendente. Se utiliza la función de costo logarítmico (Negative Log Loss) para evaluar el 
# rendimiento del modelo durante el entrenamiento. Finalmente, se realiza una predicción y se evalúa la precisión.

def sigmoid_function(X):
    return 1 / (1 + np.exp(-X))

def log_regression(X, y, theta, alpha, lambda_, epochs):
    y_ = np.reshape(y, (len(y), 1))
    N = len(X)
    avg_loss_list = []
    loss_last_epoch = 9999999

    for epoch in range(epochs):
        hyp = sigmoid_function(X.dot(theta))
        grad = X.T.dot(hyp - y_) / N + lambda_ * theta / N
        theta = theta - (alpha * grad)
        
        avg_loss = (-np.sum(y_ * np.log(hyp) + (1-y_) * np.log(1-hyp)) / N 
                   + lambda_ * np.sum(np.square(theta)) / (2*N))
        
        if epoch % 10 == 0:
            print('Epoch: {} | Avg. Loss: {}'.format(epoch, avg_loss))

        avg_loss_list.append(avg_loss)
        loss_step = abs(loss_last_epoch - avg_loss)
        loss_last_epoch = avg_loss

        if loss_step < 0.001:
            print('\nStopping training on epoch {}/{}, as the change in loss is less than 0.001 [{}]'.format(epoch, epochs, loss_step))
            break

    plt.plot(avg_loss_list)
    plt.title('Cost function')
    plt.xlabel('Epochs')
    plt.ylabel('Cost')
    plt.show()

    return theta

# Cargando el dataset de diabetes
data = np.loadtxt('diabetes.csv', delimiter=',', skiprows=1)
X = data[:, :-1]
y = data[:, -1]
X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)
X = (X - X_mean) / X_std
X_with_bias = np.c_[np.ones((len(X), 1)), X]
theta = np.random.randn(X_with_bias[0].size, 1)

# Entrenando el modelo
epochs = 10000
alpha = 0.1
lambda_ = 0.1
best_params = log_regression(X_with_bias, y, theta, alpha, lambda_, epochs)

# Haciendo predicciones
predictions = sigmoid_function(X_with_bias.dot(best_params))
predicted_classes = (predictions >= 0.5).astype(int)
accuracy = np.mean(predicted_classes == y.reshape(-1, 1))

print(f'Accuracy: {accuracy * 100:.2f}%')
