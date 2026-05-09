import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def configurar_placa(N=50, M=50, temp_borde_superior=100.0):
    """
    Crea la placa inicial con condiciones de contorno fijas.
    Escenario sugerido por el profesor:
    - Placa 50x50
    - Borde superior a 100°C
    - Resto a 0°C
    """
    placa = np.zeros((N, M))
    placa[0, :] = temp_borde_superior  # borde superior caliente
    return placa


def paso_calor(placa, alpha=0.25):
    """
    Calcula un paso de tiempo usando diferencias finitas.
    alpha controla la velocidad de propagación (material).
    """
    nueva = placa.copy()

    nueva[1:-1, 1:-1] = (
        placa[0:-2, 1:-1] +
        placa[2:,   1:-1] +
        placa[1:-1, 0:-2] +
        placa[1:-1, 2:]
    ) * 0.25 * alpha + placa[1:-1, 1:-1] * (1 - alpha)

    return nueva


def simular(placa_inicial, alpha=0.25, max_iter=500, tolerancia=1e-3):
    """
    Ejecuta la simulación hasta convergencia o límite de iteraciones.
    """
    placa = placa_inicial.copy()
    historial = [placa.copy()]

    for _ in range(max_iter):
        nueva = paso_calor(placa, alpha)
        cambio = np.abs(nueva - placa).max()
        placa = nueva

        historial.append(placa.copy())

        if cambio < tolerancia:
            break

    return historial



def animar_simulacion(historial, titulo="Simulación de calor"):
    fig, ax = plt.subplots()
    img = ax.imshow(historial[0], cmap="hot", interpolation="nearest")
    ax.set_title(titulo)

    def actualizar(i):
        img.set_data(historial[i])
        return [img]

    ani = animation.FuncAnimation(fig, actualizar, frames=len(historial), interval=50)
    plt.show()

def comparar_materiales():
    """
    Compara dos materiales cambiando alpha:
    - Aluminio: alta conductividad → alpha = 0.30
    - Hierro: menor conductividad → alpha = 0.15
    """
    placa_base = configurar_placa()

    historial_al = simular(placa_base, alpha=0.30)
    historial_fe = simular(placa_base, alpha=0.15)

    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

    axs[0].imshow(historial_al[-1], cmap="hot")
    axs[0].set_title("Aluminio (rápida difusión)")

    axs[1].imshow(historial_fe[-1], cmap="hot")
    axs[1].set_title("Hierro (difusión lenta)")

    plt.show()

if __name__ == "__main__":
    placa = configurar_placa()

    historial = simular(placa)
    animar_simulacion(historial, titulo="Difusión de calor en placa 2D")

    comparar_materiales()
