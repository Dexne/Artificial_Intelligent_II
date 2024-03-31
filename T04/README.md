# Neurona Logística

**By: Dexne**

## ¿Qué es una neurona logística?

Una neurona logística es una función matemática que transforma una entrada en una probabilidad. Se usa en redes neuronales para modelar la probabilidad de un evento.

En términos más simples:

Es como una caja negra que toma información y te da la probabilidad de que algo sea cierto.

## Instalación

Para ejecutar este código, se requiere la biblioteca de Python `numpy`. Puedes instalarla utilizando pip:

```bash
pip install numpy scikit-learn
```

## Detalles de implementación

La clase LogisticNeuron representa una neurona logística con los siguientes métodos:

- **predict_proba(X):** Calcula la probabilidad de que los datos de entrada X pertenezcan a la clase positiva.

- **predict(X, umbral):** Predice la clase de los datos de entrada X utilizando un umbral especificado (por defecto, 0.5).

- **fit(X, Y, epochs):** Entrena la neurona utilizando el método de Gradiente Descendente.

## Configuración

d = 8
η = 0.1
epochs = 10000

## Resultados obtenidos:

![Accurancy](https://github.com/Dexne/Artificial_Intelligent_II/blob/main/T04/Accurancy.png)

