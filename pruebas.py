import numpy as np
from PIL import Image
import requests
from fastapi import FastAPI
import cv2
from rembg import remove
import os
from tqdm import tqdm


######Meter letras que no solapa
def letras_sin(path, path_l):
    # 1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # opencv - PIL
    img_original = cv2.imread(path)

    # 3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # opencv - PIL
    img.paste(letras, (1220, 240), letras.convert("RGBA"))
    return img


######Meter letras que solapa
def letras_con(path, path_l):
    # 1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # opencv - PIL
    img_original = cv2.imread(path)

    # 2 - remove background
    car = remove(img_pil_original)

    # 3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # opencv - PIL
    img.paste(letras, (1220, 240), letras.convert("RGBA"))
    img

    # meter el cotxe encima de las letras
    img_pil = img
    img_pil.paste(car, (0, 0), car.convert("RGBA"))
    return img_pil


#####Control
def check(path, path_l):
    # 1 - leer imagen
    img = cv2.imread(path)
    img_pil_original = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # opencv - PIL
    img_original = cv2.imread(path)

    # 2 - remove background
    car = remove(img_pil_original)

    # 3 - meter letras
    letras = Image.open(path_l)
    img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # opencv - PIL
    img.paste(car, (0, 0), car.convert("RGBA"))
    img.paste(letras, (1220, 240), letras.convert("RGBA"))
    return img


#####insertar_letras
def insertar_letras(path, path_l):
    im1 = check(path, path_l)
    im2 = letras_con(path, path_l)
    im3 = cv2.cvtColor(np.asarray(im1), cv2.COLOR_RGB2BGR)  # PIL - opencv
    im4 = cv2.cvtColor(np.asarray(im2), cv2.COLOR_RGB2BGR)  # PIL - opencv
    dif = cv2.subtract(im4, im3)
    if not np.any(dif):
        img = letras_sin(path, path_l)
    else:
        img = letras_con(path, path_l)
    return img


def path_font(id):
    if id == 168:
        return 'font/f_sanfernando.png'
    if id == 172:
        return 'font/f_alcobendas.png'
    if id == 173:
        return 'font/f_sansebastiandelosreyes.png'
    if id == 174:
        return 'font/f_alcaladehenares.png'
    if id == 175:
        return 'font/f_leganes.png'
    if id == 178:
        return 'font/f_vaciamadrid.png'
    if id == 179:
        return 'font/f_fuenlabrada.png'
    if id == 182:
        return 'font/f_rivasii.png'
    if id == 183:
        return 'font/f_mostolesii.png'
    if id == 185:
        return 'font/f_zaragoza.png'
    if id == 186:
        return 'font/f_hospitales.png'
    if id == 187:
        return 'font/f_malaga.png'
    if id == 188:
        return 'font/f_sabadellii.png'
    if id == 189:
        return 'font/f_valladolid.png'
    if id == 190:
        return 'font/f_alicante.png'
    if id == 191:
        return 'font/f_badalona.png'
    if id == 192:
        return 'font/f_sansebastiandelosreyes.png'
    if id == 193:
        return 'font/f_bilbao.png'
    if id == 194:
        return 'font/f_sevilla.png'
    if id == 195:
        return 'font/f_sabadell.png'
    if id == 196:
        return 'font/f_aravaca.png'
    if id == 197:
        return 'font/f_valencia.png'
    if id == 198:
        return 'font/f_viladecans.png'
    if id == 199:
        return 'font/f_cordoba.png'
    if id == 200:
        return 'font/f_sevillaii.png'
    if id == 201:
        return 'font/f_bilbaoii.png'
    if id == 202:
        return 'font/f_esplugues.png'
    if id == 203:
        return 'font/f_murcia.png'
    if id == 204:
        return 'font/f_valenciaii.png'
    if id == 205:
        return 'font/f_salamanca.png'
    if id == 206:
        return 'font/f_granada.png'
    if id == 207:
        return 'font/f_granadaii.png'
    if id == 208:
        return 'font/f_malagaii.png'
    if id == 209:
        return 'font/f_vigo.png'
    if id == 210:
        return 'font/f_lasrozas.png'
    if id == 211:
        return 'font/f_sabadelliii.png'
    if id == 212:
        return 'font/f_castellon.png'
    if id == 213:
        return 'font/f_jaen.png'
    if id == 214:
        return 'font/f_granollers.png'
    if id == 215:
        return 'font/f_sevillaiii.png'
    if id == 216:
        return 'font/f_bilbaoiii.png'
    if id == 217:
        return 'font/f_zaragozaii.png'
    if id == 218:
        return 'font/f_almeria.png'
    if id == 219:
        return 'font/f_lacoruna.png'
    if id == 220:
        return 'font/f_xativa.png'
    if id == 221:
        return 'font/f_xativa.png'
    if id == 222:
        return 'font/f_toledo.png'
    if id == 223:
        return 'font/f_mataro.png'
    if id == 224:
        return 'font/f_gava.png'
    if id == 225:
        return 'font/f_huelva.png'
    if id == 226:
        return 'font/f_tarragona.png'
    if id == 227:
        return 'font/f_getafefuenlabrada.png'
    if id == 228:
        return 'font/f_mallorca.png'
    if id == 229:
        return 'font/f_jaenii.png'
    if id == 230:
        return 'font/f_estepona.png'
    if id == 231:
        return 'font/f_murciaii.png'
    if id == 232:
        return 'font/f_coslada.png'
    if id == 233:
        return 'font/f_oviedo.png'
    if id == 234:
        return 'font/f_barakaldo.png'
    if id == 235:
        return 'font/f_burgos.png'
    if id == 236:
        return 'font/f_leon.png'
    if id == 237:
        return 'font/f_autosmadridmostoles.png'
    if id == 238:
        return 'font/f_alcorcon.png'
    if id == 239:
        return 'font/f_girona.png'
    if id == 240:
        return 'font/f_torrevieja.png'
    if id == 241:
        return 'font/f_elche.png'
    if id == 242:
        return 'font/f_villareal.png'
    if id == 243:
        return 'font/f_toledoii.png'
    if id == 244:
        return 'font/f_zafra.png'
    if id == 245:
        return 'font/f_irun.png'
    if id == 246:
        return 'font/f_lalinea.png'
    if id == 247:
        return 'font/f_badalonaii.png'
    if id == 248:
        return 'font/f_caceres.png'
    if id == 249:
        return 'font/f_marbella.png'
    if id == 250:
        return 'font/f_malagaiii.png'
    if id == 251:
        return 'font/f_ciudadreal.png'
    if id == 252:
        return 'font/f_villalba.png'
    if id == 253:
        return 'font/f_alcorconii.png'
    if id == 254:
        return 'font/f_tarragonaii.png'
    if id == 255:
        return 'font/f_sagunto.png'
    if id == 256:
        return 'font/f_pamplona.png'
    if id == 257:
        return 'font/f_arrigorriaga.png'
    if id == 258:
        return 'font/f_gandia.png'
    if id == 259:
        return 'font/f_sevillaiiii.png'
    if id == 260:
        return 'font/f_antequera.png'
    if id == 261:
        return 'font/f_vilagarcia.png'
    if id == 262:
        return 'font/f_cartagena.png'
    if id == 263:
        return 'font/f_roquetas.png'
    if id == 264:
        return 'font/f_gijon.png'
    if id == 265:
        return 'font/f_autosmadridleganes.png'
    if id == 266:
        return 'font/f_ourense.png'
    if id == 267:
        return 'font/f_vitoria.png'
    if id == 268:
        return 'font/f_pamplonaii.png'
    if id == 269:
        return 'font/f_santander.png'
    if id == 270:
        return 'font/f_manacor.png'



app = FastAPI()


@app.get("/items/{item_id}")
def hello(item_id: int, q: str):
    id_position = q[23:25]
    if int(id_position) < 8:
        id = path_font(item_id)
        img = insertar_letras(q, id)
        # guarda la imagen en la carpeta prueba
        img.save('resultados/' + q[15:25] + '_new.png')
    else:
        return 'interior'
    return img


if __name__ == '__main__':
    folder_of_folders = os.listdir('coches')
    id = 167
    for plate in tqdm(folder_of_folders):
        folder_path = 'coches/'+plate
        folder_info =  os.listdir(folder_path)
        id = id + 1
        if id > 270:
            id = 167
        for image in folder_info:
            image_path = os.path.join(folder_path, image)
            resp = requests.get('http://127.0.0.1:8000/items/'+str(id)+'?q='+image_path)
