import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        # Inicialización de la clase base
        gr.sync_block.__init__(
            self,
            name='Promedios_de_tiempos',  # Nombre que aparecerá en GRC
            in_sig=[np.float32],  # Entrada de tipo float32
            out_sig=[np.float32, np.float32, np.float32, np.float32, np.float32]  # Salidas de tipo float32
        )
        self.acum_anterior = 0
        self.Ntotales = 0
        self.acum_anterior1 = 0
        self.acum_anterior2 = 0

    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Promedio de la señal
        y1 = output_items[1]  # Media cuadrática de la señal
        y2 = output_items[2]  # RMS de la señal
        y3 = output_items[3]  # Potencia promedio de la señal
        y4 = output_items[4]  # Desviación estándar de la señal

        # Cálculo del promedio
        N = len(x)
        self.Ntotales += N
        acumulado = self.acum_anterior + np.cumsum(x)
        self.acum_anterior = acumulado[-1]  # Último valor acumulado
        y0[:] = acumulado / self.Ntotales  # Promedio acumulado

        # Cálculo de la media cuadrática
        x2 = np.multiply(x, x)#
        acumulado1 = self.acum_anterior1 + np.cumsum(x2)
        self.acum_anterior1 = acumulado1[-1]  # Último valor acumulado
        y1[:] = acumulado1 / self.Ntotales  # Media cuadrática acumulada

        # Cálculo del RMS
        y2[:] = np.sqrt(y1)  # RMS = raíz cuadrada de la media cuadrática

        # Cálculo de la potencia promedio
        y3[:] = np.multiply(y2, y2)  # Potencia promedio = RMS^2

        # Cálculo de la desviación estándar
        x3 = np.multiply(x - y0, x - y0)  # (x - promedio)^2
        acumulado2 = self.acum_anterior2 + np.cumsum(x3)
        self.acum_anterior2 = acumulado2[-1]  # Último valor acumulado
        y4[:] = np.sqrt(acumulado2 / self.Ntotales)  # Desviación estándar

        # Retornamos el número de elementos procesados por salida
        return len(x)
