# Instalación de Miniconda en Windows :computer:
Aquí se presentan los pasos para la instalación de Miniconda 3 en un sistema operativo Windows.
1. Descargar e instalar Miniconda 3 del siguiente link [Miniconda](https://conda.io/miniconda.html) (una alternativa para evitar los siguientes pasos es instalar [Anaconda](https://www.anaconda.com/distribution/) (Python 3.6), sin embargo, se ha visto que algunos equipos tiene problemas para compilar y abrir :confused:)
 * Se recomienda que en la instalación no se instale de manera global, es decir, instalarlo solo para el usuario. Adicionalmente, NO seleccione la opción de usar el ambiente PATH (no añadir a PATH).
2. Posteriormente a la instalación encontrará en todos sus programas uno llamado Anaconda Prompt, abralo.
3. Escriba el siguiente comando (verá la versión de conda que se ha instalado en su equipo junto con otros datos)
```
$ conda info
```
4. Crear un ambiente en conda: (este ambiente es específico para el MCRA-2018)
```
$ conda create --name MCRA2018 python=3.6 numpy scipy matplotlib h5py pandas ipython jupyter cython seaborn networkx orange3
```
5. Activar el ambiente creado
```
$ activate MCRA2018
```
6. Una vez abierto el ambiente probar abrir jupyter notebook
```
(MCRA2018) $ jupyter notebook
```
7. Para cerrar el notebook de jupyter, cierre primero el explorador y posteriormente en el Anaconda Prompt teclee ctrl + c.
8. Para desactivar el ambiente creado escriba la orden:
```
$ deactivate
```
y con esto estará listo para el taller MCRA-2018 :wink:.
