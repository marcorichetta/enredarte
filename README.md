# Flexbox (Originalidad = 1000%)

<p align="center">
<img src="https://i.imgur.com/meQwwYf.png" width="300">

![](https://img.shields.io/badge/Python-3.9-blue)
![](https://img.shields.io/badge/Django-2.2.13-blue)

<img src="https://i.imgur.com/R22nKrg.png" width="800">
</p>


Este sistema fue realizado como parte de mi proyecto final para la carrera de Analista de Sistemas.

> El objetivo de Flexbox es el de integrar todos los procesos de la empresa, desde la consulta de un cliente hasta la entrega del producto terminado, automatizando tareas, brindando acceso rápido a información importante como
estadísticas e informes automatizados, y beneficiando la toma de decisiones de la empresa.

Está lejos de ser productivo pero sin dudas me sirvió para poner en práctica conocimientos de:

- Python/Django
- Diseño de bases de datos
- Docker
- Testing
- CI

# Setup

```bash
git clone https://github.com/marcorichetta/enredarte.git

cd enredarte
```
## Docker way
```bash
docker-compose up
```

Dentro del archivo `Makefile` hay algunos shortcuts útiles.

Por ejemplo, `make bash` abre un shell bash dentro del contenedor.

## Sin Docker

>:warn: Hace mucho empecé a utilizar Docker por lo que esta información puede estar desactualizada. (Issues bienvenidos 🙌)
### 0. Instalar PostgreSQL => [Manjaro](https://gist.github.com/marcorichetta/af0201a74f8185626c0223836cd79cfa)


## 1. Crear virtual env e instalar dependencias
```bash
cd enredarte

python3 -m venv env # Crear virtualenv con nombre 'env'

source env/bin/activate

pip install -r requirements.txt
```
## 2. Aplicamos las migraciones

```bash
python manage.py migrate
```
## 3. Crear datos de prueba

```bash
./manage.py crear_roles_y_permisos
./manage.py crear_usuarios
./manage.py crear_provincias
./manage.py crear_clientes
./manage.py crear_variables
./manage.py crear_proveedores
./manage.py crear_insumos
```

## 4. Creamos superusuario

```bash
python manage.py createsuperuser
```

## 5. Configurar ENV variables

En la carpeta `/enredarte` renombrar el archivo `.env.template` a `.env`

## 6. Correr proyecto

`python manage.py runserver`
