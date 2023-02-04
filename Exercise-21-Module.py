# Exercicio resolvido por Cesar Augusto Numero 21 18/01/23
# Faça um programa que abra e reproduza o audio de arquivo MP3
# Acesse python.org - Acesse Pypi - Pesquisar por modulos MP3 - Instale o Modulo com PIP via Terminal

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
