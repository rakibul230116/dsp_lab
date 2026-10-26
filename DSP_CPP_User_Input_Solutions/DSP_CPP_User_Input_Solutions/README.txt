DSP Sessional C++ Solutions (Problems 02-09)
=============================================

IMPORTANT
---------
These programs accept user input from the terminal.
Problem 01, 10, and 11 are intentionally omitted.

Files
-----
lab2.cpp  - Addition of two signals
lab3.cpp  - Sample-by-sample multiplication of two signals
lab4.cpp  - Amplitude scaling
lab5.cpp  - Even and odd components
lab6.cpp  - Linear convolution
lab7.cpp  - Deconvolution (polynomial long division)
lab8.cpp  - Circular convolution, circle/shifting method
lab9.cpp  - Circular convolution, matrix method

Run in VS Code (Windows PowerShell)
-----------------------------------
1. Install a C++ compiler such as MinGW-w64 and make sure g++ is in PATH.
2. Open this folder in VS Code.
3. Open Terminal > New Terminal.
4. Compile one program, for example:
      g++ lab2.cpp -o lab2
5. Run it:
      .\lab2
6. Repeat with lab3.cpp through lab9.cpp.

Example inputs
--------------
lab2:
  N = 3
  x1 samples: 1 2 3
  x2 samples: 4 5 6
  output: 5 7 9

lab3:
  N = 3
  x1 samples: 1 2 3
  x2 samples: 4 5 6
  output: 4 10 18

lab4:
  N = 3, A = 2, x samples: 1 -2 3
  output: 2 -4 6

lab5:
  N = 5, x samples from n=-2 to n=2: 1 2 3 4 5
  even: 3 3 3 3 3
  odd: -2 -1 0 1 2

lab6:
  x: 1 2 3
  h: 1 1 1
  output: 1 3 6 5 3

lab7:
  y: 1 3 3 1
  h: 1 1
  recovered x: 1 2 1
  remainder should be zero (allowing small floating-point errors).

lab8 and lab9:
  N = 4
  x: 1 2 3 4
  h: 1 2 0 0
  output: 9 4 7 10

Notes
-----
- For Problem 05, samples must be entered in order n=-M,...,0,...,+M,
  so the number of samples must be odd.
- For circular convolution, both input signals must have equal length.
- For deconvolution, h[0] must not be zero. The program estimates x length
  as length(y) - length(h) + 1.
- The requested reference PDF (DSP_by_poornachandra_sasikala.pdf) was not
  available in the chat/library when this package was prepared. The programs
  use standard DSP definitions and methods; upload the PDF if exact matching
  with the book's notation/examples is required.
