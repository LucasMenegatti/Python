import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def telhado():
    glBegin(GL_TRIANGLES)
    glColor(139/255,0,0) #Estou dividindo por 255, pois o argumento recebe valores de 0 a 1, e estou usando cores RGB que vão de 0 a 255
    glVertex2f(-2, 1)
    glVertex2f(0, 2.5)
    glVertex2f(2, 1)
    glEnd()

def parede():
    glBegin(GL_QUADS)
    glColor(240/255, 230/255, 140/255)
    glVertex2f(-2, 1)
    glVertex2f(2,  1)
    glVertex2f(2, -2)
    glVertex2f(-2, -2)
    glEnd()

def porta():
    glBegin(GL_QUADS)
    glColor(139/255, 69/255, 19/255)
    glVertex2f(-1.6, -2)
    glVertex2f(-1.6, 0)
    glVertex2f(-0.4, 0)
    glVertex2f(-0.4, -2)
    glEnd()

def janela():
    glBegin(GL_QUADS)
    glColor(72/255, 209/255, 204/255)
    glVertex2f(0.25, 0.25)
    glVertex2f(1.55, 0.25)
    glVertex2f(1.55, -1)
    glVertex2f(0.25, -1)
    glEnd()

def principal():
        pygame.init()
        tela = 800,600 #criando uma variável com o tamanho da tela
        pygame.display.set_mode(tela, DOUBLEBUF | OPENGL)
        gluPerspective(45, tela[0]/tela[1], 0.1, 50.0) 
        glTranslatef(0.0, 0.0, -10) #Afastando-se do objeto para poder vizualiza-lo

        while True: #criando um loop infinito
            for event in pygame.event.get(): #escuta eventos
                if event.type == pygame.QUIT: #caso o usuário aperte o X da janela
                    pygame.quit() #encerrando o pygame
                    quit() #saíndo
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Limpando a tela antes de desenhar o frame
            #Aqui começa o desenho das formas
            telhado()
            parede()
            porta()
            janela()
            pygame.display.flip() #Atualiza o conteúdo do display

principal() #chama a função principal