import cv2
import numpy as np

img = cv2.imread('Colores.png')

cv2.imshow('monstrar imagen OPENCV', img)

pixel =img[100,100]
print(pixel)

#rojo
'''color_bajo = (170,100,100)
color_alto = (179,255,255)'''

#verde
'''color_bajo = (60,100,100)
color_alto = (70,255,255)'''

#amarillo
color_bajo = (32,100,100)
color_alto = (22,209,252)

imagen_salida = img.copy()
imagen_salida_rgb = cv2.cvtColor(imagen_salida, cv2.COLOR_BGR2RGB)
imagen_salida_hsv = cv2.cvtColor(imagen_salida_rgb, cv2.COLOR_RGB2HSV)
mascara = cv2.inRange(imagen_salida_hsv, color_bajo, color_alto)
resultado = cv2.bitwise_and(imagen_salida, imagen_salida, mask=mascara)
cv2.imshow('PROCESADP POR OPENCV', mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()