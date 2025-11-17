Lab 6 – Waveform: Modulación Digital
Raised Cosine, Root Raised Cosine, ISI & Pulse Shaping

Este repositorio contiene el desarrollo completo del Laboratorio 6 sobre conformación de pulsos (waveforming) en sistemas de comunicación digital, implementado en GNU Radio. El objetivo principal es analizar cómo los filtros de Coseno Alzado (Raised Cosine) y Raíz de Coseno Alzado (Root Raised Cosine) afectan el ancho de banda, la eficiencia espectral, la ISI (Intersímbolos) y la calidad del enlace bajo distintos esquemas de modulación y parámetros de roll-off.

Contenido del laboratorio

-Implementación de un transmisor digital con:

8-PSK

16-QAM

-Comparación entre:

Pulsos rectangulares (sin filtrado)

Raised Cosine (β = 0, 0.5, 1)

Root Raised Cosine (β = 0.5)

-Análisis de:

PSD (densidad espectral de potencia)

Diagramas de ojo

Constelaciones

Ancho de banda teórico vs medido

Efecto del ruido AWGN

Validación del criterio Nyquist ISI-free

Comparación RC vs RRC (transmisor vs matched filter)

-Herramientas utilizadas:

GNU Radio 3.x

Python (bloques auxiliares)

Ubuntu/Linux

Git & GitHub para control de versiones
