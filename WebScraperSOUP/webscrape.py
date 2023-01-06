from bs4 import BeautifulSoup
import pandas as pd
import requests
import matplotlib.pyplot as plt
import streamlit as st
import lxml
    
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
print(df)
df_ordenado = df.sort_values(by="precio")
print("termino 0")
print("termino 1")


st.table(df_ordenado)
# Supongamos que tenemos un data frame llamado `df` con dos filas y tres columnas

# Agregamos una fila al final del data frame
#df.loc[len(df)] = [precio,detalle1,detalle2]

#print(df)
#df.plot()

# Mostramos el gráfico
#plt.show()



#df = pd.DataFrame(opciones, columns=['col1', 'col2', 'col3'])

#print(f"esto es eldf)