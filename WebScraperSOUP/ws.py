from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt
import streamlit as st
import lxml
import seaborn as sns
import plotly.express as px


    
paginas = ("https://listado.mercadolibre.cl/inmuebles/arriendo-casa-la-florida_Desde_49_NoIndex_True","https://listado.mercadolibre.cl/inmuebles/arriendo-casa-la-florida_NoIndex_True#D[A:arriendo%20casa%20la%20florida,on]","https://listado.mercadolibre.cl/inmuebles/casas/arriendo/propiedades-usadas/rm-metropolitana/puente-alto/arriendo-casa-puente-alto_Desde_49_NoIndex_True", "https://listado.mercadolibre.cl/inmuebles/casas/arriendo/propiedades-usadas/rm-metropolitana/puente-alto/arriendo-casa-puente-alto", "https://listado.mercadolibre.cl/inmuebles/casas/arriendo/propiedades-usadas/rm-metropolitana/puente-alto/arriendo-casa-puente-alto_Desde_97_NoIndex_True" )
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['precio', 'detalle1', 'detalle2'])

for pagina in paginas:
    website= pagina
    result= requests.get(website)
    content = result.text

    soup = BeautifulSoup(content, 'lxml')
    casas = soup.find_all('li', class_='ui-search-layout__item')
    print("pagina finalizada")
    

    for casa in casas:
        precio = casa.find('span', class_='price-tag-fraction').get_text()
        detalle1 = casa.find('ul', class_='ui-search-card-attributes ui-search-item__group__element shops__items-group-details').get_text()
        detalle2 = casa.find('h2', class_='ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title').get_text()
        print(precio,detalle1,detalle2)
        df.loc[len(df)] = [precio,detalle1,detalle2]


#metros = df("detalle1")
#metros = metros[["detalle1", "detalle4"]] = df["detalle1"].str.split(" ", expand=True)
df['precio'] = df['precio'].fillna(1)
#df['precio'] = df['precio'].str.replace('[\.]', '')
df['precio'] = df['precio'].replace('\.', '', regex=True)

df['precio'] = df['precio'].astype(float)
#print(df)
df_ordenado = df.sort_values(by="precio")
print("termino 0")
print("termino 1")

df_ordenado['detalle1'] = df_ordenado['detalle1'].str.split(' ')

df_ordenado2 = pd.DataFrame
df_ordenado2 = df_ordenado['detalle1'].apply(lambda x: pd.Series(x))
valores = df_ordenado2[0]
df_ordenado['detalle1'] = valores
df_ordenado.rename(columns={'detalle1': 'metros'}, inplace=True)


col1 = df_ordenado['metros']
col2 = df_ordenado['precio']

df_ordenado.drop(['detalle2'], axis=1, inplace=True)
df_ordenado.drop([0, 1], axis=0, inplace=True)
df_ordenado.drop([224], axis=0, inplace=True)


fig = px.scatter(df_ordenado, x='metros', y='precio')
st.plotly_chart(fig)

st.table(df_ordenado)
df_ordenado['metros'] = df_ordenado['metros'].astype(float)


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