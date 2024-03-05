# Red Neuronal Multicapa

**By: Dexne**

## ¿Qué es una red neuronal multicapa?

Una red neuronal multicapa (MLP, por sus siglas en inglés Multilayer Perceptron) es un tipo de red neuronal artificial que consiste en múltiples capas de neuronas interconectadas. Estas redes están compuestas por una capa de entrada, una o más capas ocultas y una capa de salida. Cada capa, excepto la de entrada, está compuesta por un conjunto de neuronas (también llamadas nodos o unidades) que están conectadas a las neuronas de la capa anterior y posterior mediante conexiones ponderadas.

La estructura de capas múltiples permite a las MLP aprender representaciones de datos complejas y no lineales mediante la combinación de transformaciones lineales y no lineales. Las neuronas en cada capa oculta calculan una combinación lineal de las salidas de las neuronas en la capa anterior, seguida de una función de activación no lineal. Estas funciones de activación introducen no linealidades en el modelo, lo que permite a la red aprender y modelar relaciones más complejas en los datos.

Las redes neuronales multicapa se utilizan en una amplia gama de aplicaciones de aprendizaje automático y reconocimiento de patrones, incluyendo clasificación, regresión, reconocimiento de voz, procesamiento de imágenes, procesamiento de lenguaje natural, entre otros. Su capacidad para modelar relaciones complejas en los datos y su flexibilidad las convierten en una herramienta poderosa para resolver una variedad de problemas de aprendizaje automático.

## Instrucciones

Para el conjunto de datos siguiente usa el código generado en clase para clasificar los datos correctamente. Gráfica los datos como se vio en clase para verificar tu arquitectura.

Archivos disponibles:

- [moons.csv]()
- [XOR.csv]()
- [circles.csv]()
- [blobs.csv]

# Resultados obtenidos

## XOR

**Valores de ajuste**

Entradas: 2

Salidas: 1

Función de activación interna: tanh

Función de activación salida: logistica

Épocas: 300

![XOR_n1]()

![XOR_n4]()

![XOR_n7]()

![XOR_n10]()

## Blobs

**Valores de ajuste**

Entradas: 2

Salidas: 1

Función de activación interna: tanh

Función de activación salida: logistica

Épocas: 300

![Blobs_n1]()

![Blobs_n5]()

![Blobs_n10]()

![Blobs_n20]()

## Circles

**Valores de ajuste**

Entradas: 2

Salidas: 1

Función de activación interna: tanh

Función de activación salida: logistica

Épocas: 300

![Circles_n1]()

![Circles_n10]()

![Circles_n30]()

![Circles_n60]()

## Moons

**Valores de ajuste**

Entradas: 2

Salidas: 1

Función de activación interna: tanh

Función de activación salida: logistica

Épocas: 300

![Moons_n1]()

![Moons_n50]()

![Moons_n300]()

![Moons_n700]()


