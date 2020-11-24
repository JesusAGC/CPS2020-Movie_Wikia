# CPS2020-Movie_Wikia

Repositorio del proyecto para ordinario de la materia Calidad y Pruebas de Software 2020 de la Facultad de Sistemas, UAdeC.

## Miembros del equipo:
- Jesús Antonio González Cárdenas - [@JesusAGC](https://github.com/JesusAGC)
- Erick Orlando Escárcega Ramírez - [@ERORESRA](https://github.com/ERORESRA)
- Fernando FLores Fernandez - [@Rephyroth](https://github.com/Rephyroth)

## Pasos para ejecutar el software:
1. En el archivo config.json añade tu llave de api en el valor "api_key" (Si no tienes una, sigue estos pasos: https://developers.themoviedb.org/3/getting-started/introduction)
2. Crea una base de datos en sqlite y corre los scripts para crear las tablas. Al terminar esto, añade la ruta de la base de datos al archivo config.json dentro del valor "database_route"
3. Corre el archivo main.py para ejecutar el software.