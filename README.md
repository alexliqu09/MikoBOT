<h2 align="center">
<p>  MikoBOT </p>
</h2>
<h2 align="center">
</h2>

## Resumen 
* Para nuestra primera versión del trabajo se buscó aprender un poco del estado del arte de los chatbots para ello nos basamos  en el tutorial de [Python Engineer](https://www.youtube.com/watch?v=RpWeNzfSUHw) y una vez entrenado intentamos desplegar el bot en la plataforma de discord siguiendo el tutorial de [Cursos y asesorías de programación](https://www.youtube.com/watch?v=iZcDF3FGOcA&t=1001s).

<p align="center">
<img src="src\Pipeline.png"  width="600"/>
</p align="center">

## 🆕 Actualización
 
 - 19/05/2021 :

 - La primera versión esta sus últimas fases.

 ## 📖 Contentenido
El contenido de la aplicación.

```
|-src/...
|-chat.py
|- discord_chatbot.py
|- intens.json
|- requeriments.txt
|- model.py
|- utils.py
|- train.py
```
# Instalación

1. Clona este repositorio:
```
https://github.com/alexliqu09/MikoBOT.git
```
2. Instalaremos el entorno
```
conda create env
```
3. Instalaremos las dependencias con el comando
```
pip install -r requirements.txt.
```

# Entrenamiento 

Si desea entrenar el modelo usted solo debe ejecutar este comando
```
 python train.py
```
## Nota
- Una vez entrenado el modelo se guardara los pesos en un archivo .pth
- Si desea implementar sus propios dialogos, es libre de modficiar el [intents.json](https://github.com/alexliqu09/MikoBOT/blob/main/intents.json)
- Si desea implementar su bot en discord le recomiendo ver este [tutorial](https://www.youtube.com/watch?v=iZcDF3FGOcA&t=1001s).
## Algunas imagenes de la implementación
<p align="center">
<img src="src\Imagen_1.jpg"  width="400"/>
</p align="center">
<p align="center">
<img src="src\Imagen_2.jpg"  width="400"/>
</p align="center">

## 👨🏽‍💻 Autores

* Alexander Leonardo Lique Lamas, Github: [alexliqu09](https://github.com/alexliqu09) Email: alexander.lique.l@uni.pe

* Diego Vázques Levano Github: [Diego-Vasquez](https://github.com/Diego-Vasquez), Email: diego.vasquez.l@uni.pe  


## 🙏🏽 Agredecimientos Especiales:

- Agredecimientos al canal de [Python Enginieer](https://www.youtube.com/channel/UCbXgNpp0jedKWcQiULLbDTA) sin sus tutoriales este repositorio no estaria finalizado.

- Agradecimeinto al canal de [Cursos y asesorías de programación](https://www.youtube.com/channel/UCwJWMXB5iJNmbhSmX3soIhQ) sin sus tutoriales este repositorio no estaria finalizado.

- Agradecimientos al [repositorio](https://github.com/HiroForYou/PyTorch-Chatbot) de [HiroForYou](https://github.com/HiroForYou) sin este repositorio este trabajo no seguria adelante.