import numpy as np
from PIL import Image
import requests
from fastapi import FastAPI
import cv2
from rembg import remove

######Meter letras que no solapa
def letras_sin(path, path_l):
    #1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img_original = cv2.imread(path)

    #3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img.paste(letras, (1220,240), letras.convert("RGBA"))
    return img


######Meter letras que solapa
def letras_con(path,path_l):
    #1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img_original = cv2.imread(path)

    #2 - remove background
    car = remove(img_pil_original)

    #3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img.paste(letras, (1220,240), letras.convert("RGBA"))
    img

    #meter el cotxe encima de las letras
    img_pil = img
    img_pil.paste(car, (0,0), car.convert("RGBA"))
    return img_pil


#####Control
def check(path,path_l):
    #1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img_original = cv2.imread(path)

    #2 - remove background
    car = remove(img_pil_original)

    #3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))#opencv - PIL
    img.paste(car, (0,0), car.convert("RGBA"))
    img.paste(letras, (1220,240), letras.convert("RGBA"))
    return img

#####insertar_letras
def insertar_letras(path, path_l):
    im1 = check(path, path_l)
    im2 = letras_con(path, path_l)
    im3 = cv2.cvtColor(np.asarray(im1),cv2.COLOR_RGB2BGR) #PIL - opencv
    im4 = cv2.cvtColor(np.asarray(im2),cv2.COLOR_RGB2BGR) #PIL - opencv
    dif = cv2.subtract(im4,im3)
    if not np.any(dif):
        img = letras_sin(path,path_l)
    else:
        img = letras_con(path,path_l)
    return img
def path_font(id):
    if id == 1:
        return 'font/f_alcobendas.png'
    if id == 2:
        return 'font/f_alcorcon.png'
    if id == 3:
        return 'font/f_alcorconii.png'
    if id == 4:
        return 'font/f_aravaca.png'
    if id == 5:
        return 'font/f_badalonaii.png'
    if id == 6:
        return 'font/f_esplugues.png'
    if id == 7:
        return 'font/f_girona.png'
    if id == 8:
        return 'font/f_irun.png'
    if id == 9:
        return 'font/f_lasrozas.png'
    if id == 10:
        return 'font/f_leon.png'

app = FastAPI()

@app.get("/my-first-api")
def hello(name: str):
    id_position = name[23:25]
    if int(id_position) < 7:
        id = path_font(2)
        img = insertar_letras(name, id)
        #guarda la imagen en la carpeta prueba
        img.save('resultados/prueba18.png')
    else:
        return 'interior'
    return img

if __name__ == '__main__':
  resp = requests.get('http://127.0.0.1:8000/my-first-api?name=coches/5776LGX/5776LGX_01_front-right.jpg')



##PRUEBAS

# resp = requests.get('http://127.0.0.1:8000/api_il?path=coches/5776LGX/5776LGX_06_feature-1.jpg')
# print(resp.text)

######api


# folder_path = 'coches/0609JFR'
# folder_info =  os.listdir(folder_path)
# for image in folder_info:
# image_path = os.path.join(folder_path, image)
# print(image_path)
# resp = requests.get('http://127.0.0.1:8000/items/6?q='+image_path)

# resp = requests.get('http://127.0.0.1:8000/items/6?q=coches/5776LGX/5776LGX_07_rear.jpg')
