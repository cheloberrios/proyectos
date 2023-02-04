from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt
import streamlit as st
import lxml
import seaborn as sns
import plotly.express as px


#me traigo la data desde la paginas y creo el data frame que lo va a contoner 
paginas = ("https://listado.mercadolibre.cl/inmuebles/arriendo-casa-la-florida_Desde_49_NoIndex_True","https://listado.mercadolibre.cl/inmuebles/arriendo-casa-la-florida_NoIndex_True#D[A:arriendo%20casa%20la%20florida,on]","https://listado.mercadolibre.cl/inmuebles/casas/arriendo/propiedades-usadas/rm-metropolitana/puente-alto/arriendo-casa-puente-alto_Desde_49_NoIndex_True", "https://listado.mercadolibre.cl/inmuebles/casas/arriendo/propiedades-usadas/rm-metropolitana/puente-alto/arriendo-casa-puente-alto", "https://listado.mercadolibre.cl/inmuebles/casas/arriendo/propiedades-usadas/rm-metropolitana/puente-alto/arriendo-casa-puente-alto_Desde_97_NoIndex_True" )
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['precio', 'detalle1', 'detalle2'])

#Iteracion para sacar una scraping por cada pagina en la lista de paginas 
for pagina in paginas:
    website= pagina
    result= requests.get(website)
    content = result.text
 #defino el lugar desde donde se iterara    
    soup = BeautifulSoup(content, 'lxml')
 #individualizo las casas   
    casas = soup.find_all('li', class_='ui-search-layout__item')
    print("pagina finalizada")
    
#itero para generar una linea por cada casa
    for casa in casas:
        precio = casa.find('span', class_='price-tag-fraction').get_text()
        detalle1 = casa.find('ul', class_='ui-search-card-attributes ui-search-item__group__element shops__items-group-details').get_text()
        detalle2 = casa.find('h2', class_='ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title').get_text()
        detalle3 = casa.find('a', class_='ui-search-link').get_text()
        print(precio,detalle1,detalle2)
        df.loc[len(df)] = [precio,detalle1,detalle2]

#elimino filas remplazo puntos  por nada y cambio de formato fila precio
df['precio'] = df['precio'].fillna(1)
df['precio'] = df['precio'].replace('\.', '', regex=True)
df['precio'] = df['precio'].astype(float)

#ordeno por precio
df_ordenado = df.sort_values(by="precio")
print("termino 0")
print("termino 1")
#separa los metros cuadrador de el resto de la descripcion
df_ordenado['detalle1'] = df_ordenado['detalle1'].str.split(' ')

df_ordenado2 = pd.DataFrame
df_ordenado2 = df_ordenado['detalle1'].apply(lambda x: pd.Series(x))
#le paso la lista a valores para remplazar la columna y le cambio el nombre a la columna 
valores = df_ordenado2[0]
df_ordenado['detalle1'] = valores
df_ordenado.rename(columns={'detalle1': 'metros'}, inplace=True)


col1 = df_ordenado['metros']
col2 = df_ordenado['precio']
# elimino filas y COLUMNAS.  saco valores que rompen la visualizacion 

df_ordenado.drop([0, 1], axis=0, inplace=True)
df_ordenado[df_ordenado['precio'] < 750000]


fig = px.scatter(df_ordenado, x='metros', y='precio')

#event_data = st.plotly_chart(fig, 'selected')

#if event_data is not None:
 #   x = event_data['points'][0]['x']
  #  y = event_data['points'][0]['y']
   # st.write(f'Valores seleccionados: x = {x}, y = {y}')

#st.print(event_data)

st.plotly_chart(fig)


st.table(df_ordenado)
df_ordenado['metros'] = df_ordenado['metros'].astype(float)

#filtro 



corr = df_ordenado.corr()
st.table(corr)

fig = px.imshow(corr,
                x=corr.columns,
                y=corr.columns,
                color_continuous_scale='magma',
                title='Correlación entre var1 y var2')

st.plotly_chart(fig)

#st.heatmap([col1, col2], xlabel="Columna 1", ylabel="Columna 2")

df_ordenado.info()


# Crea una función que filtra el DataFrame y muestra la tabla
#def filter_data(precio):
    #df_ordenado = df_ordenado.loc[df_ordenado['precio'] == precio]
    #st.write(df_ordenado)

# Agrega un widget de selección de color al gráfico
#color_widget = st.sidebar.selectbox('Selecciona un color', df['precio'].unique())

# Llama a la función de filtrado al seleccionar un valor en el widget
#filter_data(color_widget)
#st.table(df_ordenado2[0])

# Supongamos que tenemos un data frame llamado `df` con dos filas y tres columnas

# Agregamos una fila al final del data frame
#df.loc[len(df)] = [precio,detalle1,detalle2]

#print(df)
#df.plot()

# Mostramos el gráfico
#plt.show()



#df = pd.DataFrame(opciones, columns=['col1', 'col2', 'col3'])

#print(f"esto es eldf)