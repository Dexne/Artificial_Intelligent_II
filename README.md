# Inteligencia Artificial 2

**By: Dexne**

## ¿Qué es la inteligencia artifical?

La inteligencia artificial (IA) es un campo de la informática que se enfoca en desarrollar sistemas y programas capaces de realizar tareas que, normalmente, requieren de la inteligencia humana. Estos sistemas emplean algoritmos y técnicas para aprender, razonar, percibir y actuar de manera autónoma, con el fin de resolver problemas, tomar decisiones o interactuar con el entorno de manera eficiente. La IA abarca diversos enfoques, como el aprendizaje automático, el procesamiento del lenguaje natural, la visión por computadora y la robótica, entre otros, y su aplicación abarca una amplia gama de áreas, desde la medicina hasta la conducción autónoma y la atención al cliente.

## Menú 📖
- **Tarea 02:** [Algoritmo del perceptrón](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T02)
- **Tarea 03:** [Neurona Lineal - ADALINE](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T03)
- **Tarea 04:** [Neurona Logística](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T04)
- **Tarea 05:** [softmax](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T05)
- **Tarea 06:** [Red Neuronal Multietiqueta](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T06)
- **Tarea 08:** [Máquina de Soporte Vectorial - SVM](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T08)

# Perceptrón

## Modelo de McCulloch-Pitts

El modelo de McCulloch-Pitts (También conocido como modelo de neurona artificial) es un modelo matemático que fue propuesto por Warren McCulloch y Walter Pitts en 1943. Es uno de los primeros modelos de la teoría de la inteligencia artificial y sigue siendo una parte importante de la investigación.
En el modelo de McCulloch-Pitts, una neurona se representa como un elemento básico que puede recibir señales de entrada y producir una señal de salida. Cada señal de entrada se asocia con un peso, que indica la importancia de la señal. La salida de la neurona se determina por una función de activación que evalúa la suma ponderada de las señales de entrada. Este modelo ha sido ampliamente utilizado como una base para el desarrollo de algoritmos de aprendizaje automático y para la investigación en la inteligencia artificial y la neurociencia computacional. Aunque es un modelo simplificado de una neurona real, ha sido muy útil para entender el funcionamiento de los sistemas de procesamiento de información en el cerebro.

## El algoritmo del Perceptrón

El algoritmo del Perceptrón es un algoritmo de aprendizaje automático supervisado que se utiliza para clasificar datos en dos categorías. Se basa en el modelo de McCulloch-Pitts y es uno de los primeros algoritmos de aprendizaje automático desarrollados.
El algoritmo del Perceptrón funciona asignando pesos a las características de los datos de entrada y aplicando una función de activación para producir una salida. La función de activación es una función lineal que toma en cuenta la suma ponderada de las señales de entrada. Si la salida es mayor que cero, la entrada se clasifica en una categoría, y si la salida es menor o igual a cero, se clasifica en otra categoría. El algoritmo se ajusta iterativamente a los datos de entrenamiento, ajustando los pesos para minimizar el número de errores de clasificación. Este proceso de ajuste de pesos se llama “entrenamiento” y se realiza utilizando una técnica de optimización, como el gradiente descendente.
Aunque el algoritmo del Perceptrón es muy simple, ha sido ampliamente utilizado y ha demostrado ser efectivo en una amplia variedad de problemas de clasificación. Sin embargo, también tiene algunas limitaciones, como su capacidad limitada para manejar problemas de clasificación no lineales.
Por esta razón, se han desarrollado algoritmos más avanzados como los árboles de decisión, las redes neuronales y los algoritmos de aprendizaje profundo.

**¿Por qué la compuerta XOR no puede ser aprendida por este modelo?**

El modelo del perceptrón es una red neuronal de una sola capa que puede aprender a clasificar datos linealmente seriales (aquellos que se pueden separar con una línea recta), la compuerta XOR es un problema que no es linealmente separable, lo que significa que no se puede separar los puntos en dos clases usando una línea recta. En particular, los puntos de entrada (0,0) y (1,1) pertenecen a una clase, mientras que los puntos (0,1) y (1,0) pertenecen a la otra clase. Cuando se intenta entrenar un perceptrón para aprender la compuerta XOR, el modelo no es capaz de encontrar una línea recta que separe los puntos en dos clases.

**¿Qué importancia tiene el factor de aprendizaje?**

El factor de aprendizaje es un valor que se utiliza para ajustar la magnitud de los cambios en los pesos de la red durante el entrenamiento. El factor de aprendizaje controla qué tan rápido o lento la red neuronal ajusta sus pesos en función de los errores cometidos durante el entrenamiento.
La importancia del factor de aprendizaje radica en que puede afectar significativamente el rendimiento del modelo del perceptrón. Si el factor de aprendizaje es demasiado pequeño, el modelo puede tardar mucho tiempo en converger y, en algunos casos, puede quedarse atascado en un mínimo local. Si el factor de aprendizaje es demasiado grande, el modelo puede oscilar demasiado entre los pesos y no converger. Por lo tanto, elegir un factor de aprendizaje apropiado es crucial para lograr un buen rendimiento del modelo del perceptrón.

Si deseas acceder al proyecto puedes hacerlo a través del siguiente enlace -> [Algoritmo del perceptrón](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T02).

# Neurona Lineal

Una neurona lineal es un tipo de neurona artificial en la que la salida es una función lineal de la suma ponderada de las entradas. En el contexto del aprendizaje automático, las neuronas lineales se utilizan a menudo como capas de entrada o capas de entrada o capas de salida en redes neuronales. También se pueden usar como capas ocultas, aunque en general, las capas no lineales son más efectivas para capturar relaciones complejas entre las entradas y salidas. Es importante tener en cuenta que la neurona lineal es una de las funciones de activación más simples, y si salida no está limitada a un rango específico, lo que puede dar lugar a problemas de saturación si los procesos son demasiado grandes.

Si deseas acceder al proyecto puedes hacerlo a través del siguiente enlace -> [Neurona Lineal - ADALINE](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T03).

# Neurona Logistica

La neurona logística, también conocida como perceptrón, es una unidad fundamental en las redes neuronales artificiales (ANNs) que se utiliza para modelar la probabilidad de que una entrada pertenezca a una clase específica.

En términos más simples: Es como una caja negra que toma información y te da la probabilidad de que algo sea cierto.

Si deseas acceder al proyecto puedes hacerlo a través del siguiente enlace -> [Neurona Logística](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T04).

# Red neuronal de una capa

## ¿Qué es una red neuronal de una capa?

Una red neuronal de una capa, también conocida como perceptrón, es el tipo más simple de red neuronal artificial. Consiste en un conjunto de neuronas organizadas en una única capa, donde cada neurona está conectada a todas las entradas de la red. Cada conexión entre una neurona y una entrada tiene asociado un peso que determina la contribución de esa entrada a la neurona.

En una red neuronal de una capa, la salida de cada neurona se calcula como una combinación lineal de las entradas, ponderadas por los pesos respectivos, seguida de la aplicación de una función de activación. Comúnmente, la función de activación utilizada es la función de paso, que produce una salida binaria basada en si la suma ponderada de las entradas supera un umbral determinado.

## ¿Qué es softmax?

En inteligencia artificial (IA), especialmente en el ámbito del aprendizaje profundo y las redes neuronales, softmax es una función de activación utilizada comúnmente en la capa de salida de una red neuronal para convertir las salidas brutas en una distribución de probabilidad.

La función softmax toma un vector de números reales como entrada y devuelve otro vector de la misma longitud, donde cada elemento del vector de salida representa la probabilidad de que la entrada pertenezca a una de las posibles clases. La función softmax calcula estas probabilidades normalizando exponencialmente los valores de entrada y luego dividiendo cada valor por la suma de todas las exponenciales, asegurando que la suma de las probabilidades resultantes sea igual a uno.

La función softmax es especialmente útil en problemas de clasificación multiclase, donde se busca asignar una instancia de entrada a una de varias clases diferentes. La salida de softmax proporciona una interpretación intuitiva de las salidas de la red neuronal como probabilidades que pueden ser utilizadas para tomar decisiones de clasificación.

Si deseas acceder al proyecto puedes hacerlo a través del siguiente enlace -> [softmax](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T05).

# Red Neuronal Multicapa

## ¿Qué es una red neuronal multicapa?

Una red neuronal multicapa (MLP, por sus siglas en inglés Multilayer Perceptron) es un tipo de red neuronal artificial que consiste en múltiples capas de neuronas interconectadas. Estas redes están compuestas por una capa de entrada, una o más capas ocultas y una capa de salida. Cada capa, excepto la de entrada, está compuesta por un conjunto de neuronas (también llamadas nodos o unidades) que están conectadas a las neuronas de la capa anterior y posterior mediante conexiones ponderadas.

La estructura de capas múltiples permite a las MLP aprender representaciones de datos complejas y no lineales mediante la combinación de transformaciones lineales y no lineales. Las neuronas en cada capa oculta calculan una combinación lineal de las salidas de las neuronas en la capa anterior, seguida de una función de activación no lineal. Estas funciones de activación introducen no linealidades en el modelo, lo que permite a la red aprender y modelar relaciones más complejas en los datos.

Las redes neuronales multicapa se utilizan en una amplia gama de aplicaciones de aprendizaje automático y reconocimiento de patrones, incluyendo clasificación, regresión, reconocimiento de voz, procesamiento de imágenes, procesamiento de lenguaje natural, entre otros. Su capacidad para modelar relaciones complejas en los datos y su flexibilidad las convierten en una herramienta poderosa para resolver una variedad de problemas de aprendizaje automático.

Si deseas acceder al proyecto puedes hacerlo a través del siguiente enlace -> [Red Neuronal Multietiqueta](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T06).

# Máquina de Soporte Vectorial - SVM

SVM (siglas en inglés de Support Vector Machine) es un algoritmo de aprendizaje supervisado utilizado en inteligencia artificial para resolver problemas de clasificación y regresión.

En la clasificación, SVM busca un hiperplano que separe de la mejor manera posible dos clases diferentes de puntos de datos. Este hiperplano maximiza el margen entre las dos clases, creando una separación clara entre ellas.

En la regresión, SVM busca un hiperplano que se ajuste lo mejor posible a los datos, minimizando el error de predicción.

Para más detalles acerca de este proyecto puedes hacerlo a través del siguiente enlace -> [Máquina de Soporte Vectorial - SVM](https://github.com/Dexne/Artificial_Intelligent_II/tree/main/T08)
