import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import animation
from matplotlib.widgets import Button

def vecindario(b):
    vecindario = (
        np.roll(np.roll(b, 1, 1), 1, 0) + 
        np.roll(b, 1, 0) + 
        np.roll(np.roll(b, -1, 1), 1, 0) + 
        np.roll(b, -1, 1) + 
        np.roll(np.roll(b, -1, 1), -1, 0) + 
        np.roll(b, -1, 0) + 
        np.roll(np.roll(b, 1, 1), -1, 0) +  
        np.roll(b, 1, 1)  
    )
    return vecindario


def paso(b):
    v = vecindario(b)
    buffer_b = b.copy() 
    for i in range(buffer_b.shape[0]):
        for j in range(buffer_b.shape[1]):
            if v[i, j] == 3 or (v[i, j] == 2 and buffer_b[i, j]):
                buffer_b[i, j] = 1
            else:
                buffer_b[i, j] = 0
    return buffer_b


GENERACIONES = 100
N = 25 # Dimensiones del tablero (N, M)
M = 40

pause = True

def onClick(event):
    global pause
    pause ^= True

# Construccion de tablero
tablero = np.zeros((N, M), dtype = int)

# CONDICIONES INICIALES (CASILLAS ENCENDIDAS)
# Figura inicial de células vivas en el centro de la pantalla
centro_x, centro_y = N // 2, M // 2
tam_figura = 5
tablero[centro_x - tam_figura//2: centro_x + tam_figura//2 + 1, centro_y - tam_figura//2: centro_y + tam_figura//2 + 1] = 1

def randomize(event):
    for i in range(N):
        for j in range(M):
            tablero[i, j] = random.randint(0, 1)
            tablero[i,j] = random.randint(0,tablero[i,j])
            tablero[i,j] = random.randint(0,tablero[i,j])
    global b
    b = tablero.copy()
    imagen.set_data(b)

fig, ax = plt.subplots(figsize=(4, 4))
plt.subplots_adjust(bottom=0.15)

# Major ticks
ax.set_xticks([])  # Eliminar ticks del eje x
ax.set_yticks([])  # Eliminar ticks del eje y

# Labels for major ticks
ax.set_yticklabels([])  # Eliminar etiquetas del eje y

# Minor ticks
ax.set_xticks([], minor=True)  # Eliminar ticks menores del eje x
ax.set_yticks([], minor=True)  # Eliminar ticks menores del eje y

b = tablero 
imagen = ax.imshow(b, interpolation="none", aspect = "equal", cmap=cm.gray_r)

def animate(i):
    global b

    if not pause: 
        b = paso(b) 
        
        imagen.set_data(b)
    
    return imagen,

# Botones inicio/pausa, randomizar
pause_ax = fig.add_axes((0.3, 0.025, 0.23, 0.04), anchor='SE')
pause_button = Button(pause_ax, 'Inicio/Pausa', hovercolor='0.975')
pause_button.on_clicked(onClick)

random_ax = fig.add_axes((0.6, 0.025, 0.3, 0.04), anchor='SW')
random_button = Button(random_ax, 'Randomizar', hovercolor='0.975')
random_button.on_clicked(randomize)

# Animacion 
anim = animation.FuncAnimation(fig, animate, frames=GENERACIONES, blit=True, interval = 200, repeat = True)
plt.show()
