# Perceptrón
**BY: Dexne**

## Modelo de McCulloch-Pitts


El modelo de McCulloch-Pitts (También conocido como modelo de neurona artificial) es un modelo matemático que fue propuesto por Warren McCulloch y Walter Pitts en 1943. Es uno de los primeros modelos de la teoría de la inteligencia artificial y sigue siendo una parte importante de la investigación.
En el modelo de McCulloch-Pitts, una neurona se representa como un elemento básico que puede recibir señales de entrada y producir una señal de salida. Cada señal de entrada se asocia con un peso, que indica la importancia de la señal. La salida de la neurona se determina por una función de activación que evalúa la suma ponderada de las señales de entrada. Este modelo ha sido ampliamente utilizado como una base para el desarrollo de algoritmos de aprendizaje automático y para la investigación en la inteligencia artificial y la neurociencia computacional. Aunque es un modelo simplificado de una neurona real, ha sido muy útil para entender el funcionamiento de los sistemas de procesamiento de información en el cerebro.

## El algoritmo del Perceptrón


El algoritmo del Perceptrón es un algoritmo de aprendizaje automático supervisado que se utiliza para clasificar datos en dos categorías. Se basa en el modelo de McCulloch-Pitts y es uno de los primeros algoritmos de aprendizaje automático desarrollados.
El algoritmo del Perceptrón funciona asignando pesos a las características de los datos de entrada y aplicando una función de activación para producir una salida. La función de activación es una función lineal que toma en cuenta la suma ponderada de las señales de entrada. Si la salida es mayor que cero, la entrada se clasifica en una categoría, y si la salida es menor o igual a cero, se clasifica en otra categoría. El algoritmo se ajusta iterativamente a los datos de entrenamiento, ajustando los pesos para minimizar el número de errores de clasificación. Este proceso de ajuste de pesos se llama “entrenamiento” y se realiza utilizando una técnica de optimización, como el gradiente descendente.
Aunque el algoritmo del Perceptrón es muy simple, ha sido ampliamente utilizado y ha demostrado ser efectivo en una amplia variedad de problemas de clasificación. Sin embargo, también tiene algunas limitaciones, como su capacidad limitada para manejar problemas de clasificación no lineales.
Por esta razón, se han desarrollado algoritmos más avanzados como los árboles de decisión, las redes neuronales y los algoritmos de aprendizaje profundo.

### Parte 1 - Compuertas lógicas

Figura 1 - Compuerta AND
![Figura 1](T02\Logic_Gates_AND.png)

Fugura 2 - Compuerta OR
![Figura 2](T02\Logic_Gates_OR.png)

Fugura 3 - Compuerta XOR
![Figura 3](T02\Logic_gates_XOR.png)

### Parte 2 - Índice de masa corporal

Figura 4 - Índice de masa corporal - Datos de entrenamiento
![Figura 4](T02\BMI_1.png)

Figura 5 - Índice de masa corporal - Neurona entrenada
![Figura 5](T02\BMI_2.png)

**¿Por qué la compuerta XOR no puede ser aprendida por este modelo?**


El modelo del perceptrón es una red neuronal de una sola capa que puede aprender a clasificar datos linealmente seriales (aquellos que se pueden separar con una línea recta), la compuerta XOR es un problema que no es linealmente separable, lo que significa que no se puede separar los puntos en dos clases usando una línea recta. En particular, los puntos de entrada (0,0) y (1,1) pertenecen a una clase, mientras que los puntos (0,1) y (1,0) pertenecen a la otra clase. Cuando se intenta entrenar un perceptrón para aprender la compuerta XOR, el modelo no es capaz de encontrar una línea recta que separe los puntos en dos clases.

**¿Qué importancia tiene el factor de aprendizaje?**


El factor de aprendizaje es un valor que se utiliza para ajustar la magnitud de los cambios en los pesos de la red durante el entrenamiento. El factor de aprendizaje controla qué tan rápido o lento la red neuronal ajusta sus pesos en función de los errores cometidos durante el entrenamiento.
La importancia del factor de aprendizaje radica en que puede afectar significativamente el rendimiento del modelo del perceptrón. Si el factor de aprendizaje es demasiado pequeño, el modelo puede tardar mucho tiempo en converger y, en algunos casos, puede quedarse atascado en un mínimo local. Si el factor de aprendizaje es demasiado grande, el modelo puede oscilar demasiado entre los pesos y no converger. Por lo tanto, elegir un factor de aprendizaje apropiado es crucial para lograr un buen rendimiento del modelo del perceptrón.
