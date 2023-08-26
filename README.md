# Módulo 2 - Algoritmo Sin Uso de Frameworks
# Regresión Logística para la Predicción de Diabetes

## Descripción del Dataset

El dataset utilizado para este proyecto proviene de Kaggle y contiene diferentes parámetros relacionados con la salud de pacientes, incluyendo su edad, niveles de glucosa, entre otros. El objetivo es usar estos parámetros para predecir si un paciente tiene diabetes o no (etiqueta binaria: 1 o 0). Para simplificar el modelo, sólo hemos utilizado dos características: **Niveles de Glucosa** y **Edad**.

## Modelo de Regresión Logística

### Justificación del Modelo

Se optó por un modelo de regresión logística debido a su eficacia y simplicidad en problemas de clasificación binaria. La regresión logística utiliza una función sigmoide para mapear las predicciones a un rango de [0,1].

### Fórmulas Claves

La **Función Sigmoide** es definida como:

$\[\sigma(z) = \frac{1}{1 + e^{-z}}\]$

La **Función de Costo Logarítmico** a minimizar es:

$\[J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} [ y^{(i)} \log(h(x^{(i)})) + (1 - y^{(i)}) \log(1 - h(x^{(i)})) ]
\]$

### Parámetros del Modelo

- **Tasa de Aprendizaje (lr)**: 0.01
- **Épocas**: 10,000

## Implementación y Pruebas

La implementación del modelo se llevó a cabo en Python, sin el uso de bibliotecas especializadas en aprendizaje automático. Se implementaron funciones para calcular la media y la desviación estándar de las características, para posteriormente realizar su normalización. Esto resultó en una mejor convergencia durante el entrenamiento.

### Resultados de las Pruebas

1. Paciente con 130 de glucosa y 60 años de edad: Paciente con Diabetes
2. Paciente con 80 de glucosa y 21 años de edad: Paciente sin Diabetes

Estas pruebas nos dieron resultados consistentes con la lógica médica general respecto a la diabetes.

## Conclusiones y Pasos Futuros

El modelo mostró una precisión moderada pero puede mejorarse a través de una selección más extensa de características, ajuste de hiperparámetros, o incluso utilizando modelos más complejos. Además, podrían llevarse a cabo más pruebas utilizando un conjunto de datos de validación.

