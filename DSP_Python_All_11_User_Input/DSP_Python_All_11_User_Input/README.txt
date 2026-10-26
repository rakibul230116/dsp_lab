DSP Sessional - All 11 Python Programs (User Input)
===================================================

Programs included:
lab1.py  - Sample a continuous-time sine wave to obtain discrete-time samples
lab2.py  - Addition of signals
lab3.py  - Sample-by-sample multiplication of signals
lab4.py  - Amplitude scaling
lab5.py  - Even and odd components
lab6.py  - Linear convolution
lab7.py  - Deconvolution
lab8.py  - Circular convolution: circle/shifting method
lab9.py  - Circular convolution: matrix method
lab10.py - Fourier series approximation (square/sawtooth/triangle)
lab11.py - Discrete Fourier Transform (DFT)

Install dependencies once:
    python -m pip install numpy matplotlib

Run an individual file:
    python lab1.py
    python lab2.py
    ...
    python lab11.py

All programs request the needed values from the user in the terminal.
Plots appear for visualizing the signals.

Notes:
- The requested book PDF was not available in the chat/library when this ZIP
  was prepared. These programs use standard DSP formulas and methods.
- Problem 10 is implemented as a Fourier-series approximation for common
  periodic waveforms.
- Problem 11 is implemented as the Discrete Fourier Transform (DFT), a
  sampled/discrete form of the Fourier transform commonly used in DSP labs.
- Problem 05 samples must be entered in order n=-M,...,0,...,+M and N must
  be odd.
- Problem 08 and 09 require both input sequences to have equal length.
- Problem 07 assumes y is a linear convolution result and h[0] is non-zero.
