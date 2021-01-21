from OpenGL.GL import *
from glew_wish import *
import glfw 
import random

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea ventana
    #independientemente del SO que usemos
    window = glfw.create_window(800,600,"Mi ventana", None, None)

    #configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #establecemos el contexto
    glfw.make_context_current(window)

    #activamos la validacion de 
    #funciones modernas de OpenGL
    glewExperimental = True

    #inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #obtener versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):

        c1= random.random()
        c2= random.random()
        c3= random.random()

        #establece region de dibujo
        glViewport(0,0,800,600)
        #Establece region de borrado
        glClearColor(c1,c2,c3,1)
        #borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #dibujar

        #preguntar si hubo entradas de perifericos
        #(Teclados, mouse, game pad, etc.)
        glfw.poll_events()
        #intercambia los buffers
        glfw.swap_buffers(window)

    #destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #termina los procesos que inicio glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()
