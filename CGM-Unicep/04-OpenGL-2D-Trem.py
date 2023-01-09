# Aluno: Lucas Gentil Menegatti
# RA: 4201000

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

def cabine():
    glBegin(GL_QUADS)
    glColor(79/255, 79/255, 79/255) #Estou dividindo por 255, pois o argumento recebe valores de 0 a 1, e estou usando cores RGB que vão de 0 a 255
    glVertex2f(-4, 2)   # Cima Esquerda
    glVertex2f(-1, 2)   # Cima Direita
    glVertex2f(-1, -2)  # Baixo Direita
    glVertex2f(-4, -2)  # Baixo Esquerda
    glEnd()

def janela_cabine():
    glBegin(GL_QUADS)
    glColor(65/255, 105/255, 1)
    glVertex2f(-3.5, 1.5)   # Cima Esquerda
    glVertex2f(-1.5, 1.5)   # Cima Direita
    glVertex2f(-1.5, 0)  # Baixo Direita
    glVertex2f(-3.5, 0)  # Baixo Esquerda
    glEnd()

def teto_cabine():
    glBegin(GL_QUADS)
    glColor(178/255,34/255,34/255)
    glVertex2f(-4.25, 2.5)   # Cima Esquerda
    glVertex2f(-0.75, 2.5)   # Cima Direita
    glVertex2f(-0.75, 2)     # Baixo Direita
    glVertex2f(-4.25, 2)     # Baixo Esquerda
    glEnd()

def caldeira():
    glBegin(GL_QUADS)
    glColor(79/255, 79/255, 79/255)
    glVertex2f(-1, 0)   # Cima Esquerda
    glVertex2f(3, 0)   # Cima Direita
    glVertex2f(3, -2)     # Baixo Direita
    glVertex2f(-1, -2)     # Baixo Esquerda
    glEnd()

def chamine():
    glBegin(GL_QUADS)
    glColor(178/255,34/255,34/255)
    glVertex2f(1, 1.5)   # Cima Esquerda
    glVertex2f(2, 1.5)   # Cima Direita
    glVertex2f(2, 0)     # Baixo Direita
    glVertex2f(1, 0)     # Baixo Esquerda
    glEnd()

def limpatrilho():
    glBegin(GL_TRIANGLES)
    glColor(178/255,34/255,34/255)
    glVertex2f(3, -0.25)
    glVertex2f(4.5, -1.75)
    glVertex2f(3, -1.75)
    glEnd()

def roda(x,y):
    glColor(28/255, 28/255, 28/255)
    posx, posy = x,y
    lados = 30
    fator_escala = 1
    glBegin(GL_POLYGON)
    for i in range(100):
        cosine=cos(i*pi/lados)+posx
        sine=sin(i*pi/lados)+posy
        glVertex2f(cosine*fator_escala,sine*fator_escala)
    glEnd()


def principal():
        pygame.init()
        tela = 640,480 #criando uma variável com o tamanho da tela
        pygame.display.set_mode(tela, DOUBLEBUF | OPENGL)
        gluPerspective(45, tela[0]/tela[1], 0.1, 50.0) 
        glTranslatef(0.0, 0.0, -30) #Afastando-se do objeto para poder vizualiza-lo

        # B) Realizando o Escalonamento
        glScalef(1.5,1.5,0)
        # C) Movimentando para o segundo quadrante
        glTranslatef(-4.0,4.0,0.0)
        # D) Realizando a rotação de 45º
        glRotatef(45,0,0,1)

        while True: #criando um loop infinito
            for event in pygame.event.get(): #escuta eventos
                if event.type == pygame.QUIT: #caso o usuário aperte o X da janela
                    pygame.quit() #encerrando o pygame
                    quit() #saíndo
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Limpando a tela antes de desenhar o frame
            #Aqui começa o desenho das formas
            cabine()
            janela_cabine()
            teto_cabine()
            caldeira()
            chamine()
            limpatrilho()
            roda(-2.5,-2)
            roda(0,-2)
            roda(2,-2)

            pygame.display.flip() #Atualiza o conteúdo do display

principal() #chama a função principal