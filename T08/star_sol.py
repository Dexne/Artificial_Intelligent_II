"""Star_sol.py By: Dexne

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H87No1lVuTBILU2FzGxokBQwkaztGmb2
"""

# Importamos paquetería
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline

# Leemos los datos
data = pd.read_csv('Stars.csv')

# Codify
le = LabelEncoder()

# Codificación de la variable categórica 'Spectral Class'
data[['Spectral Class']] = le.fit_transform(np.array(data[['Spectral Class']]).ravel()).reshape(-1,1)
labels = le.classes_
le = LabelEncoder()

# Almacenar las etiquetas codificadas para la variable 'Spectral Class'
data[['Star color']] = le.fit_transform(np.array(data[['Star color']]).ravel()).reshape(-1,1)

# Seleccionamos las variables independientes (X) y la variable dependiente (Y)
x = np.asanyarray(data.drop(columns=['Star category', 'Spectral Class']))
y = np.asanyarray(data[['Spectral Class']])

# Dividir los datos en conjuntos de entrenamiento y prueba
xtrain, xtest, ytrain, ytest = train_test_split( x, y, test_size=0.3 )

# Creamos dos modelos: SVC (Support Vector Machine) y MLP (Multilayer Perceptron)
model1 = Pipeline([('scaler', StandardScaler()),
                   ('SVM', SVC(gamma=1))])

model2 = Pipeline([('scaler', StandardScaler()),
                   ('mlp', MLPClassifier(hidden_layer_sizes=(100,),
                                         max_iter=500))])

# Entrenar y evaluar el modelo SVC
model1.fit(xtrain, ytrain.ravel())
print('SVC')
print('Train: ', model1.score( xtrain, ytrain.ravel() ))
print('Test: ', model1.score( xtest, ytest.ravel() ))

# Entrenar y evaluar el modelo MLP
model2.fit( xtrain, ytrain.ravel() )
print('MLP')
print('Train: ', model2.score( xtrain, ytrain.ravel() ))
print('Test: ', model2.score( xtest, ytest.ravel() ))

"""
    Results

Model1 - SVC
Train:  0.9404761904761905
Test:  0.8611111111111112

Model2 - MLP
Train:  0.9345238095238095
test:  0.8611111111111112
"""