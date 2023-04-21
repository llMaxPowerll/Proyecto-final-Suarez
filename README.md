#Tercera-pre-entrega-Suarez

En el inicio se pueden buscar las editoriales cargadas en la base de datos, van a figurar todos los libros de esa editorial

podemos acceder a Autores, Libros y Bibliotecas. Donde cada una muestra que posee en la base de datos y cuenta con el formulario para agregar lo correspondiente.

los pasos a seguir son: 

clonar el repositorio, correr el entorno virtual y correr el servidor local

los comandos a seguir en terminal serian:

- git clone https://github.com/llMaxPowerll/Tercera-pre-entrega-Suarez.git

- cd Tercera

- pip install virtualenv

- virtualenv venv

- venv\scripts\activate

- pip install -r requirements.txt

- python manage.py migrate

- python manage.py runserver