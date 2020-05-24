# Setup de este repo

## Para el setup de PostgreSQL ver [acá](https://gist.github.com/marcorichetta/af0201a74f8185626c0223836cd79cfa)

```bash
git clone https://github.com/marcorichetta/enredarte.git

cd enredarte

python3 -m venv env # Crear virtualenv con nombre 'env'

source env/bin/activate[.fish] # Dependerá de la terminal que este utilizando
```

## 1. Instalar dependencias

`pip install -r requirements.txt`

## 2. Aplicamos las migraciones

`python manage.py migrate`

## 3. Crear datos de prueba

```bash
./manage.py crear_provincias
./manage.py crear_clientes
./manage.py crear_variables
./manage.py crear_proveedores
./manage.py crear_insumos
```

## 4. Creamos superusuario

`python manage.py createsuperuser`

## 5. Crear archivo **.env** en carpeta _/enredarte_ con las variables

**DBUSER** = 'usuario'

**DBPASSWORD** = 'password'

## 6. Correr proyecto

`python manage.py runserver`
