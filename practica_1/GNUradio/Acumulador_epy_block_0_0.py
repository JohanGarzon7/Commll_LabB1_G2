from gnuradio import gr
import numpy as np

class blk(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Diferenciador',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        self.x_prev = 0.0  # Valor anterior de la entrada

    def work(self, input_items, output_items):
        x = input_items[0]   # Señal de entrada
        y = output_items[0]  # Señal de salida
        N = len(x)

        # Diferenciación discreta: y[n] = x[n] - x[n-1]
        y[0] = x[0] - self.x_prev
        y[1:] = np.diff(x)

        # Guardar último valor para la próxima llamada
        self.x_prev = x[-1]

        return len(y)