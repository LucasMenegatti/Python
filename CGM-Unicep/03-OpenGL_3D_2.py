import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices1 = (
    (1, -2, -1),
    (1, 0, -1),
    (-1, 0, -1),
    (-1, -2, -1),
    (1, -2, 1),
    (1, 0, 1),
    (-1, -2, 1),
    (-1, 0, 1)
    )

vertices2 = (
    (1, 0, -1),
    (1, 2, -1),
    (-1, 2, -1),
    (-1, 0, -1),
    (1, 0, 1),
    (1, 2, 1),
    (-1, 0, 1),
    (-1, 2, 1)
    )

bordas = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

superficies = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
)

def cubo(verticesAUsar, corCubo, corBordas):
    glBegin(GL_QUADS)
    for superficie in superficies:
        glColor3fv(corCubo)
        for vertice in superficie:
            glVertex3fv(verticesAUsar[vertice])
    glEnd()
    glBegin(GL_LINES)
    glColor3fv(corBordas)
    for borda in bordas:
        for vertice in borda:
            glVertex3fv(verticesAUsar[vertice])
    glEnd()

def principal():
        pygame.init()
        tela = 800,600 #criando uma variável com o tamanho da tela
        pygame.display.set_mode(tela, DOUBLEBUF | OPENGL)
        gluPerspective(90, tela[0]/tela[1], 0.1, 50.0) 
        glTranslatef(0, 0, -5) #Afastando-se do objeto para poder vizualiza-lo
        glRotatef(40,1,0,0) #Girando um pouco a tela para enxergar melhor os cubos (Eixo X)
        glRotatef(40,0,1,0) #Girando um pouco a tela para enxergar melhor os cubos (Eixo Y)

        while True: #criando um loop infinito
            for event in pygame.event.get(): #escuta eventos
                if event.type == pygame.QUIT: #caso o usuário aperte o X da janela
                    pygame.quit() #encerrando o pygame
                    quit() #saíndo
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #Limpando a tela antes de desenhar o frame
            #Aqui começa o desenho das formas
            cubo(vertices1, (72/255,61/255,139/255), (1,1,1))
            cubo(vertices2, (0/255,168/255,107/255), (1,1,1))
            pygame.display.flip() #Atualiza o conteúdo do display

principal() #chama a função principal
