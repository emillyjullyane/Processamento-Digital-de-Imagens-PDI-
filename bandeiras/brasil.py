# -*- coding: utf-8 -*-
"""Bandeira do Brasil

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j_GDVS8-UlIMVvIw7P8yQNB22QmL6Jg0
"""

!pip install opencv-python-headless pillow matplotlib numpy

from PIL import ImageDraw

from IPython.display import display

def create_brazilian_flag(width):

  green = (0,155,58)
  yellow = (255,255,0)
  blue = (0,39,118)

  heigth = int((14 / 20) * width)
  losango_B = (20/24) * width
  losango_b = (20/27)* heigth
  circulo_diam = (2/4) * heigth

  flag = Image.new("RGB", (width, heigth), green)
  draw = ImageDraw.Draw(flag)

  centro_x = width / 2
  centro_y = heigth / 2

  coordenadas_L = [
      (centro_x, centro_y - losango_b / 2),
      (centro_x + losango_B / 2, centro_y),
      (centro_x, centro_y + losango_b / 2),
      (centro_x - losango_B / 2, centro_y),
  ]

  draw.polygon(coordenadas_L, fill = yellow)

  circle_top_left = (centro_x - circulo_diam / 2, centro_y - circulo_diam / 2)
  circle_bottom_right = (centro_x + circulo_diam / 2, centro_y + circulo_diam / 2)

  draw.ellipse([circle_top_left, circle_bottom_right], fill=(0, 39, 118))

  display(flag)
create_brazilian_flag(600)