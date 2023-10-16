# Proyecto de Reconocimiento Facial y Detección de Emociones

Este proyecto utiliza tecnologías de vanguardia para realizar reconocimiento facial y detección de emociones en trabajadores. También integra Firebase para almacenar información sobre los trabajadores y sus emociones detectadas.

## Tecnologías Utilizadas

### OpenCV

[OpenCV](https://opencv.org/) (Open Source Computer Vision Library) es una biblioteca de código abierto que proporciona una amplia gama de herramientas para el procesamiento de imágenes y vídeo. En este proyecto, OpenCV se utiliza para cargar y manipular imágenes, así como para el reconocimiento facial.

### deepface

[deepface](https://github.com/serengil/deepface) es una biblioteca de Python que proporciona una serie de modelos de aprendizaje profundo pre-entrenados para el análisis de emociones en imágenes faciales. El modelo de emoción de deepface se utiliza para detectar y analizar las emociones en las imágenes de los trabajadores.

### face_recognition

La biblioteca [face_recognition](https://github.com/ageitgey/face_recognition) se basa en dlib y ofrece capacidades de reconocimiento facial de alto nivel. En este proyecto, se utiliza para reconocer y codificar los rostros de los trabajadores.

### Firebase

[Firebase](https://firebase.google.com/) es una plataforma de desarrollo de aplicaciones móviles y web de Google que proporciona una variedad de servicios en la nube. Se utiliza Firebase para almacenar información sobre los trabajadores y sus emociones detectadas, lo que permite un seguimiento y análisis eficaces.

## Inicialización de Modelos

El proyecto inicializa dos modelos clave:

1. **Modelo de Emoción:** Utiliza deepface para cargar un modelo de detección de emociones. Este modelo es capaz de analizar las emociones en una imagen facial y determinar la emoción dominante.

2. **Modelo de Reconocimiento Facial:** Emplea face_recognition para cargar un modelo que reconoce y codifica los rostros de los trabajadores conocidos.

## Proceso de Reconocimiento y Detección

El proceso se divide en las siguientes etapas:

1. **Reconocimiento Facial:** Las imágenes de los trabajadores se cargan en el proyecto. El modelo de reconocimiento facial se utiliza para codificar los rostros de los trabajadores conocidos.

2. **Detección de Emociones:** Cuando se captura una imagen de un trabajador, el proyecto utiliza el modelo de emoción de deepface para analizar las emociones en la imagen. Se calcula la emoción dominante y se almacena en Firebase.

3. **Almacenamiento en Firebase:** La información sobre la emoción detectada se almacena en Firebase, permitiendo un seguimiento a largo plazo de las emociones de los trabajadores.

## Uso

1. Ejecuta el proyecto en tu entorno de Python.
2. La aplicación utilizará la cámara web para capturar imágenes de los trabajadores.
3. Los rostros detectados se compararán con los trabajadores conocidos.
4. Las emociones en los rostros detectados se analizarán utilizando el modelo de emoción.
5. La información sobre la emoción dominante se almacenará en Firebase para su seguimiento.

## Contribución

¡Estamos abiertos a contribuciones! Si deseas mejorar o expandir este proyecto, no dudes en abrir un issue o enviar una solicitud de extracción.

## Contacto

Si tienes alguna pregunta o inquietud, no dudes en ponerte en contacto con nosotros. Puedes encontrarnos en [adrian2012011@gmail.com].
