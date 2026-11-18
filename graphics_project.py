"""
Creating Graphics with Python
=============================
Name      : Daniyal Umar
Intern ID : ZYNVEX-CERT-2119
Project   : Creating Graphics with Python

Generates six different graphics with NumPy, Matplotlib and Pillow and saves
them to the ./output folder, plus one combined gallery image.

Run:  python graphics_project.py
"""
import math
import os

import matplotlib
matplotlib.use("Agg")                      # draw without opening a window
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

OUT = "output"
os.makedirs(OUT, exist_ok=True)

NAME, INTERN_ID, PROJECT = "Daniyal Umar", "ZYNVEX-CERT-2119", "Creating Graphics with Python"


def get_font(size, bold=True):
    """Use the DejaVu font that ships with Matplotlib (works on any computer)."""
    fname = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    path = os.path.join(matplotlib.get_data_path(), "fonts", "ttf", fname)
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


# ---------------------------------------------------------------- 1. Scene (Pillow)
def draw_scene(path=f"{OUT}/1_scene.png", w=900, h=600):
    """A landscape built only from basic shapes: gradient sky, sun, mountains, house, trees."""
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)

    # gradient sky: one coloured line per row
    top, bottom = np.array([25, 60, 140]), np.array([255, 190, 120])
    for y in range(h):
        t = y / h
        d.line([(0, y), (w, y)], fill=tuple((top * (1 - t) + bottom * t).astype(int)))

    d.ellipse([650, 70, 770, 190], fill=(255, 236, 140))                    # sun
    d.polygon([(0, 420), (180, 190), (360, 420)], fill=(88, 96, 120))        # mountains
    d.polygon([(220, 420), (430, 150), (640, 420)], fill=(70, 78, 105))
    d.polygon([(520, 420), (700, 240), (900, 420)], fill=(104, 112, 135))
    d.polygon([(430, 150), (400, 195), (430, 185), (455, 200)], fill=(240, 244, 250))  # snow cap
    d.rectangle([0, 400, w, h], fill=(52, 128, 70))                          # ground
    d.rectangle([0, 470, w, h], fill=(44, 112, 62))

    d.rectangle([330, 380, 520, 520], fill=(196, 80, 64))                    # house body
    d.polygon([(310, 385), (425, 300), (540, 385)], fill=(96, 52, 40))       # roof
    d.rectangle([405, 440, 450, 520], fill=(70, 42, 30))                     # door
    d.rectangle([350, 410, 390, 450], fill=(255, 238, 170))                  # windows
    d.rectangle([465, 410, 505, 450], fill=(255, 238, 170))

    for x in (130, 220, 650, 760):                                           # trees
        d.rectangle([x - 8, 440, x + 8, 520], fill=(92, 60, 36))
        d.ellipse([x - 45, 360, x + 45, 460], fill=(30, 96, 50))
    img.save(path)
    return path


# ---------------------------------------------------------------- 2. Spirograph (Matplotlib)
def draw_spirograph(path=f"{OUT}/2_spirograph.png"):
    """Hypotrochoid curves with different parameters layered in different colours."""
    fig, ax = plt.subplots(figsize=(7, 7), facecolor="black")
    t = np.linspace(0, 2 * np.pi * 20, 6000)
    colors = plt.cm.cool(np.linspace(0, 1, 5))
    for k, (R, r, dist) in enumerate([(10, 3, 5), (10, 4, 6), (10, 7, 4), (10, 9, 5), (10, 2, 7)]):
        x = (R - r) * np.cos(t) + dist * np.cos((R - r) / r * t)
        y = (R - r) * np.sin(t) - dist * np.sin((R - r) / r * t)
        ax.plot(x * (1 - 0.08 * k), y * (1 - 0.08 * k), color=colors[k], lw=0.7, alpha=0.9)
    ax.set_aspect("equal"); ax.axis("off")
    fig.savefig(path, dpi=120, facecolor="black", bbox_inches="tight")
    plt.close(fig)
    return path


# ---------------------------------------------------------------- 3. Mandelbrot (NumPy)
def draw_mandelbrot(path=f"{OUT}/3_mandelbrot.png", w=900, h=600, max_iter=120):
    """The Mandelbrot fractal: colour = how fast each point escapes to infinity."""
    x = np.linspace(-2.2, 1.0, w)
    y = np.linspace(-1.2, 1.2, h)
    c = x[None, :] + 1j * y[:, None]
    z = np.zeros_like(c)
    escape = np.zeros(c.shape)
    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] ** 2 + c[mask]
        escape[mask & (np.abs(z) > 2)] = i
    escape[np.abs(z) <= 2] = 0
    fig = plt.figure(figsize=(9, 6), facecolor="black")
    plt.imshow(escape, cmap="magma", extent=[-2.2, 1.0, -1.2, 1.2])
    plt.axis("off")
    fig.savefig(path, dpi=100, facecolor="black", bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    return path


# ---------------------------------------------------------------- 4. Polar flower (Matplotlib)
def draw_flower(path=f"{OUT}/4_flower.png"):
    """Rose curves r = cos(k*theta) in polar coordinates, drawn as a layered flower."""
    fig = plt.figure(figsize=(7, 7), facecolor="#101020")
    ax = fig.add_subplot(111, projection="polar", facecolor="#101020")
    theta = np.linspace(0, 2 * np.pi, 2000)
    for k, col in zip([2, 3, 4, 5, 7], plt.cm.spring(np.linspace(0, 1, 5))):
        r = np.abs(np.cos(k * theta / 2)) * (1 + 0.15 * k)
        ax.fill(theta, r, color=col, alpha=0.35)
        ax.plot(theta, r, color=col, lw=1.2)
    ax.axis("off")
    fig.savefig(path, dpi=120, facecolor="#101020", bbox_inches="tight")
    plt.close(fig)
    return path


# ---------------------------------------------------------------- 5. Wave art (Matplotlib)
def draw_waves(path=f"{OUT}/5_waves.png"):
    """Stacked, shaded sine waves with a changing frequency and colour gradient."""
    fig, ax = plt.subplots(figsize=(9, 5), facecolor="#0b132b")
    ax.set_facecolor("#0b132b")
    x = np.linspace(0, 4 * np.pi, 800)
    n = 28
    colors = plt.cm.plasma(np.linspace(0.05, 0.95, n))
    for i in reversed(range(n)):                      # draw the back layers first
        y = np.sin(x * (1 + i * 0.05) + i * 0.3) * (0.5 + i * 0.02) + i * 0.55
        ax.fill_between(x, y, -3, color=colors[i] * np.array([0.55, 0.55, 0.55, 1]), zorder=n - i)
        ax.plot(x, y, color=colors[i], lw=1.6, zorder=n - i)
    ax.axis("off")
    fig.savefig(path, dpi=110, facecolor="#0b132b", bbox_inches="tight")
    plt.close(fig)
    return path


# ---------------------------------------------------------------- 6. Title banner (Pillow)
def draw_banner(path=f"{OUT}/6_banner.png", w=1000, h=420):
    """A project title card with the intern's details on a gradient with a circle pattern."""
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    c1, c2 = np.array([16, 24, 64]), np.array([110, 40, 150])
    for x in range(w):                                   # left-to-right gradient
        t = x / w
        d.line([(x, 0), (x, h)], fill=tuple((c1 * (1 - t) + c2 * t).astype(int)))
    for i in range(9):                                   # decorative concentric rings
        r = 20 + i * 20
        d.ellipse([w - 100 - r, h - 40 - r, w - 100 + r, h - 40 + r], outline=(255, 255, 255), width=2)
    d.rectangle([60, 70, 68, 340], fill=(255, 200, 80))  # accent bar
    d.text((95, 70), PROJECT, font=get_font(46), fill="white")
    d.text((95, 170), f"Name       :  {NAME}", font=get_font(30, False), fill=(235, 235, 250))
    d.text((95, 220), f"Intern ID  :  {INTERN_ID}", font=get_font(30, False), fill=(235, 235, 250))
    d.text((95, 290), "Python  |  NumPy  |  Matplotlib  |  Pillow", font=get_font(24, False), fill=(255, 200, 80))
    img.save(path)
    return path


# ---------------------------------------------------------------- Gallery
def make_gallery(paths, path=f"{OUT}/gallery.png"):
    """Combine every graphic into one 3 x 2 contact sheet."""
    fig, axes = plt.subplots(2, 3, figsize=(18, 9), facecolor="#1a1a1a")
    titles = ["1. Landscape scene", "2. Spirograph", "3. Mandelbrot fractal",
              "4. Polar flower", "5. Wave art", "6. Title banner"]
    for ax, p, title in zip(axes.ravel(), paths, titles):
        ax.imshow(Image.open(p)); ax.axis("off")
        ax.set_title(title, color="white", fontsize=14, pad=8)
    fig.suptitle(f"{PROJECT}  -  {NAME} ({INTERN_ID})", color="white", fontsize=18, y=0.99)
    plt.tight_layout()
    fig.savefig(path, dpi=80, facecolor="#1a1a1a")
    plt.close(fig)
    return path


if __name__ == "__main__":
    steps = [draw_scene, draw_spirograph, draw_mandelbrot, draw_flower, draw_waves, draw_banner]
    files = []
    for step in steps:
        files.append(step())
        print("Created", files[-1])
    print("Created", make_gallery(files))
