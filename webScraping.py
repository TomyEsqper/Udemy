import bs4
import requests

#Crear URL sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'


#lista titulos con 4 o 5 estrellas
Lista_rating = []

#Iterar paginas
for pagina in range(1, 51):
    
    #crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar libros
    for libro in libros:
        
        #checar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):

            #guardar titulo en variable 
            titulo_libro = libro.select('a')[1]['title']

            #agregar libro a la lista
            Lista_rating.append(titulo_libro)

#ver libros 4 o 5 estrellas en la consola
for t in Lista_rating:
    print(t)
