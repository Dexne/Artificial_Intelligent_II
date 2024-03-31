# Máquina de Soporte Vectorial

**By: Dexne**

# Proyecto: Análisis de precios de vivienda

Este proyecto realiza un análisis de precios de vivienda utilizando técnicas de aprendizaje automático para predecir los precios de las viviendas. Se utiliza un conjunto de datos proporcionado en el archivo [home_data.csv](T08\home_sol.py).

## Contenido del proyecto

El proyecto consta de los siguientes archivos:

- [home_data.csv](T08\home_sol.py) Archivo de datos que contiene la información sobre las viviendas.
- home_sol.py Código para el análisis
- README.md Documentación del proyecto (este archivo).

## Objetivo

El objetivo de este proyecto es calcular el porcentaje de efectividad al tratar de predecir los precios de las viviendas utilizando técnicas de aprendizaje automático. Se realiza un análisis exploratorio de datos, seguido de la selección y entrenamiento de modelos de regresión.

## Instalación

No se requiere ninguna instalación especial para ejecutar este proyecto. Sin embargo, se necesitarán las siguientes bibliotecas de Python:

- numpy
- pandas
- scikit-learn

Estas bibliotecas se pueden instalar fácilmente utilizando pip:

```
pip install numpy pandas scikit-learn
```

## Uso

Para ejecutar este proyecto, simplemente asegurese de tener el archivo home_data.csv en la misma ruta que el archivo home_sol.py. Ejecute el archivo home_sol.py en cualquier ambiente compatible.

## Descripción del código

El archivo Home_sol.py contiene el código para el análisis y modelado de datos. Aquí hay una descripción de las principales secciones del código:

- **Importación de paquetes:** Se importan las bibliotecas necesarias, incluyendo numpy, pandas y scikit-learn.

- **Lectura de datos:** Se leen los datos del archivo home_data.csv utilizando pandas.

- **Selección de variables:** Se seleccionan las variables relevantes para el análisis, eliminando 'id', 'price', 'date' y 'zipcode' de los datos.

- **Normalización de datos:** Se normalizan los datos utilizando MinMaxScaler para escalar las características en un rango entre 0 y 1.

- **División de datos de entrenamiento y prueba:** Se dividen los datos normalizados en conjuntos de entrenamiento y prueba.

- **Creación y entrenamiento del modelo:** Se crea un modelo de regresión lineal utilizando LinearRegression y se entrena con los datos de entrenamiento.

- **Evaluación del modelo:** Se calcula el coeficiente de determinación (R^2) para evaluar el rendimiento del modelo tanto en los datos de entrenamiento como en los datos de prueba.

## Resultados

El modelo de regresión lineal muestra un rendimiento razonablemente bueno en los datos de entrenamiento y prueba, con coeficientes de determinación de aproximadamente **0.69** y **0.73** respectivamente.

## Contribución

Las contribuciones son bienvenidas. Si desea contribuir a este proyecto, no dude en enviar un pull request.

# Proyecto: Análisis de Estrellas

Este proyecto realiza un análisis de estrellas utilizando técnicas de aprendizaje automático para predecir la clase espectral y el color de las estrellas. Se utiliza un conjunto de datos proporcionado en el archivo [Stars.csv](T08\Stars.csv)


Proyecto: Análisis de Estrellas
Este proyecto realiza un análisis de estrellas utilizando técnicas de aprendizaje automático para predecir la clase espectral y el color de las estrellas. Se utiliza un conjunto de datos proporcionado en el archivo Stars.csv.

## Contenido del proyecto

El proyecto consta de los siguientes archivos:

- [Stars.csv:](T08\Stars.csv) Archivo de datos que contiene información sobre las estrellas.

- Star_sol.py: Código Python que contiene el análisis y modelado de datos.

- README.md: Documentación del proyecto (este archivo).

## Objetivo

El objetivo de este proyecto es calcular el porcentaje de acerciones al tratar de predecir la clase espectral y el color de las estrellas utilizando técnicas de aprendizaje automático. Se realiza un análisis exploratorio de datos, seguido de la selección y entrenamiento de modelos de clasificación.

## Instalación

No se requiere ninguna instalación especial para ejecutar este proyecto. Sin embargo, se necesitarán las siguientes bibliotecas de Python:

- pandas
- numpy
- scikit-learn

Estas bibliotecas se pueden instalar fácilmente utilizando pip:

```
pip install pandas numpy scikit-learn
```

## Uso

Para poder ejecutar el código asegurese de tener descargado y en la misma ruta los archivos Stars.csv y star_sol.py. Ejecute el archivo .py en un ambiente compatible

## Descripción del código

El archivo Star_sol.py contiene el código para el análisis y modelado de datos. Aquí hay una descripción de las principales secciones del código:

- **Importación de paquetes:** Se importan las bibliotecas necesarias, incluyendo pandas, numpy y scikit-learn.

- **Lectura de datos:** Se leen los datos del archivo Stars.csv utilizando pandas.

- **Codificación de variables categóricas:** Se codifican las variables categóricas 'Spectral Class' y 'Star color' utilizando LabelEncoder de scikit-learn.

- **Selección de variables:** Se seleccionan las variables independientes (X) y la variable dependiente (Y) para el análisis.

- **División de datos de entrenamiento y prueba:** Se dividen los datos en conjuntos de entrenamiento y prueba.

- **Creación y entrenamiento de modelos:** Se crean dos modelos de clasificación: uno utilizando Support Vector Machine (SVM) y otro utilizando Multilayer Perceptron (MLP). Los modelos se entrenan con los datos de entrenamiento.

- **Evaluación de los modelos:** Se evalúan los modelos utilizando los datos de entrenamiento y prueba, y se imprime el rendimiento de cada modelo en términos de precisión.

## Resultados

Los modelos de clasificación muestran un rendimiento bastante bueno en los datos de entrenamiento y prueba. El modelo SVM alcanza una precisión de aproximadamente 94% en el conjunto de entrenamiento y 86% en el conjunto de prueba, mientras que el modelo MLP alcanza una precisión de aproximadamente 93% en el conjunto de entrenamiento y 86% en el conjunto de prueba.

## Contribución

Las contribuciones son bienvenidas. Si desea contribuir a este proyecto, no dude en enviar un pull request.