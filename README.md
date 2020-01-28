# ClickTracker GUI

### Uso
Correr el script `python3 main.py`
Apareceran cuadrados de forma random en la pantalla. Al darle click el puntaje aumenta en uno. Al terminar las iteraciones del programa, arroja por consola el puntaje si se hizo click dentro del cuadrado.

### Configuraciones en código
```
rectangle_max_iter  = 5   # Iteraciones, cuantos cuadrados aparecen 
max_timer_click     = 2   # Tiempo para presionar un cuadrado en segundos
rectangle_width     = 200 # Ancho del cuadrado
click_error         = 0   # Error del click
```
El error es similar a generar un cuadrado de mayor area imaginario. Quiere decir si el cuadrado normal es de 200x200 al tener un error de 100 permite que el click sea válido presionando en un cuadrado de 300x300.

### Prerequisitos 
Hay que tener los siguientes paquetes instalados.
- `pip3`
- `tkinter` para la interfaz gráfica, viene en python 3 ahora.
- `pip3 install pynput` 
- `pip3 intsall keyboard`