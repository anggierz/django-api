# Django API
Desarrollo de una API Completa con Django

Utilizaremos el código desarrollado en la práctica del tema 2 (https://github.com/anggierz/spotify_api), para generar una API las mismas funcionalidades, esta vez utilizando Django.

## Descripción del proyecto

Este repositorio incluye la actividad 3: Desarrollo de una API Completa con Django del Módulo 2. Fundamentos de Backend con Python del Máster de Desarrollo Web de la UEM.

Se implementa una API RESTful haciendo uso del framework **Django** para gestionar usuarios. Adicionalmente,
se integra con la **API de Spotify** para obtener información musical.

## Funcionalidades

1. **Gestión de Usuarios**:
   - Crear, leer, actualizar y eliminar usuarios.
   - Los usuarios tienen los siguientes atributos definidos en el modelo de datos: nombre, apellido, correo electrónico, edad, país y géneros musicales favoritos.

2. **Integración con la API de Spotify**:
   - Buscar información de artistas, canciones y álbumes.
   - Obtener los "top tracks" de un artista.


## Endpoints disponibles

### **1. Gestión de Usuarios (USER ENDPOINTS)**

#### **GET /api/users**

#### **GET /api/users/{id}**

#### **POST /api/users/create/**

#### **PATCH /api/users/update/{id}**

#### **DELETE /api/users/delete/{id}**


### **2. Integración con Spotify (SPOTIFY ENDPOINTS)**

#### **GET /api/spotify/artist-top-tracks/{artist}**

#### **GET /api/spotify/search/{item}/{type}**

## Instrucciones de uso

### 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto a tu máquina local

### 2. Instalar dependencias 

Instala las dependencias que se encuentran en el archivo requirements.txt

```bash
pip install -r requirements.txt
```

### 3. Configura las variables del archivo .env

Para hacer llamadas al endpoint de Spotify, se necesita **client_id** y **client_secret**. El código del proyecto
está configurado de manera que carga las variables del archivo .env. Crea tu archivo .env a partir del archivo
**.env.example** que proporciono en el proyecto. 

### 4. Levantar los endpoints

Finalmente, levanta las rutas para poder utilizarlas

```bash
python manage.py runserver
```