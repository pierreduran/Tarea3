#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Tarea 3 - Modelos probabílisticos de señales y sistemas
#Pierre Durán Guzmán
#B42323
#Grupo 01


# In[2]:


#Importar las librerías a utilizar
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import mpl_toolkits.mplot3d as mpl
plt.rcParams["figure.figsize"] = 12.8, 9.6


# In[3]:


#Importar los archivos csv de X y Y
xy = pd.read_csv("xy.csv",header=0,index_col=0)
xyp=pd.read_csv("xyp.csv",header=0)


# In[4]:


##Punto 1

#Primero debemos encontrar la mejor curva de ajuste (modelo probabilístico) 
#para las funciones de densidad marginales de X y Y

#declaramos los vectores de x y y a utilizar
#x iría de 5 a 15
xs=np.linspace(5,15,11)
#y iría de 5 a 25
ys=np.linspace(5,25,21)

#Luego calculamos los vectores que describen las funciones de densidad
#marginales de X y Y
X=np.sum(xy,axis=1) #suma a lo largo de y
print("La función de densidad marginal de X está descrita por:")
print(X)
Y=np.sum(xy,axis=0) #suma a lo largo de x
print("La función de densidad marginal de Y está descrita por:")
print(Y)


# In[5]:


#Una vez obtenidas las funciones de densidad marginales se procede 
#a graficar X y Y para ver su forma y encontrar la curva de ajuste
#que mejor se adapte a las graficas de las mismas

#Se observa que las graficas de X y Y tienen una forma de campana
#distorcionada por lo que se procede a realizar un ajuste con la 
#distribución Gaussiana

#se define primero la función de Gauss
def gauss(x,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

#se calculan los parámetros mu y sigma para la funcion marginal X
paramX,_=curve_fit(gauss,xs,X)
print("Los parametros de ajuste mu y sigma de la curva Gaussiana de X son:",paramX)

#se calculan los parámetros mu y sigma para la funcion marginal Y
paramY,_=curve_fit(gauss,ys,Y)
print("Los parametros de ajuste mu y sigma de la curva Gaussiana de Y son:",paramY)


# In[6]:


#Plot de la mejor curva de ajuste del modelo X obtenido
dist = stats.norm
pdf_fitted1 = dist.pdf(xs,*paramX)
plt.plot(xs, pdf_fitted1, 'o-')
plt.title("Mejor curva de ajuste (Gaussiana) de la marginal de X")
plt.xlabel("Datos de x")
plt.ylabel("Datos de la función marginal X")
plt.show()

#Plot de la mejor curva de ajuste del modelo Y obtenido
pdf_fitted2 = dist.pdf(ys, *paramY)
plt.plot(ys, pdf_fitted2, 'o-')
plt.title("Mejor curva de ajuste (Gaussiana) de la marginal de Y")
plt.xlabel("Datos de y")
plt.ylabel("Datos de la función marginal Y")
plt.show()


# In[7]:


#Punto 3
#Primero se procede a calcular la correlación
#para ello, usaremos el csv de xyp ya que es una mejor forma de calularla
x1=xyp["x"]
y1=xyp["y"]
p=xyp["p"]

#Determinando la correlación
corre=0;
for i in range(231):
    corre=corre+x1[i]*y1[i]*p[i]
print("El valor de correlación de los datos es:", corre)

#Determinando la covarianza
covarianza=corre-(9.90484381*15.0794609)
print("El valor de la covarianza de los datos es:", covarianza)

#Determinando el coeficiente de correlación (Pearson)
Pearson=covarianza/((3.29944288)*(6.02693776))
print("El valor del coeficiente de correlación (Pearson) es:", Pearson)


# In[8]:


#Punto 4
#Primero se proceden a gráficar las funciones de densidad 
#marginales en 2D de X y Y
plt.plot(xs,X)
plt.title("Grafica en 2D de la funcion de densidad marginal de X")
plt.xlabel("Datos de x")
plt.ylabel("Datos de la función marginal X")
plt.show()

plt.plot(ys,Y)
plt.title("Grafica en 2D de la funcion de densidad marginal de Y")
plt.xlabel("Datos de y")
plt.ylabel("Datos de la función marginal Y")
plt.show()

#Ahora, se procede a graficar la función de densidad conjunta
#en #d de los datos brindados
ax=plt.axes(projection='3d')
x3=x1
y3=y1
z3=p
ax.plot_trisurf(x3,y3,z3,cmap='twilight_shifted')
ax.set_title("Gráfica en 3D de la función de densidad conjunta")
ax.set_xlabel("Datos de x")
ax.set_ylabel("Datos de y")
ax.set_zlabel("Datos de p")


# In[ ]:




