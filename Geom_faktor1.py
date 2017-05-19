#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Geometricky faktor detektoru 

from random import random
import math

N = 1000000.0
b = 3.6  # Vzdálenost detekčních vrstev

k = 0.0
while k <= 180.0:  
  j = 0.0
  while j <= 90.0:
    pocet_zasahu = 0.0
    i = 0
    while i < N:
      alpha_1 = k / 180.0 * math.pi
      #alpha_1 = random() * 2 * math.pi # Úhel od osy X
      alpha_2 = j / 180.0 * math.pi
      # alpha_2 = math.acos(random() * 2 - 1)  # Úhel od osy Z
      x_1 = random() * 256 * 0.055  # Náhodná poloha v první vrstvě detektoru 
      y_1 = random() * 256 * 0.055  # Náhodná poloha v první vrstvě detektoru
      
      a = b * math.tan(alpha_2)
      a_x = a * math.cos(alpha_1)
      a_y = a * math.sin(alpha_1)
      x_2 = x_1 + a_x  # Poloha v druhé vrstvě detektoru
      y_2 = y_1 + a_y  # Poloha v druhé vrstvě detektoru
      
      if (x_2 >= 0 and x_2 <= 256 * 0.055) and (y_2 >= 0 and y_2 <= 256 * 0.055):
	pocet_zasahu += 1
      
      i += 1
    
    smerova_ucinnost = pocet_zasahu/N
    print j, smerova_ucinnost
    j += 1.0
  k += 1
  
