<div align="center">
  <table width="1000px">
    <theader>
      <tr>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
        <th>
          <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
          <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
          <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
          <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
        </th>
        <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
      </tr>
    </theader>
    <tbody>
      <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
      <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
  </table>
</div>

<div align="center">
    <span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />
</div>

<div align="center">
  <table width="1000px">
    <theader>
      <tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
    </theader>
    <tbody>
      <tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 02</td></tr>
      <tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Django - Usando una plantilla para ver Destinos Turísticos</td></tr>
      <tr><td>NÚMERO DE PRÁCTICA:</td><td>06</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td width="60px">  III  </td></tr>
      <tr><td>FECHA DE PRESENTACIÓN:</td><td>03/07/2023</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3">23:59</td></tr>
      <tr>
        <td colspan="4">NOMBRE:
          <ul>
            <li>Melsy Melany Huamaní Vargas</li>
          </ul>
        </td>
        <td>NOTA:</td><td></td>
      </tr>
      <tr>
        <td colspan="6" width="1000px">DOCENTES:
          <ul>
            <li>Anibal Sardon Paniagua</li>
          </ul>
        </td>
      </tr>
    </tbody>
  </table>
</div>


##
## ACTIVIDADES


***Django Setup***

Se utiliza el sistema Windows para usar las herramientas necesarias para crear los proyectos.<br/><br/>

- Creando el ambiente para el proyecto
    ```sh
    C:\Users\melsy>mkvirtualenv test
    C:\Users\melsy\Envs is not a directory, creating
    created virtual environment CPython3.11.1.final.0-64 in 5832ms
    creator CPython3Windows(dest=C:\Users\melsy\Envs\test, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\melsy\AppData\Local\pypa\virtualenv)
        added seed packages: pip==23.1.2, setuptools==67.8.0, wheel==0.40.0
    activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
    ```
    <br/>

- Se instala Django
    ```sh
    (test) C:\Users\melsy>pip install django
    Collecting django
    Using cached Django-4.2.2-py3-none-any.whl (8.0 MB)
    Collecting asgiref<4,>=3.6.0 (from django)
    Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
    Collecting sqlparse>=0.3.1 (from django)
    Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
    Collecting tzdata (from django)
    Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
    Installing collected packages: tzdata, sqlparse, asgiref, django
    Successfully installed asgiref-3.7.2 django-4.2.2 sqlparse-0.4.4 tzdata-2023.3
    ```
    <br/>

- Se crea la carpeta de projects y se inicia el proyecto
    ```sh
    (test) C:\Users\melsy>mkdir projects
    (test) C:\Users\melsy>cd projects
    (test) C:\Users\melsy\projects>django-admin startproject destinosTuristicos
    (test) C:\Users\melsy\projects>cd destinosTuristicos
    ```
    <br/>

- Se corre el servidor para verificar
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    June 29, 2023 - 11:08:01
    Django version 4.2.2, using settings 'destinosTuristicos.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    <br/>

- Se ve en la página

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img1.png" style="width:70%"/><br/>

<br/>

***First app in Django***

- Se crea la aplicación de calculadora y se corre el servidor
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py startapp calc
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    June 29, 2023 - 11:30:45
    Django version 4.2.2, using settings 'destinosTuristicos.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    <br/>

- Se ve la página como antes

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img1.png" style="width:70%"/><br/>

- Se agrega en el archivo urls.py de destinosTuristicos
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('', include('calc.urls')),
        path('admin/', admin.site.urls),
    ]

- Se agrega en el archivo urls.py de calc las siguientes líneas
    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name="home")
    ]
    ```
    <br/>

- Se agrega en el archivo views.py de calc lo siguiente
    ```py
    from django.shortcuts import render
    from django.http import HttpResponse

    # Create your views here.

    def home(request):
        return HttpResponse("Hello World")
    ```
    <br/>

- Se ve en la página

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img2.png" style="width:70%"/><br/>

<br/>

***Django Template Language***

- Se crea el directorio templates y el archivo home.html
    ```html
    <h1>Hello World!!</h1>
    ```
    <br/>


- Se agrega las siguientes líneas en settings.py de destinosTuristicos
    ```py
    import os

    TEMPLATES = [
        {
            # (...)
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            # (...)
        },
    ]
    ```
    <br/>

- Se modifica el archivo views.py de calc
    ```py
    def home(request):
        return render(request, 'home.html')
    ```
    <br/>

- Se corre el servidor nuevamente
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    June 29, 2023 - 11:51:44
    Django version 4.2.2, using settings 'destinosTuristicos.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    <br/>

- Se ve en la página

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img3.png" style="width:70%"/><br/>

- Se modifica el archivo home.html de templates para probar el nombre
    ```html
    <h1>Hello {{name}}!!</h1>

    (views.py / calc) se agrega name
    def home(request):
        return render(request, 'home.html', {'name':'Melsy'})
    ```
    <br/>

- Se ve la página como antes

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img4.png" style="width:70%"/><br/>

- Se crea el archivo base.html en templates
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <title>Destinos Turísticos</title>
    </head>
    <body bgcolor="cyan">
        
        {% block content %}

        {% endblock %}

    </body>
    </html>
    ```
    <br/>

- Se agregan algunas líneas en home.html y se modifica de la siguiente forma
    ```html
    {% extends 'base.html' %}

    {% block content %}

    <h1>Hello {{name}}!!</h1>

    {% endblock %}
    ```
    <br/>

- Se ve en la página

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img5.png" style="width:70%"/><br/>

<br/>

***Addition of two Numbers in Django***

- Se agrega un formulario en home.html de templates
    ```html
    {% extends 'base.html' %}

    {% block content %}

    <h1>Hello {{name}}!!</h1>

    <form action="add">
        Ingrese 1er número: <input type="text" name="num1"><br>
        Ingrese 2do número: <input type="text" name="num2"><br>
        <input type="submit">
    </form>

    {% endblock %}
    ```
    <br/>


- Se crea el archivo result.html en templates
    ```html
    {% extends 'base.html' %}

    {% block content %}

    Result...

    {% endblock %}
    ```
    <br/>

- Se agrega una línea en urls.py de calc
    ```py
    urlpatterns = [
        path('', views.home, name="home"),
        path('add', views.add, name="add")
    ]
    ```
    <br/>

- Se agrega línea de la siguiente manera en views.py de calc
    ```py
    def add(request):
        return render(request, 'result.html')
    ```
    <br/>

- Se ponen los números

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img6.png" style="width:70%"/><br/>

- Se presiona enviar y obtenemos la página de result.html

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img7.png" style="width:70%"/><br/>

- Se modifica el archivo result.html de templates para mostrar un resultado
    ```py
    {% extends 'base.html' %} se agrega resultado

    {% block content %}

    Resultado: {{result}}

    {% endblock %}
    ```
    <br/>

- Se agrega lo siguiente en el archivo de views.py de calc
    ```py
    def add(request):

        val1 = request.GET['num1']
        val2 = request.GET['num2']
        res = val1 + val2

        return render(request, 'result.html', {'result':res})
    ```
    <br/>

- Se obtiene un resultado pero de strings

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img8.png" style="width:70%"/><br/>

- Se modifica archivo views.py de calc par sumar como enteros
    ```py
    def add(request):

        val1 = int(request.GET['num1'])
        val2 = int(request.GET['num2'])
        # ...
    ```
    <br/>

- Se muestra el resultado real

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img9.png" style="width:70%"/><br/>

<br/>

***Get vs Post HTTP methods***

- Se modifica el archivo result.html de templates para usar el POST
    ```html
    <form action="add" method="post">

        {% csrf_token %}

        Ingrese 1er número: <input type="text" name="num1"><br>
        Ingrese 2do número: <input type="text" name="num2"><br>
        <input type="submit">
    </form>
    ```
    <br/>

- Se modifica el archivo views.py de calc
    ```py
    def add(request):

        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])

        # ...
    ```
    <br/>

- Se ponen los números, se envía y no se nota en el url

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img10.png" style="width:70%"/><br/>

<br/>

***Model View Template y Static Files (Nueva Aplicación)***

- Se crea una nueva aplicación travello y se descarga una plantilla para el index.html
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py startapp travello
    ```
    <br/>


- Se crea el archivo urls.py de travello para incluir el index de la plantilla descargada
    ```py
    from django.urls import path
    from . import views

    urlpatterns = [path('', views.index, name="index")]
    ```
    <br/>

- Se agrega lo siguiente en el archivo de views.py de travello para incluir el index.html
    ```py
    from django.shortcuts import render

    # Create your views here.

    def index(request):
        return render(request, 'index.html')
    ```
    <br/>

- Se cambia el archivo de urls.py de destinosTuristicos para incluir las urls de travello
    ```py
    urlpatterns = [
        path('', include('travello.urls')),
        path('admin/', admin.site.urls),
    ]
    ```
    <br/>

- Se corre el servidor
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    June 29, 2023 - 14:32:24
    Django version 4.2.2, using settings 'destinosTuristicos.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    <br/>

- Se puede ver la pagina pero solamente el html

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img11.png" style="width:70%"/><br/>

- Se agregan las siguientes líneas en el archivo settings.py de destinosTuristicos para que reconozcxa la dirección de archivos estáticos, en donde se ha guardado todo lo que no se ha podido ver en la página anterior, es decir, imagenes, scripts, etc
    ```py
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
    ```
    <br/>

- Se realiza la colección de archivos static
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py collectstatic

    250 static files copied to 'C:\Users\melsy\projects\destinosTuristicos\assets'.
    ```
    <br/>

- Se corre el servidor y se pueden notar una gran cantidad de errores por los que no se ha podido ver adecuadamente la página de index.html
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    June 29, 2023 - 14:55:51
    Django version 4.2.2, using settings 'destinosTuristicos.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.

    [29/Jun/2023 14:56:00] "GET / HTTP/1.1" 200 69508
    
    (...)

    [29/Jun/2023 14:56:00] "GET /images/intro.png HTTP/1.1" 404 2298
    ```
    <br/>

- Debido que sale errores se modifica los plugins, estilos, imagenes y scripts con {% static ' ' %}
    ```html
    {% load static %}

    <!-- ... -->
    <head>
        <!-- ... -->
        <link rel="stylesheet" type="text/css" href="{% static 'styles/bootstrap4/bootstrap.min.css' %}">
        <link href="{% static 'plugins/font-awesome-4.7.0/css/font-awesome.min.css' %}" rel="stylesheet" type="text/css">
        <link rel="stylesheet" type="text/css" href="{% static 'plugins/OwlCarousel2-2.2.1/owl.carousel.css' %}">
        <link rel="stylesheet" type="text/css" href="{% static 'plugins/OwlCarousel2-2.2.1/owl.theme.default.css' %}">
        <link rel="stylesheet" type="text/css" href="{% static 'plugins/OwlCarousel2-2.2.1/animate.css' %}">
        <link rel="stylesheet" type="text/css" href="{% static 'styles/main_styles.css' %}">
        <link rel="stylesheet" type="text/css" href="{% static 'styles/responsive.css' %}">
    </head>
    <body>

        <!-- ... -->
        <script src="{% static 'js/jquery-3.2.1.min.js' %}"></script>
        <script src="{% static 'styles/bootstrap4/popper.js' %}"></script>
        <script src="{% static 'styles/bootstrap4/bootstrap.min.js' %}"></script>
        <script src="{% static 'plugins/OwlCarousel2-2.2.1/owl.carousel.js' %}"></script>
        <script src="{% static 'plugins/Isotope/isotope.pkgd.min.js' %}"></script>
        <script src="{% static 'plugins/scrollTo/jquery.scrollTo.min.js' %}"></script>
        <script src="{% static 'plugins/easing/easing.js' %}"></script>
        <script src="{% static 'plugins/parallax-js-master/parallax.min.js' %}"></script>
        <script src="{% static 'js/custom.js' %}"></script>
    </body>
    ```
    <br/>

- Se actualiza y al haber modificado todo lo anterior entonces se puede ver la página correcta

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img12.png" style="width:70%"/><br/>

<br/>

***Passing Dynamic Data in HTML***

- Se agrega lo siguiente en el archivo models.py de travello para crear una clase Destination que sirve para crear nuevos destinos
    ```py
    from django.db import models

    class Destination:
        id: int
        name: str
        img: str
        desc: str
        price: int
    ```
    <br/>


- Se modifica el archivo views.py de travello para crear un primer destino con nuevos datos
    ```py
    def index(request):

        dest1 = Destination()
        dest1.name = "Mumbai"
        dest1.desc = "The city that never sleeps"
        dest1.price = 700

        return render(request, 'index.html', {'dest1': dest1})
    ```
    <br/>

- Se modifica el archivo index.html de templates para mostrar los datos nuevos del primer destino con lo que se ha creado anteriormente
    ```html
    <div class="destination item">
        <div class="destination_image">
            <img src="{% static 'images/destination_1.jpg' %}" alt="">
            <div class="spec_offer text-center"><a href="#">Special Offer</a></div>
        </div>
        <div class="destination_content">
            <div class="destination_title"><a href="destinations.html">{{dest1.name}}</a></div>
            <div class="destination_subtitle"><p>{{dest1.desc}}</p></div>
            <div class="destination_price">From ${{dest1.price}}</div>
        </div>
    </div>
    ```
    <br/>

- Se actualiza y se puede ver lo siguiente en la página

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img13.png" style="width:70%"/><br/>

- Se añaden las siguientes líneas en el archivo views.py de travello para agregar nuevos destinos
    ```py
    def index(request):

        dest1 = Destination()
        dest1.name = "Arequipa"
        dest1.desc = "La ciudad blanca"
        dest1.img = "destination_1.jpg"
        dest1.price = 50

        dest2 = Destination()
        dest2.name = "Tacna"
        dest2.desc = "La ciudad heroica"
        dest2.img = "destination_2.jpg"
        dest2.price = 70

        dest3 = Destination()
        dest3.name = "Piura"
        dest3.desc = "Hermosas playas"
        dest3.img = "destination_3.jpg"
        dest3.price = 90

        dests = [dest1, dest2, dest3]

        return render(request, 'index.html', {'dests': dests})
    ```
    <br/>

- Se modifica el archivo index.html de templates para agregar el for
    ```html
    {% for dest in dests %}
    <!-- Destination -->
    <div class="destination item">
        <div class="destination_image">
            <img src="{% static 'images/destination_1.jpg' %}" alt="">
            <div class="spec_offer text-center"><a href="#">Special Offer</a></div>
        </div>
        <div class="destination_content">
            <div class="destination_title"><a href="destinations.html">{{dest.name}}</a></div>
            <div class="destination_subtitle"><p>{{dest.desc}}</p></div>
            <div class="destination_price">From ${{dest.price}}</div>
        </div>
    </div>
    {% endfor %}
    ```
    <br/>

- Se actualiza y salen las tres nuevas ciudades con el for pero imagenes iguales

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img14.png" style="width:70%"/><br/>

- Se modifica el archivo index.html de templates para que reconozca la imagen en el lugar estático de images
    ```html
    {% static "images" as baseUrl %}

    {% for dest in dests %}
    <!-- Destination -->
    <div class="destination item">
        <div class="destination_image">
            <img src="{{baseUrl}}/{{dest.img}}" alt="">
            <div class="spec_offer text-center"><a href="#">Special Offer</a></div>
        </div>
        <!-- ... -->
    </div>
    {% endfor %}
    ```
    <br/>

- Se actualiza y se ve las tres ciudades con imagen diferente

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img15.png" style="width:70%"/><br/>

<br/>

***If statement in Django***

- Se crea el nuevo atributo de offer para oferta en el archivo models.py de travello
    ```py
    class Destination:
        # (...)
        offer: bool
    ```
    <br/>


- Se modifica el archivo views.py de travello para mostrar que están en oferta o no
    ```py
    def index(request):

        dest1 = Destination()
        # ...
        dest1.offer = False

        dest2 = Destination()
        # ...
        dest2.offer = True

        dest3 = Destination()
        # ...
        dest3.offer = False
    ```
    <br/>

- .
    ```html
    {% if dest.offer %}
        <div class="spec_offer text-center"><a href="#">Special Offer</a></div>
    {% endif %}
    ```
    <br/>

- Actualizamos y se puede ver la imagen con las ciudades y con la respectiva oferta

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img16.png" style="width:70%"/><br/>

<br/>

***Postgres and PgAdmin Setup***

- Instalamos Postgres y Pgadmin

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img17.png" style="width:20%"/><br/>

- Se puede ver la interfaz de usuario con Pgadmin para ver las bases de datos que se crean con Postgres

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img18.png" style="width:70%"/><br/>

<br/>

***Models and migrations***

- Se crea la base de datos con Pgadmin

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img19.png" style="width:40%"/><br/>

- Se pone el nombre a la base de datos

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img20.png" style="width:70%"/><br/>

- Se puede ver ya creada

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img21.png" style="width:70%"/><br/>

- Para crear una enlace con la base de datos se modifica con las siguientes líneas el archivo settings.py de destinosTuristicos
    ```py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'destinosTuristicos',
            'USER': 'postgres',
            'PASSWORD': '1234',
            'HOST': 'localhost'
        }
    }
    ```
    <br/>


- Se instala psycopg2 para que exista conexión con la base de datos proximamente
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>pip install psycopg2
    Collecting psycopg2
      Downloading psycopg2-2.9.6-cp311-cp311-win_amd64.whl (1.2 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 8.2 MB/s eta 0:00:00
    Installing collected packages: psycopg2
    Successfully installed psycopg2-2.9.6
    ```
    <br/>

- Creando modelo Destination para la base de datos
    ```py
    class Destination(models.Model):
        name = models.CharField(max_length=100)
        img = models.ImageField(upload_to='pics')
        desc = models.TextField()
        price = models.IntegerField()
        offer = models.BooleanField(default=False)
    ```
    <br/>

- En el archivo settings.py de destinosTuristicos se agregan las siguientes lineas
    ```py
    INSTALLED_APPS = [
        'travello.apps.TravelloConfig',
        # ...
    ]
    ```
    <br/>

- Se instala Pillow para habilitar el uso de imagenes en el modelo creado
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>pip install Pillow
    Collecting Pillow
      Downloading Pillow-10.0.0-cp311-cp311-win_amd64.whl (2.5 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 11.4 MB/s eta 0:00:00
    Installing collected packages: Pillow
    Successfully installed Pillow-10.0.0
    ```
    <br/>

- Se crean las migraciones para crear el modelo Destination
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py makemigrations
    Migrations for 'travello':
      travello\migrations\0001_initial.py
        - Create model Destination
    ```
    <br/>

- Se conecta con la base de datos que ha sido creada anteriormente
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py sqlmigrate travello 0001
    BEGIN;
    --
    -- Create model Destination
    --
    CREATE TABLE "travello_destination" ("id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, "name" varchar(100) NOT NULL, "img" varchar(100) NOT NULL, "desc" text NOT NULL, "price" integer NOT NULL, "offer" boolean NOT NULL);
    COMMIT;
    ```
    <br/>

- Se realiza la migración del modelo creado
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py migrate
    Operations to perform:
        Apply all migrations: admin, auth, contenttypes, sessions, travello
    Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying admin.0002_logentry_remove_auto_add... OK
        Applying admin.0003_logentry_add_action_flag_choices... OK
        Applying contenttypes.0002_remove_content_type_name... OK
        Applying auth.0002_alter_permission_name_max_length... OK
        Applying auth.0003_alter_user_email_max_length... OK
        Applying auth.0004_alter_user_username_opts... OK
        Applying auth.0005_alter_user_last_login_null... OK
        Applying auth.0006_require_contenttypes_0002... OK
        Applying auth.0007_alter_validators_add_error_messages... OK
        Applying auth.0008_alter_user_username_max_length... OK
        Applying auth.0009_alter_user_last_name_max_length... OK
        Applying auth.0010_alter_group_name_max_length... OK
        Applying auth.0011_update_proxy_permissions... OK
        Applying auth.0012_alter_user_first_name_max_length... OK
        Applying sessions.0001_initial... OK
        Applying travello.0001_initial... OK
    ```
    <br/>

- Se puede ver la tabla pero vacía porque todavía no se han añadido destinos

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img22.png" style="width:70%"/><br/>

<br/>

***Admin Panel***

- Se crea el superusuario con los datos necesarios
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py createsuperuser
    Username (leave blank to use 'melsy'): mhuamanivar
    Email address: mhuamanivar@unsa.edu.pe
    Password:
    Password (again):
    This password is too common.
    This password is entirely numeric.
    Bypass password validation and create user anyway? [y/N]: y
    Superuser created successfully.
    ```
    <br/>


- Se corre el servidor
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py runserver
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).
    July 03, 2023 - 17:33:48
    Django version 4.2.2, using settings 'destinosTuristicos.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
    ```
    <br/>

- Se ingresa el nombre del superusuario y contraseña

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img23.png" style="width:70%"/><br/>

- Se ve lo que existe actualmente en la página de admin

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img24.png" style="width:70%"/><br/>

- Se añaden las siguiente líneas en el archivo admin.py de travello para agregar modelo Destination en la pagina de admin
    ```py
    from django.contrib import admin
    from .models import Destination

    # Register your models here.

    admin.site.register(Destination)
    ```
    <br/>

- Se puede ver el modelo en la página de admin

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img25.png" style="width:70%"/><br/>

<br/>

***Add and fetch data from database***

- Creando carpeta de media para guardar las imagenes
    ```py
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```
    <br/>


- Se agregan las siguientes líneas para la media en el archivo urls.py de destinosTuristicos
    ```py
    from django.conf import settings
    from django.conf.urls.static import static

    # ...

    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
    <br/>

- Actualizamos y damos en "add" en Destinations para agregar los destinos

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img26.png" style="width:70%"/><br/>

- Despues añadimos todos los destinos

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img27.png" style="width:70%"/><br/>

- Vemos en base de datos

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img28.png" style="width:70%"/><br/>

- Para que los nuevos datos se vean en la pagina se actualiza el views.py de travello
    ```py
    from django.shortcuts import render
    from .models import Destination

    def index(request):

        dests = Destination.objects.all()
        return render(request, 'index.html', {'dests': dests})
    ```
    <br/>


- Solo se modifica lo de imagen y su tamaño en el archivo index.html de templates
    ```html
    {% for dest in dests %}
    <!-- Destination -->
    <div class="destination item">
        <div class="destination_image">
            <img src="{{dest.img.url}}" alt="" height=200px width=100%>
                                    
            <!-- ... -->

        </div>

        <!-- ... -->
                        
    </div>
    {% endfor %}
    ```
    <br/>

- Se actualiza y se ve la imagen en página principal con los destinos creados

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img29.png" style="width:70%"/><br/>

<br/>

***User registration in Django***

- Se crea la nueva aplicación accounts
    ```sh
    (test) C:\Users\melsy\projects\destinosTuristicos>python manage.py startapp accounts
    ```
    <br/>

- Se crea el archivo urls.py en accounts para que se llame a una nueva página llamada resgister
    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('register', views.register, name="register")
    ]
    ```
    <br/>

- Se modifica el archivo urls.py de destinosTuristicos para que reconoza las urls de accounts
    ```py
    urlpatterns = [
        # ...
        path('accounts/', include('accounts.urls'))
    ]
    ```
    <br/>

- Se modifica views.py de accounts para que muestra la página de register.html
    ```py
    from django.shortcuts import render

    def register(request):
        return render(request, 'register.html')
    ```
    <br/>

- Se modifica el index.html de templates para que exista una opción que nos redirija a la página de registrarse
    ```html
    <nav class="main_nav">
        <ul class="d-flex flex-row align-items-start justify-content-start">
            <li class="active"><a href="index.html">Home</a></li>
            <li><a href="contact.html">Contacto</a></li>
            <li><a href="accounts/register">Registrarse</a></li>
        </ul>
    </nav>
    ```
    <br/>

- Para crear la pagina de registro necesitamos la base de datos de los usuarios que esta creado por django

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img30.png" style="width:70%"/><br/>

- Se crea el archivo register.html en templates y se escribe lo siguiente
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Registrarse</title>
    </head>
    <body>
        
        <form action="register" method="post">
            {% csrf_token %}

            <input type="text" name="first_name" placeholder="First Name"><br>
            <input type="text" name="last_name" placeholder="Last Name"><br>
            <input type="text" name="username" placeholder="Username"><br>
            <input type="email" name="email" placeholder="Email"><br>
            <input type="password" name="password1" placeholder="Password"><br>
            <input type="password" name="password2" placeholder="Confirm password"><br>
            <input type="Submit">

        </form>

    </body>
    </html>
    ```
    <br/>

- Se va a la página principal

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img31.png" style="width:70%"/><br/>

- Se hace click en registrarse

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img32.png" style="width:60%"/><br/>

- Se cambia todo el archivo de views.py de accounts para crear el usuario
    ```py
    from django.shortcuts import render, redirect
    from django.contrib.auth.models import User, auth

    # Create your views here.

    def register(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print('User created')
            return redirect('/')
        
        else:
            return render(request, 'register.html')
    ```
    <br/>

- Actualizamos, ponemos datos con contraseña 1234

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img33.png" style="width:60%"/><br/>

- Vemos la base de datos

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img34.png" style="width:70%"/><br/>

- Se modifica la estructura para las verificacion de email, username y contraseña, además se cambia a español
    ```py
    from django.shortcuts import render, redirect
    from django.contrib.auth.models import User, auth

    # Create your views here.

    def register(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1==password2:
                if User.objects.filter(username=username).exists:
                    print('El nombre de usuario ya existe')
                elif User.objects.filter(email=email).exists:
                    print('Ya existe un usuario con este email')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    print('Usuario creado')

            else:
                print('La contraseña no coincide')
            
            return redirect('/')
        
        else:
            return render(request, 'register.html')
    ```
    <br/>

- Cambiando el archivo register.html de templates a español
    ```html
    <form action="register" method="post">
        {% csrf_token %}

        <input type="text" name="first_name" placeholder="Nombres"><br>
        <input type="text" name="last_name" placeholder="Apellidos"><br>
        <input type="text" name="username" placeholder="Nombre de usuario"><br>
        <input type="email" name="email" placeholder="Email"><br>
        <input type="password" name="password1" placeholder="Contraseña"><br>
        <input type="password" name="password2" placeholder="Confirmar contraseña"><br>
        <input type="Submit">

    </form>
    ```
    <br/>

<br/>

***Passing messages in Django***

- Se modifica el archivo views.py de accounts para mostrar los mensajes con las opciones que nos da Django, por lo que también se importa messages
    ```py
    def register(request):
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1==password2:
                if User.objects.filter(username=username).exists:
                    messages.info(request, 'El nombre de usuario ya existe')
                    return redirect('register')
                elif User.objects.filter(email=email).exists:
                    messages.info(request, 'Ya existe un usuario con este email')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    print('Usuario creado')

            else:
                messages.info(request, 'La contraseña no coincide')
            
            return redirect('/')
        
        else:
            return render(request, 'register.html')
    ```
    <br/>

- Se cambia los messages del archivo register.html de templates
    ```html
    <div>
        {% for message in messages %}
        <h3> {{message}} </h3>
        {% endfor %}
    </div>
    ```
    <br/>

- Se ve la imagen de la página si las contraseñas introducidas anteriormente no coincide 

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img35.png" style="width:60%"/><br/>

- Se ve la imagen de la página si es que el nombre de ususario introducido ya se encuentra en la base de datos

    <img src="https://raw.githubusercontent.com/mhuamanivar/PW2-HuamaniV-Lab06/main/imagenes/img36.png" style="width:60%"/><br/>