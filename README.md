# service

Service es un programa que permite a dos usuarios comunicarse de manera sencilla a través de un servidor.

# Estructura del Proyecto

`Es dividido el proyecto en diferentes modulos:`

main.py: Este módulo actúa como el punto de entrada del programa. Recoge los detalles del usuario y lanza el cliente o el servidor según sea necesario, proporcionando una interfaz de usuario fluida y eficiente.

constants.py: Este módulo define una serie de constantes y funciones auxiliares que se utilizan a lo largo del proyecto para mantener la coherencia y la eficiencia.

client.py: Este módulo implementa la funcionalidad del cliente, estableciendo una conexión con el servidor y gestionando el envío y recepción de mensajes.

Service.py: Este módulo es responsable de la lógica de procesamiento de mensajes, asegurando que los mensajes se manejen de manera eficiente y efectiva.

server.py: Este módulo implementa la funcionalidad del servidor, aceptando conexiones de los clientes y facilitando la comunicación entre ellos mediante la retransmisión de mensajes

# Cómo usar

Para usar service, sigue estos pasos:

1. Ejecuta `main.py`.
2. Luego, se te presentará un menú con varias opciones. Puedes elegir crear una sala de chat, unirte a una sala de chat existente, cambiar tu idioma o salir del programa.
3.  
    Si seleccionas `crear una sala`, se abrirá una nueva pestaña del cmd con el servidor iniciado y se te pedirá en la pestaña donde estas que ingreses tu nombre para unirte al servidor.
    Si seleccionas `unirte a una sala existente`, se te pedira ingresar el nombre.
    Si seleccionas `salir` se te dara un mensaje de despedida y se cerrará el programa.