# Neurona Lineal

**By: Dexne**

## Neurona Lineal

Una neurona lineal es un tipo de neurona artificial en la que la salida es una función lineal de la suma ponderada de las entradas. En el contexto del aprendizaje automático, las neuronas lineales se utilizan a menudo como capas de entrada o capas de entrada o capas de salida en redes neuronales. También se pueden usar como capas ocultas, aunque en general, las capas no lineales son más efectivas para capturar relaciones complejas entre las entradas y salidas.
Es importante tener en cuenta que la neurona lineal es una de las funciones de activación más simples, y si salida no está limitada a un rango específico, lo que puede dar lugar a problemas de saturación si los procesos son demasiado grandes.

## Instalación

Para ejecutar este código, se requieren las siguientes bibliotecas de Python:

- Numpy
- Pandas
- Matplotlib

Puedes instalarlas a través del siguiente comando:

```
pip install numpy pandas matplotlib
```

## Detalles de Implementación

**LinearNeuron**

La clase LinearNeuron representa una neurona lineal con los siguientes métodos:

- **predict(X):** Predice la salida para un conjunto de datos de entrada X.

- **batcher(X, Y, batch_size):** Genera lotes de datos para el entrenamiento por lotes.
  
- **MSE(X, Y):** Calcula el Error Cuadrático Medio (MSE) entre las predicciones y los datos reales.
  
- **fit(X, Y, solver, epochs, batch_size):** Entrena la neurona utilizando diferentes métodos de optimización, como Gradiente Descendente Estocástico (SGD), Gradiente Descendente por Lotes (BGD), Mini Batcher Gradiente Descendente (mBGD) y Pseudo-inverso (PINV).


## Funcion objetivo

f(x) = −x+7∗N(0,1)
η=0.005
Epoch=500 

#### Resultados

Stochastic Gradient Descent

![SGD Error](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T03/MSE_SGD.png)
![SGD](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T03/SGD.png)

Batch Gradient Descent

![Batch Gradient Descent Error](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T03/MSE_BGD.png)
![Batch Gradient Descent](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T03/BGD.png)

mini Batch Gradient Descent

![mini Batch Gradient Descent Error](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T03/MSE_mBGD.png)
![mini Batch Gradient Descent](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T03/mBGD.png)

Pseudo Inverse

![Pseudo Inverse](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T03/PINV.png)

## Conclusión

Podemos denotar, en las diferentes gráficas, como cada formato reduce su error cuadrático medio respecto a las iteraciones, con estos datos podemos concluir que no solo importa el algoritmo, sino también los parámetros de ajuste y las épocas que iteramos, siendo una correlación dependiente, con ellos veremos nuestros resultados mejorar u oscilar de ser mal ajustados dichos parámetros. Como podemos observar, la relación de tasa de aprendizaje y el algoritmo, es importante para objetivar la cantidad de épocas necesarias para una solución aceptable, ya que, como vimos en las gráficas previas, podemos tener cientos de iteraciones sin mejorar en nuestro modelo.
