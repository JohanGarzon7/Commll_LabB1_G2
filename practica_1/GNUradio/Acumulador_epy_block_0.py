import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Promedios_de_tiempos',
            in_sig=[np.float32],
            out_sig=[np.float32, np.float32, np.float32, np.float32, np.float32]
        )
        self.sum_x = 0.0       # Acumulador de la señal
        self.sum_x2 = 0.0      # Acumulador de la señal al cuadrado
        self.Ntotales = 0      # Número total de muestras

    def work(self, input_items, output_items):
        x = input_items[0]   # Señal de entrada
        y0 = output_items[0] # Media
        y1 = output_items[1] # Media cuadrática
        y2 = output_items[2] # RMS
        y3 = output_items[3] # Potencia promedio
        y4 = output_items[4] # Desviación estándar

        N = len(x)

        # Actualizar acumuladores
        self.sum_x += np.sum(x)
        self.sum_x2 += np.sum(x**2)
        self.Ntotales += N

        # Media
        mean = self.sum_x / self.Ntotales
        y0[:] = mean

        # Media cuadrática (mean of squares)
        mean_square = self.sum_x2 / self.Ntotales
        y1[:] = mean_square

        # RMS
        rms = np.sqrt(mean_square)
        y2[:] = rms

        # Potencia promedio (idéntica a mean_square para señales reales)
        y3[:] = mean_square

        # Desviación estándar
        variance = mean_square - mean**2
        std_dev = np.sqrt(variance)
        y4[:] = std_dev

        return len(x)
