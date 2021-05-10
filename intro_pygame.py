import pygame

#ajustacion de pantalla + titulo
tittle = "Juego1"
size = [400, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption(tittle)

clock = pygame.time.Clock()
FPS = 60
#Guardamos la paleta de colores a utilizar.....
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
#game loop

gameover = False

width = 10
height = 10
x_coord = 200
y_coord = 280
des_x = 0
des_y = 0
vel = 2

#parametros oponente

#x_opo =

def dibujarPersonaje(x,y,color, screen, w, h):
	pygame.draw.rect(screen,color, (x,y,w*6,h))

while not gameover:
	#recorremos lista de eventos
	for event in pygame.event.get():
			#si hacemos click en cerrar (x)
		if event.type == pygame.QUIT:
			gameover = True
		elif event.type == pygame.KEYDOWN:
			#if event.key == pygame.K_UP:
			#	des_y = -vel
			#elif event.key == pygame.K_DOWN:
			#	des_y = vel
			if event.key == pygame.K_LEFT:
				des_x = -vel
			elif event.key == pygame.K_RIGHT:
				des_x = vel

			#if event.key == pygame.K_a:
				#des_x = -vel
			#elif event.key == pygame.K.d:
				#des_x = vel

		elif event.type == pygame.KEYUP:
			#if event.key == pygame.K_UP:
			#	des_y = 0
			#elif event.key == pygame.K_DOWN:
			#	des_y = 0
			if event.key == pygame.K_LEFT:
				des_x = 0
			elif event.key == pygame.K_RIGHT:
				des_x = 0

			#if event.key == pygame.K_a:
				#des_x = 0
			#elif event.key == pygame.K_d:
				#des_x = 0



	#ejecutar accion
	x_coord = x_coord + des_x
	y_coord = y_coord + des_y
	screen.fill(white)
	dibujarPersonaje(x_coord, y_coord, black, screen, width, height)
	#dibujarPersonaje(x_coord_opo, y_coord_opo, black, screen, width, height)
	pygame.display.flip()
	clock.tick(FPS)
pygame.quit()