# Práctica 4 - Modulación de M-PSK

Este proyecto corresponde al desarrollo de la **Práctica 4** del curso **Comunicaciones II**, centrada en la implementación y análisis de sistemas de modulación digital **M-PSK (Phase Shift Keying)** mediante la plataforma **GNU Radio**.

---

## Descripción

El objetivo de la práctica fue **analizar, representar y convertir señales de radiofrecuencia (RF)** a su **envolvente compleja (EC)**, comparando distintos esquemas de modulación digital:

- **OOK (On-Off Keying)**
- **BPSK (Binary Phase Shift Keying)**
- **QPSK (Quadrature PSK)**
- **8-PSK**, **16-PSK** y **32-PSK**

Se estudió el comportamiento de las señales moduladas en los dominios **temporal**, **frecuencial** y **de constelación**, aplicando la regla de los **–20 dB** para estimar el ancho de banda y relacionarlo con la tasa de símbolos.

---

## Metodología

- Simulación en **GNU Radio** bajo entorno **Linux**.  
- Implementación de transmisores digitales con bloques como `VCO`, `Vector Source`, `Complex Multiply` e `Interpolating FIR Filter`.  
- Visualización mediante los bloques `QT GUI Time Sink`, `QT GUI Frequency Sink` y `QT GUI Constellation Sink`.  
- Análisis de desempeño y robustez frente al **ruido gaussiano**.  
- Validación del modelo mediante **Vector Source** y **tablas de verdad**.

---

## Resultados

- **QPSK** presentó buena tolerancia al ruido y una eficiencia espectral equilibrada.  
- **8-PSK** y modulaciones de orden superior mostraron mayor sensibilidad al ruido.  
- Se comprobó la equivalencia entre fuentes aleatorias y vectores definidos, confirmando la reproducibilidad del modelo de modulación digital en GNU Radio.

