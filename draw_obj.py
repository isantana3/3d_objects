from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time, sys


def draw_cone(position=(0, -1, 0), radius=1, height=2, slices=50, stacks=10):
    '''Desenha um cone utilizinado o método glutSolidCone do glut como base'''
    glPushMatrix()
    try:
        glColor(0.8, 0.1, 0.2, 0.5)
        glTranslatef(*position)
        glRotatef(250, 1, 0, 0)
        glutSolidCone(radius, height, slices, stacks)
    finally:
        glPopMatrix()


def depth():
    """Setup depth testing"""
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)


def display(swap=1, clear=1):
    '''Display function onde ocorre toda a dinâmica e atualiação dos frames do vídeo'''

    if clear:
        glClearColor(0.2, 0.5, 0.8, 0.5)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # establish the projection matrix (perspective)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    x, y, width, height = glGetDoublev(GL_VIEWPORT)
    gluPerspective(
        45,  # field of view in degrees
        width / float(height or 1),  # aspect ratio
        0.25,  # near clipping plane
        200,  # far clipping plane
    )

    # and then the model view matrix
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(
        0,
        1,
        5,  # eyepoint
        0,
        0,
        0,  # center-of-view
        0,
        1,
        0,  # up-vector
    )
    depth()

    rotation()
    draw_cone()
    if swap:
        glutSwapBuffers()


def idle():
    glutPostRedisplay()


starttime = time.time()


def rotation(period=10):
    """Do rotation of the scene at given rate"""
    angle = (((time.time() - starttime) % period) / period) * 360
    glRotate(angle, 0, 1, 0)
    return angle


def main():
    print("""You should see a high-resolution cone rotating slowly.""")
    import sys

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow('Rotating Cone')
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
