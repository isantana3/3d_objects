import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import time

lista = []
tour = 0.0
modo = ""


def read_txt(name):
    global lista
    arquivo = open(name, 'r')
    linha = arquivo.readlines()
    for i in range(1, len(linha)):
        x, y, z = linha[i].split('     ')
        coordenada = [float(x), float(y), float(z)]
        lista.append(coordenada)
    arquivo.close()


def draw_object():
    global lista
    global modo
    if modo == "solid":
        glBegin(GL_POLYGON)
    else:
        glBegin(GL_POLYGON_BIT)
    glColor4f(0.0, 1.0, 1.0, 0.1)
    for i in range(0, len(lista)):
        glVertex3f(lista[i][0], lista[i][1], lista[i][2])
    glEnd()


def eixo_xy():
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-200, 0)
    glVertex2f(200, 0)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(0, -200)
    glVertex2f(0, 200)
    glEnd()


def iterate():
    glViewport(0, 0, 400, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-200.0, 200, -200.0, 200, -200.0, 200.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def show_screen():
    global lista
    global tour
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glEnable(GL_DEPTH_TEST)
    iterate()
    eixo_xy()
    tour += 3

    glLoadIdentity()
    glRotated(tour, 2, 0.5, 1)
    glScaled(30, 30, 30)

    for i in range(0, len(lista)):
        draw_object()

    glutSwapBuffers()


def main():
    global modo
    escolha = input("Digite o nome do modelo 3D\n").lower()
    modo = input("Prefere wire ou solid?\n")

    try:
        if escolha[-4:-0] == ".txt":
            read_txt(escolha)
        else:
            read_txt(escolha + ".txt")

    except:
        print("Modelo não encontrado, divirta-se com a bola ^_^ ")
        read_txt("sphere.txt")

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(-200, -200)
    wind = glutCreateWindow("OpenGL")
    glutDisplayFunc(show_screen)
    glutIdleFunc(show_screen)
    glutMainLoop()


if __name__ == "__main__":
    main()
