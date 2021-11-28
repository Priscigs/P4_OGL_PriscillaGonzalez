# Universidad del Valle de Guatemala
# Priscilla González - 20689
# Proyecto 4 OGL - Gráficas

import pygame
from pygame.locals import *
import numpy as np
from gl import Renderer, Model
import shaders

width = 960
height = 540

deltaTime = 0.0

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
clock = pygame.time.Clock()

# Sound
pygame.mixer.music.load("sounds/ambient.mp3")
pygame.mixer.music.play(10)

rend = Renderer(screen)
rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)

# Lego
model3D = Model('models/legoToys.obj', 'textures/lego-tex.png')
model3D.position.z = -5
model3D.position.y = -1.5
rend.scene.append(model3D)
rend.pointLight.z = 1
model3D.scale.x = 0.06
model3D.scale.y = 0.06
model3D.scale.z = 0.06

isRunning = True
while isRunning:
    distance = ((rend.camPosition.x)**2 + (rend.camPosition.y)**2 + (rend.camPosition.z)**2)**0.5
    keys = pygame.key.get_pressed()

    # Traslacion de camara
    if keys[K_d]:
        rend.camPosition.x += 1 * deltaTime
    if keys[K_a]:
        rend.camPosition.x -= 1 * deltaTime
    if keys[K_w]:
        rend.camPosition.z += 1 * deltaTime
    if keys[K_s]:
        rend.camPosition.z -= 1 * deltaTime
    if keys[K_q]:
        rend.camPosition.y -= 1 * deltaTime
    if keys[K_e]:
        rend.camPosition.y += 1 * deltaTime

    # Zoom in and out
    if keys[K_n]:
        rend.camPosition += 0.01
    if keys[K_m]:
        rend.camPosition -= 0.01

    # Rotacion de camara
    if keys[K_z]:
        rend.camRotation.y += 15 * deltaTime
    if keys[K_x]:
        rend.camRotation.y -= 15 * deltaTime
    if keys[K_LEFT]:
        rend.left(rend.camRotation, 25 * deltaTime)
    if keys[K_RIGHT]:
        rend.right(rend.camPosition, 25 * deltaTime)

    # Movimiento de objeto
    rend.scene[0].rotation.y += 25 * deltaTime

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isRunning = False

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isRunning = False

            if ev.key == K_u:
                # Flor
                pygame.init()
                screen1 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )
                
                rend = Renderer(screen1)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                model3D = Model('models/PrimroseP.obj', 'textures/frog-tex.jpg')
                model3D.position.z = -5
                model3D.position.y = -0.5
                rend.scene.append(model3D)
                model3D.scale.x = 3
                model3D.scale.y = 3
                model3D.scale.z = 3

            if ev.key == K_i:
                # Planta
                pygame.init()
                screen2 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )

                rend = Renderer(screen2)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                model3D = Model('models/planta.obj', 'textures/plantaTex.jpg')
                model3D.position.z = -5
                model3D.position.y = -1.8
                rend.scene.append(model3D)
                rend.pointLight.x = -5
                rend.pointLight.y = 0
                rend.pointLight.z = -5
                model3D.scale.x = 8
                model3D.scale.y = 8
                model3D.scale.z = 8

            if ev.key == K_o:
                # Camera
                pygame.init()
                screen3 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )

                rend = Renderer(screen3)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                model3D = Model('models/Canon_AT-1.obj', 'textures/camTex.png')
                model3D.position.z = -5
                model3D.position.y = -0.8
                rend.scene.append(model3D)
                rend.pointLight.z = -5
                model3D.scale.x = 20
                model3D.scale.y = 20
                model3D.scale.z = 20

            if ev.key == K_p:
                # Rana
                pygame.init()
                screen4 = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.OPENGL )

                rend = Renderer(screen4)
                rend.setShaders(shaders.vertex_shader, shaders.fragment_shader)
                model3D = Model('models/Tree_frog.obj', 'textures/frog-tex.jpg')
                model3D.position.z = -10
                rend.scene.append(model3D)
                model3D.scale.x = 1
                model3D.scale.y = 1
                model3D.scale.z = 1

            # Shaders
            if ev.key == K_1:
                rend.filledMode()
            if ev.key == K_2:
                rend.wireframeMode()
            if ev.key == K_3:
                rend.setShaders(shaders.toon_vertex_shader, shaders.toon_fragment_shader)
            if ev.key == K_4:
                rend.setShaders(shaders.toon_vertex_shader, shaders.negative_fragment_shader)
            if ev.key == K_5:
                rend.setShaders(shaders.toon_vertex_shader, shaders.trigonometric_fragment_shader)
            if ev.key == K_6:
                rend.setShaders(shaders.toon_vertex_shader, shaders.rad_fragment_shader)
            if ev.key == K_7:
                rend.setShaders(shaders.toon_vertex_shader, shaders.flower_fragment_shader)
            
    rend.tiempo += deltaTime
    deltaTime = clock.tick(60) / 1000

    rend.render()

    pygame.display.flip()

pygame.quit()