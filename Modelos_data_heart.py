# -*- coding: utf-8 -*-
"""TRABAJO DE ANALISIS DE DATOS CON PYTHON 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1APnoqylXxTkvvNhGUh-arXMn4pHfSDSX

# Data de corazón
"""

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor as KNr
import plotly.graph_objects as go
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split as tts


print('A continuación se presenta una data dataset pacientes UCI para diagnóstico de enfermedad al corazón')
print('')
print('1.age (age in years)')
print('2.sex (1 = male; 0 = female)')
print('3.cp (chest pain type)')
print('4.trestbps(resting blood pressure (in mm Hg on admission to the hospital))')
print('5.chol (serum cholestoral in mg/dl)')
print('6.fbs (fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)')
print('7.restecg (resting electrocardiographic results)')
print('8.thalach (maximum heart rate achieved)')
print('9.exang (exercise induced angina (1 = yes; 0 = no))')
print('10.oldpeak (ST depression induced by exercise relative to rest)')
print('11.slope (the slope of the peak exercise ST segment)')
print('12.ca (number of major vessels (0-3) colored by flourosopy)')
print('13.thal (3 = normal; 6 = fixed defect; 7 = reversable defect)')
print('14.target (1 or 0)')
print('')
print('El modelo a ejecutar es de tipo KNN y realiza predicción del nivel de colesterol a partir de la edad')
print('')
heart_df=pd.read_csv('https://raw.githubusercontent.com/manuelrey94/PYTHON-TRABAJO/main/heart.csv')
heart_df

"""#Gráficas"""

import pandas
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

dataset = pandas.read_csv("https://raw.githubusercontent.com/manuelrey94/PYTHON-TRABAJO/ac9ff7a33b76166d39b6dfd6e4fc0c66289b3c3b/heart.csv")
dataset.head()
x_edad = list(dataset['age'])
y_trestbps = list(dataset['trestbps'])
fig1 = px.scatter(x = x_edad, y= y_trestbps , color_discrete_sequence=['rgb(255,0,0)'])
fig1.show()

import pandas
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

dataset = pandas.read_csv("https://raw.githubusercontent.com/manuelrey94/PYTHON-TRABAJO/ac9ff7a33b76166d39b6dfd6e4fc0c66289b3c3b/heart.csv")
dataset.head()
x_edad = list(dataset['age'])
y_thalach = list(dataset['thalach'])
fig1 = px.scatter(x = x_edad, y= y_thalach , color_discrete_sequence=['rgb(255,0,0)'])
fig1.show()

fig4 = px.scatter(dataset, x = 'age',y  = 'trestbps', color = 'sex',facet_col ='cp')
fig4.show()

fig5 = px.scatter(dataset, x = 'age',y  = 'chol', color = 'sex',facet_col ='cp')
fig5.show()

fig6 = px.scatter(dataset, x = 'age',y  = 'thalach', color = 'sex',facet_col ='cp')
fig6.show()

fig7 = px.scatter(dataset, x = 'age',y  = 'oldpeak', color = 'sex',facet_col ='cp')
fig7.show()

"""#Datos estadísticos"""

dataset.describe()

import plotly.express as px
import numpy as np
df_heart = pd.read_csv('https://raw.githubusercontent.com/manuelrey94/PYTHON-TRABAJO/main/heart.csv')
t= np.linspace(0,np.pi)
fig3 = px.line(x=t, y= np.sin(t), labels={'x':'age', 'y':'trestbps'})
fig3.show()

dataset.hist()

fig1= px.scatter(dataset, x= 'age', y= 'trestbps', trendline = 'ols')
fig1.show()

import plotly.figure_factory as ff

target_arr_list=[np.array(dataset['age'])]
group_labels=['Rango de edades']
fig9=ff.create_distplot(target_arr_list,group_labels,bin_size=4) #bin_size me va a determinar el tamaño de la distribución de los datos
fig9.show()

"""# MODELO 1: **KNN** para regresión en la data heart desease (nivel de colesterol vs edad)"""

heart_df=pd.read_csv('https://raw.githubusercontent.com/manuelrey94/PYTHON-TRABAJO/main/heart.csv')
heart_df

X = np.array(heart_df['age'])
y =  np.array(heart_df['chol'])
print(np.shape(X))
print(np.shape(y))
X = np.reshape(X,(303,1))
y = np.reshape(y,(303,1))
print(np.shape(X))
print(np.shape(y))

from pandas.core.common import random_state
from sklearn import neighbors

Xtrain,Xtest,ytrain,ytest = tts(X,y,test_size = 0.10,random_state = 12)
modeloknnr = KNr(n_neighbors=1)
modeloknnr.fit(Xtrain,ytrain) 
print(np.shape(Xtrain))
print(np.shape(Xtest))
print(np.shape(ytrain))
print(np.shape(ytest))

print(np.max(X))
print(np.min(X))
print(np.max(y))
print(np.min(y))

Xr = np.linspace(10,100,90) 
Xr = np.reshape(Xr,(90,1))

ypredtrain = modeloknnr.predict(Xtrain) 
ypredtest = modeloknnr.predict(Xtest)
r2modelknntrain = r2_score(ytrain,ypredtrain)
r2modelknntest = r2_score(ytest,ypredtest)

print('A continuación se muestran los coeficientes r2  del set de entrenamiento y el set de validación')
print('')

print(r2modelknntrain)
print(r2modelknntest)

Xtrainr = np.reshape(Xtrain,(272,))
ytrainr = np.reshape(ytrain,(272,))
yr =modeloknnr.predict(Xr)
Xrr = np.reshape(Xr,(90,))
yrr = np.reshape(yr,(90,))
Xtestr = np.reshape(Xtest,(31,))
ytestr = np.reshape(ytest,(31,))

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=Xtrainr,y = ytrainr, mode ='markers',marker_color = 'orange'))
fig1.add_trace(go.Scatter(x=Xrr,y = yrr))
fig1.add_trace(go.Scatter(x = Xtestr, y= ytestr, mode = 'markers', marker_color = 'green'))
fig1.show()

"""# MODELO 2 Comparación entre modelo **ridge y lasso** para la data heart desease """

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso


print('A continuación se presenta una data dataset pacientes UCI para diagnóstico de enfermedad al corazón')
print('')
print('1.age (age in years)')
print('2.sex (1 = male; 0 = female)')
print('3.cp (chest pain type)')
print('4.trestbps(resting blood pressure (in mm Hg on admission to the hospital))')
print('5.chol (serum cholestoral in mg/dl)')
print('6.fbs (fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)')
print('7.restecg (resting electrocardiographic results)')
print('8.thalach (maximum heart rate achieved)')
print('9.exang (exercise induced angina (1 = yes; 0 = no))')
print('10.oldpeak (ST depression induced by exercise relative to rest)')
print('11.slope (the slope of the peak exercise ST segment)')
print('12.ca (number of major vessels (0-3) colored by flourosopy)')
print('13.thal (3 = normal; 6 = fixed defect; 7 = reversable defect)')
print('14.target (1 or 0)')

print('')
print('El modelo a ejecutar es de tipo  Lasso vs regresión lineal  y realiza predicción del nivel de colesterol a partir de la edad, presión sanguínea y el valor ST del electrocardiograma ')
print('')

heart_df

array_age = np.array(heart_df['age'])
array_trestbps = np.array(heart_df['trestbps'])
array_oldpeak = np.array(heart_df['oldpeak'])


Xla = np.c_[array_age,array_trestbps,array_oldpeak]
yla = np.array(heart_df['chol'])
yla = np.reshape(yla,(303,1))

Xlatrain,Xlatest,ylatrain,ylatest = tts(Xla,yla,test_size=296,random_state=152)
modelLasso = Lasso(alpha = 0.5)
modelLinear = LinearRegression()

r2listt = []
r2listpr = []
for i in [modelLasso,modelLinear]:
  i.fit(Xlatrain,ylatrain)
  ytrainp = i.predict(Xlatrain)
  ytestp = i.predict(Xlatest)
  r2t = r2_score(ylatrain,ytrainp) 
  r2listt.append(r2t)
  r2test = r2_score(ylatest,ytestp) 
  r2listpr.append(r2test)

print('A continuación se presentan los coeficientes r2 de comparación entre el modelo lasso y el modelo de regresión lineal')
print('')
print(r2listt)
print(r2listpr)

"""# 3. MODELO 3: Modelo Ridge de Regresión vs regresión lineal"""

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso


print('A continuación se presenta una data dataset pacientes UCI para diagnóstico de enfermedad al corazón')
print('')
print('1.age (age in years)')
print('2.sex (1 = male; 0 = female)')
print('3.cp (chest pain type)')
print('4.trestbps(resting blood pressure (in mm Hg on admission to the hospital))')
print('5.chol (serum cholestoral in mg/dl)')
print('6.fbs (fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)')
print('7.restecg (resting electrocardiographic results)')
print('8.thalach (maximum heart rate achieved)')
print('9.exang (exercise induced angina (1 = yes; 0 = no))')
print('10.oldpeak (ST depression induced by exercise relative to rest)')
print('11.slope (the slope of the peak exercise ST segment)')
print('12.ca (number of major vessels (0-3) colored by flourosopy)')
print('13.thal (3 = normal; 6 = fixed defect; 7 = reversable defect)')
print('14.target (1 or 0)')

print('')
print('El modelo a ejecutar es de tipo Ridge vs regresión lineal  y realiza predicción del nivel de colesterol a partir de la edad, presión sanguínea y el valor ST del electrocardiograma ')
print('')

heart_df

array_age = np.array(heart_df['age'])
array_trestbps = np.array(heart_df['trestbps'])
array_oldpeak = np.array(heart_df['oldpeak'])


Xla = np.c_[array_age,array_trestbps,array_oldpeak]
yla = np.array(heart_df['chol'])
yla = np.reshape(yla,(303,1))

Xlatrain,Xlatest,ylatrain,ylatest = tts(Xla,yla,test_size=296,random_state=152)
modelRidge = Ridge(alpha = 0.5)

modelLinear = LinearRegression()

r2listt = []
r2listpr = []
for i in [modelRidge,modelLinear]:
  i.fit(Xlatrain,ylatrain)
  ytrainp = i.predict(Xlatrain)
  ytestp = i.predict(Xlatest)
  r2t = r2_score(ylatrain,ytrainp) 
  r2listt.append(r2t)
  r2test = r2_score(ylatest,ytestp) 
  r2listpr.append(r2test)

print('A continuación se presentan los coeficientes r2 de comparación ente el modelo ridge y el modelo de regresión lineal')
print('')
print(r2listt)
print(r2listpr)

"""# 4. MODELO 4 : Clasificación binaria-regresión logística (diagnóstico de enfermedad al corazón )"""

import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso


print('A continuación se presenta una data dataset pacientes UCI para diagnóstico de enfermedad al corazón')
print('')
print('1.age (age in years)')
print('2.sex (1 = male; 0 = female)')
print('3.cp (chest pain type)')
print('4.trestbps(resting blood pressure (in mm Hg on admission to the hospital))')
print('5.chol (serum cholestoral in mg/dl)')
print('6.fbs (fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)')
print('7.restecg (resting electrocardiographic results)')
print('8.thalach (maximum heart rate achieved)')
print('9.exang (exercise induced angina (1 = yes; 0 = no))')
print('10.oldpeak (ST depression induced by exercise relative to rest)')
print('11.slope (the slope of the peak exercise ST segment)')
print('12.ca (number of major vessels (0-3) colored by flourosopy)')
print('13.thal (3 = normal; 6 = fixed defect; 7 = reversable defect)')
print('14.target (1 or 0)')

print('')
print('El modelo a ejecutar es de clasificación binaria y permite determinar el diagnóstico de enfermedad al corazón ( 1 (sí tiene la enfermedad) 0 (no tiene la enfermedad)) ')
print('')

heart_df


heart_df=pd.read_csv('https://raw.githubusercontent.com/manuelrey94/PYTHON-TRABAJO/main/heart.csv')
heart_df

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split as tts
import numpy as np
from sklearn.metrics import recall_score, precision_score

x1 = np.array(heart_df['age'])
x2 = np.array(heart_df['trestbps'])
x3 = np.array(heart_df['chol'])
x4 = np.array(heart_df['thalach'])
x5 = np.array(heart_df['oldpeak'])
X = np.c_[x1,x2,x3,x4,x5]
y = np.array(heart_df['target'])
y = np.reshape(y,(303,))

Xtrain,Xtest,ytrain,ytest = tts(X,y,test_size = 0.20, random_state = 32)
modellogist = LogisticRegression(max_iter=200)
modellogist.fit(Xtrain,ytrain)

Xtrain,Xtest,ytrain,ytest = tts(X,y,test_size = 0.20, random_state = 32)
modellogist = LogisticRegression(max_iter=200)
modellogist.fit(Xtrain,ytrain)

ypredtest = modellogist.predict(Xtest)
ypredtrain = modellogist.predict(Xtrain)

precision = precision_score(ytest,ypredtest)
print(round(precision,2))

x_1 = float(input('Ingresa el valor de tu edad: '))
x_2 = float(input('Ingresa el valor de tu presión sanguínea: '))
x_3 = float(input('Ingresa el valor de tu colesterol en la sangre: '))
x_4 = float(input('Ingresa el valor de tus latidos por minuto: '))
x_5 = float(input('Ingrese el valor del ST del electrocardiograma: '))
X_ = np.c_[x_1,x_2,x_3,x_4,x_5]
diagnostico = int(modellogist.predict(X_))
print(('1 si tiene enfermedad al corazón y 0 si no, su resultado es: ',diagnostico))

