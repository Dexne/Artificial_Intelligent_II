# Red neuronal de una capa

**By: Dexne**

## ¿Qué es una red neuronal de una capa?

Una red neuronal de una capa, también conocida como perceptrón, es el tipo más simple de red neuronal artificial. Consiste en un conjunto de neuronas organizadas en una única capa, donde cada neurona está conectada a todas las entradas de la red. Cada conexión entre una neurona y una entrada tiene asociado un peso que determina la contribución de esa entrada a la neurona.

En una red neuronal de una capa, la salida de cada neurona se calcula como una combinación lineal de las entradas, ponderadas por los pesos respectivos, seguida de la aplicación de una función de activación. Comúnmente, la función de activación utilizada es la función de paso, que produce una salida binaria basada en si la suma ponderada de las entradas supera un umbral determinado.

## ¿Qué es softmax?

En inteligencia artificial (IA), especialmente en el ámbito del aprendizaje profundo y las redes neuronales, softmax es una función de activación utilizada comúnmente en la capa de salida de una red neuronal para convertir las salidas brutas en una distribución de probabilidad.

La función softmax toma un vector de números reales como entrada y devuelve otro vector de la misma longitud, donde cada elemento del vector de salida representa la probabilidad de que la entrada pertenezca a una de las posibles clases. La función softmax calcula estas probabilidades normalizando exponencialmente los valores de entrada y luego dividiendo cada valor por la suma de todas las exponenciales, asegurando que la suma de las probabilidades resultantes sea igual a uno.

La función softmax es especialmente útil en problemas de clasificación multiclase, donde se busca asignar una instancia de entrada a una de varias clases diferentes. La salida de softmax proporciona una interpretación intuitiva de las salidas de la red neuronal como probabilidades que pueden ser utilizadas para tomar decisiones de clasificación.

### Resultados obtenidos

Ejemplo 1

![Ejemplo 1](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T05/Figure_1.png)

Ejemplo 2

![Ejemplo 2](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T05/Figure_2.png)
