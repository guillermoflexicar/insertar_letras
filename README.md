# insertar_letras
En pruebas.py encontramos el código que nos permitirá utilizar la api. En la llamada a la api se le pasa un numero de identificación del
concesionario y el path de la imagen. Dentro de la api mira si es una imagen interior o exterior dependiendo de si es de las 7 primeras.
En caso de que sea exterior llama a la función insertar letras y después se guarda el resultado en la carpeta resultados. También retorna la
imagen para tener esa opción en el momento de montar la estructura final. En el caso de que no sea exterior retorna interior, pero que eso 
también se puede eliminar si no es necesario.

Para esta primera prueba he creado lo que seria un circuito interno donde en una carpeta estan las imágenes de los coches, en otra estan
las imágenes de las fuentes y en otra se guardan los resultados. Esto lo modificaremos cuando trabajemos directamente con los buckets
correspondientes.

Para ejecutar la api, trabajo en pycharm y la ejecuto desde allí utilizando requests, aunque previamente llamo el siguiente comando desde terminal, 
dentro de la carpeta insertar_letras, para poder trabajar con FastApi:
uvicorn api:app --reload

Ejemplo de la llamada:
requests.get('http://127.0.0.1:8000/items/6?q=coches/5776LGX/5776LGX_07_rear.jpg')
El 6 hace referencia al id del concesionario y lo de despues de la q es el path de la imagen del coche.

He puesto tres carpetas de pruebas con los resultados correspondientes despues de ejecutar el código con cada imagen.
