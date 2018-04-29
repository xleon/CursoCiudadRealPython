# Curso de introducción a Python, Django y API REST (EOI 2018 Ciudad Real)

![logos](https://raw.githubusercontent.com/xleon/CursoLeonEoiPythonDjango/master/Assets/logos.png)

> Archivos y documentación del curso en https://github.com/xleon/CursoCiudadRealPython

# ¿Qué hemos aprendido?
- Conceptos básicos de python
  - Input: recoger entrada de datos en aplicaciones de consola
  - Asignación de variables
  - Manejo de strings
  - Operadores aritméticos
  - Operadores de asignación
  - Operadores condicionales
  - Listas
  - Tuplas
  - Diccionarios
  - Funciones y argumentos de función
  - Bucles
  - Imports
  - Fechas
  - Generación de números aleatorios y elementos aleatorios de una lista
  - Llamadas http
  - Imprimir con colores en la consola
  - Control de errores con try-except
- Introducción a la programación orientada a objetos en python
  - Clases e instancias de clase
  - Herencia y herencia múltiple
  - Encapsulación con métodos privados

- Cómo hacer un juego simple con una aplicación de consola, utilizando los conceptos aprendidos
- Comandos básicos de git (init, status, add, commit, push, pull, remote, etc) para crear un repositorio
- Utilización de GitHub para alojar nuestro respositorio
- Utilizar la herramienta PipEnv para gestionar entornos virtuales y paquetes de nuestros proyectos
- Instalación de proyectos django mediante línea de comandos
- Configuración y utilización de Visual Studio Code para python y proyectos django
- Configuración y utilización de PyCharm para python y proyectos django
- Depurar un programa python con Visual Studio Code
- Depurar un programa python con PyCharm
- Introducción a los settings de django
- Creación de modelos y relaciones entre modelos de django
- Aplicar migraciones de datos en django
- Utilizar y personalizar la herramienta admin de django
- Creación de vistas html mediante plantillas/templates de django
- Gestión de Urls en django
- Introducción a REST y RESTfull: conceptos básicos (GET, POST, PUT, DELETE)
- Instalación y configuración de django rest framework
- Creación de ViewSets y serializers con django rest framework
- Utilización de Postman para probar nuestra API REST

# Ejercicio final

Para poner en práctica los conceptos aprendidos hemos creado una aplicación cliente-servidor. Se trata de un mini juego de lucha donde tenemos torneos, luchadores y combates. Una vez elegido un torneo presente en la base de datos, se podrán crear combates entre los luchadores disponibles (elegidos aleatoriamente). Cada luchador tiene un número de vidas y un nivel de poder, que irá perdiendo en cada combate. La pérdida total de poder implica pérdida de una vida. Cuando solo quede un luchador con vida se dará el torneo por terminado.

El servidor proporciona una API rest con `django-rest-framework` y el cliente (aplicación de consola escrita con python) se comunica mediante llamadas http utilizando la librería `requests`, tanto para recibir listados de datos como para enviar objetos/modelos que se guardarán en la base de datos.

<div align="center">
  <img src="https://github.com/xleon/CursoCiudadRealPython/blob/master/Help/fight-game-client-server.gif?raw=true" 
  alt="fight game client and server"></a>
</div>


# Extras

### Enlaces de interés
- [Django project](https://www.djangoproject.com/)
- [Django REST framework](http://www.django-rest-framework.org/)
- [Descargas de python](https://www.python.org/downloads/)
- [Documentación pipenv](https://docs.pipenv.org/) 
- [Python](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [PyCharm IDE](https://www.jetbrains.com/pycharm/)
- [Git por línea de comandos](https://git-scm.com/download/win)
- [Github](https://github.com/)
- [Postman](https://www.getpostman.com/)
- [Librería Requests](http://docs.python-requests.org)
- [Introducción a REST (en español)](http://asiermarques.com/2013/conceptos-sobre-apis-rest/)

### Instalación y uso de python 3 y pipenv
Para trabajar en distintos proyectos de python/django es conveniente aislar entornos de python de manera que distintas versiones de paquetes o librerías no entren en conflicto. En este vídeo instalamos python 3 en Windows y además pipenv para gestionar entornos virtuales (virtualenv) de manera muy sencilla.
<div align="center">
  <a href="https://www.youtube.com/watch?v=zciRWEfZ-jc"><img src="https://img.youtube.com/vi/zciRWEfZ-jc/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>

### Crear y lanzar proyecto django con línea de comandos
<div align="center">
  <a href="https://www.youtube.com/watch?v=sTlFTcPBq9k"><img src="https://img.youtube.com/vi/sTlFTcPBq9k/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>

### Instalar y configurar Visual Stutio Code para python y django (windows y mac)
<div align="center">
  <a href="https://www.youtube.com/watch?v=EGYw4gPPp7w"><img src="https://img.youtube.com/vi/EGYw4gPPp7w/0.jpg" alt="IMAGE ALT TEXT"></a>
</div>