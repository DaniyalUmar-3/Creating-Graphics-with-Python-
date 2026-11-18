# Creating Graphics with Python

**Name:** Daniyal Umar  
**Intern ID:** ZYNVEX-CERT-2119  
**Project:** Creating Graphics with Python

## About
A Python project that creates six different graphics from code, using NumPy, Matplotlib and Pillow, and combines them into one gallery image.

| # | Graphic | Library | Idea |
|---|---------|---------|------|
| 1 | Landscape scene | Pillow | Sky gradient, sun, mountains, house and trees drawn from basic shapes (lines, rectangles, ellipses, polygons) |
| 2 | Spirograph | Matplotlib | Parametric hypotrochoid curves layered in a colour gradient |
| 3 | Mandelbrot fractal | NumPy + Matplotlib | Complex-number iteration; colour shows how fast points escape |
| 4 | Polar flower | Matplotlib | Rose curves drawn in polar coordinates |
| 5 | Wave art | Matplotlib | Layered sine waves with different frequencies |
| 6 | Title banner | Pillow | Text, gradient background and circle pattern |

## How to run
```
pip install -r requirements.txt
python graphics_project.py
```
All images are saved in the `output/` folder, including `gallery.png` (all six together).

In Google Colab: upload `graphics_project.py`, then run `!python graphics_project.py`.

## Project structure
```
graphics_project.py   main script (one function per graphic)
requirements.txt      libraries needed
output/               generated images
```
