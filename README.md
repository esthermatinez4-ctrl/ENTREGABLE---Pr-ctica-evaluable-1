# Simulación de difusión de calor en una placa 2D

Este proyecto simula cómo se propaga el calor en una placa metálica utilizando el método de diferencias finitas. Incluye una animación de la evolución térmica y una comparación entre materiales con distinta conductividad.

## Requisitos

Instala Python 3.8 o superior y las librerías necesarias:

pip install numpy matplotlib

## Cómo ejecutarlo

1. Clona el repositorio:

git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo

2. Ejecuta el programa principal:

python simulacion_calor.py

Esto mostrará:
- La animación de la difusión del calor.
- Una comparación visual entre dos materiales (aluminio y hierro).

## Descripción rápida del proyecto

- La placa es de 50×50 celdas.
- El borde superior se fija a 100 °C.
- El resto comienza a 0 °C.
- El calor se propaga iterativamente hasta alcanzar el equilibrio.
- Se pueden comparar materiales cambiando el parámetro `alpha`.

## Archivos principales

- simulacion_calor.py → Código completo de la simulación.
- README.md → Este archivo.
