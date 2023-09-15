#!/usr/bin/env python
# coding: utf-8

# In[34]:


#https://statso.io/fitness-data-analysis-case-study/
import pandas as pd
import plotly.express as px

data = pd.read_csv("C:/Users/ferbu/OneDrive/Escritorio/DATA/Apple-Fitness-Data.csv", sep=",")


# In[35]:


#Visualizamos los primeros 5 valores y todas las columans de dataset
#observamos que esta organizado por fecha 
data.head()


# In[36]:


data.info()
#observamos que no hay valores nulos  


# In[37]:


#realizamos un grafico de pasos en funcion del tiempo 
fig1 = px.line(data, x ="Time", y = "Step Count" ,title= "Step count over Time ")
fig1.show()


# In[26]:


#realizamos un grafico  de distancia en funcion del tiempo 
fig2 = px.line(data, x ="Time", y = "Distance", title ="Distance over Time ")
fig2.show()


# In[27]:


#realizamos un grafico de energia quemada en funcion del tiempo 
fig3 = px.line(data, x ="Time", y = "Energy Burned", title ="Energy Burned over Time "  )
fig3.show()


# In[28]:


#realizamos un cuadro de la velocidad en funcion del tiempo 
fig4 = px.line(data, x="Time", y="Walking Speed", title = "Walking Speed Over time ")
fig4.show()


# In[29]:


#queremos ver el promedio de pasos en funcion del tiempo
average = data.groupby("Date")["Step Count"].mean().reset_index()

fig5 =px.bar(average, x="Date", y ="Step Count", title="Step Over time")


fig5.show()


# In[ ]:





# In[ ]:




