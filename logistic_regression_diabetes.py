import csv
import math

# ---- Comentarios de Elección del Modelo ----
# Elegí un modelo de regresión logística porque es una técnica bien comprendida y efectiva para 
# la clasificación binaria. En este caso, queremos clasificar a los pacientes como diabéticos o no diabéticos
# en función de su edad y niveles de glucosa en sangre.

# ---- Comentarios de Estructura ----
# La estructura del código sigue un patrón típico de aprendizaje automático: 
# - Carga de datos
# - Preprocesamiento
# - Entrenamiento del modelo
# - Realización de predicciones

# ---- Comentarios de Procedimiento ----
# Para mejorar el modelo, se implementa la normalización de las características, lo que 
# generalmente hace que el modelo sea más efectivo y facilita la convergencia durante el entrenamiento.

# Función para calcular la media y la desviación estándar
def mean_std(data):
    mean_x1 = sum(x1 for x1, _, _ in data) / len(data)
    mean_x2 = sum(x2 for _, x2, _ in data) / len(data)
    std_x1 = math.sqrt(sum((x1 - mean_x1)**2 for x1, _, _ in data) / len(data))
    std_x2 = math.sqrt(sum((x2 - mean_x2)**2 for _, x2, _ in data) / len(data))
    return mean_x1, std_x1, mean_x2, std_x2

# Función sigmoide: esencial para el modelo de regresión logística
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# Función para entrenar la regresión logística
def train_logistic_regression(data, epochs, lr):
    w0, w1, w2 = 0.0, 0.0, 0.0
    mean_x1, std_x1, mean_x2, std_x2 = mean_std(data)
    data = [( (x1-mean_x1)/std_x1, (x2-mean_x2)/std_x2, y ) for x1, x2, y in data]

    for epoch in range(epochs):
        for x1, x2, y in data:
            z = w0 + w1 * x1 + w2 * x2
            pred = sigmoid(z)
            error = pred - y
            w0 = w0 - lr * error
            w1 = w1 - lr * error * x1
            w2 = w2 - lr * error * x2
            
    return w0, w1, w2, mean_x1, std_x1, mean_x2, std_x2

# Función para hacer predicciones
def predict(x1, x2, w0, w1, w2, mean_x1, std_x1, mean_x2, std_x2):
    x1 = (x1 - mean_x1) / std_x1
    x2 = (x2 - mean_x2) / std_x2
    z = w0 + w1 * x1 + w2 * x2
    pred = sigmoid(z)
    return "Paciente con Diabetes" if pred >= 0.5 else "Paciente sin Diabetes"

# Cargar datos desde un archivo CSV
data = []
with open("diabetes.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Saltar la fila de encabezado
    for row in reader:
        if row:  
            glucose, age, outcome = float(row[1]), float(row[7]), int(row[8])
            data.append((glucose, age, outcome))

# Entrenar el modelo de regresión logística
w0, w1, w2, mean_x1, std_x1, mean_x2, std_x2 = train_logistic_regression(data, epochs=10000, lr=0.01)

# Realizar predicciones y mostrar los resultados
print(f"Paciente con 130 de glucosa y 60 años de edad: {predict(130.0, 60.0, w0, w1, w2, mean_x1, std_x1, mean_x2, std_x2)}")
print(f"Paciente con 80 de glucosa y 21 años de edad: {predict(80.0, 21.0, w0, w1, w2, mean_x1, std_x1, mean_x2, std_x2)}")
