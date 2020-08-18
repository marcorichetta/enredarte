## Debugging con Docker y VSCode (Source)[https://emilyemorehouse.com/017-debug-django-with-docker-vs-code/]

Para hacer debug con Docker:

1. Configurar una variable de entorno `VSCODE_DEBUGGER=True` en `docker-compose.yml`.

2. Reconstruir y ejecutar los contenedores: `docker-compose up --build`

3. Comenzar una sesión de debugging desde VS Code:

   1. `Ctrl+Shift+D` para abrir el menú de Debugging.

   2. Elegir `[django:docker] runserver` del select al lado del botón Play.

   3. Click en el botón Play o `F5` para comenzar la sesión de debugging.

      - Los logs se redireccionan a la terminal integrada de Debug de VS Code.

4. Ahora se pueden colocar breakpoints en el código:

   - Haciendo click en el circulo rojo al lado del número de línea establecemos un breakpoint. 
   - Cuando ese código es ejecutado, el debugger pausa la ejecución y se puede inespeccionar el call stack
   y las variables del código.