import time
import sys
import msvcrt
from player import *
from monster import Goblin, Orc, Dragao, FinalBoss

import pygame


#funçao MUSICAS PYGAME
def tocar_musica(caminho, repetir=False):
    pygame.mixer.init()
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play(-1 if repetir else 0)  # Se repetir=True, toca em loop

def parar_musica():

    pygame.mixer.music.stop()

def trocar_musica(nova_musica):
    parar_musica()  # Para a música atual
    tocar_musica(nova_musica, repetir=True)


#FIM FUNÇAO MUSICA PYGAME

def turno_batalha(jogador, monstro):
    tocar_musica('musicas\\musica.mp3')
    digitar_texto(f"\nA batalha contra {monstro.nome} começa! ⚔️")
    
    while jogador.hp > 0 and monstro.hp > 0:
        
        print(f"\nHP do {jogador.nome}: {jogador.hp} | HP do {monstro.nome}: {monstro.hp}")
        print("Escolha sua ação:")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Curar")

        escolha = input("Digite sua escolha: ")

        if escolha == "1":
            print("\nEscolha o tipo de ataque:")
            print("1 - Ataque Básico")
            print("2 - Ataque Especial")
            tipo_ataque = input("Digite sua escolha: ")

            if tipo_ataque == "1":
                dano = jogador.atacar()
            elif tipo_ataque == "2":
                dano = jogador.usar_ataque_especial()

            monstro.hp -= dano
            print(f"{jogador.nome} causou {dano:.2f} de dano! HP do {monstro.nome}: {monstro.hp}")

        elif escolha == "2":
            defesa = jogador.defender()
            print(f"{jogador.nome} se defendeu, aumentando defesa para {defesa}!")

        elif escolha == "3":
            jogador.curar()
            print(f"{jogador.nome} se curou, recuperando  pontos de vida! HP atual: {jogador.hp}")

        if monstro.hp <= 0:
            jogador.hp =jogador.hp_max
            trocar_musica('musicas\\vitoria.mp3')
            digitar_texto(f"\n{monstro.nome} foi derrotado! 🎉")
            input("Pressione ENTER para continuar...")
            print(jogador.restaurar_hp())  # Restaura o HP ao valor inicial
            trocar_musica("musicas\\musica.mp3")
            break

        print(f"\nTurno do {monstro.nome}:")
        dano_monstro = monstro.atacar()
        jogador.hp -= dano_monstro
        print(f"{monstro.nome} atacou e causou {dano_monstro:.2f} de dano! HP do {jogador.nome}: {jogador.hp}")

        if jogador.hp <= 0:
            print(f"\n{jogador.nome} foi derrotado! 💀")
            break

        input("\nPressione ENTER para o próximo turno...")


def digitar_texto(texto, velocidade=0.05):
    for caractere in texto:
        if msvcrt.kbhit():  # Verifica se alguma tecla foi pressionada
            tecla = msvcrt.getch()
            if tecla == b'\r':  # ENTER foi pressionado
                print(texto)
                return


        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)

    print()


def introducao():
    tocar_musica('musicas\\musica.mp3')
    digitar_texto('“Aê, meu filho! Estamos sendo\natacados por criaturas\ninimagináveis. E você! Um novato,')
    digitar_texto( '\nnoob, nível 0, da ralé... Cof, cof...\nBem, quer dizer, todo o Reino')
    digitar_texto ('\nacredita que você é o escolhido\npara nos salvar.\nPortanto, sem delongas,')
    digitar_texto('\nescolha sua classe e vai pro fight!”')

    escolha = input("Digite '1' para começar ou 'sair' para deixar a aventura: ").strip().lower()
    
    if escolha == "1":
        iniciar_jogo()
        parar_musica()
    else:
       digitar_texto("\n👋 Adeus, viajante! Que sua jornada um dia recomece!")
       parar_musica()







def iniciar_jogo():
    digitar_texto("\n🎮 Bem-vindo ao RPG de Turnos! 🎮")
    jogador = escolher_classe()

    inimigos = [Goblin(), Orc(), Dragao()]  # Agora usamos as classes de monstros!

    for inimigo in inimigos:
        turno_batalha(jogador, inimigo)
        if jogador.hp <= 0:
            digitar_texto("\nGAME OVER! Tente novamente.")
            return
    trocar_musica('musicas\\finalboss.mp3')
    digitar_texto("\n🔥 O chefe final apareceu! É o Rei Demônio! 🔥")
    digitar_texto('\n🔥 O ar fica pesado. A temperatura parece mudar. 🔥')
    digitar_texto('\nO chão treme, e uma presença avassaladora emerge das sombras.')
    digitar_texto('\n“Você chegou longe demais, mortal...”')
    digitar_texto('\nUma voz profunda ecoa pelo ambiente, reverberando nos seus ossos.')
    digitar_texto('\nO Rei Demônio observa você com olhos chamejantes, um sorriso cruel se formando.')
    digitar_texto('\n“Pensei que cairia antes mesmo de chegar aqui. Mas vejo que tem algo especial.”')
    digitar_texto('\nEle ergue sua lâmina negra, envolta em energia sombria.')
    digitar_texto('\n“Agora vamos ver se você é digno do título de herói ou apenas mais um fracassado!”')
    digitar_texto('\n⚔️ Prepare-se! A luta final começa agora! ⚔️')

    boss = FinalBoss()
    turno_batalha(jogador,boss)
    if jogador.hp <= 0:
            digitar_texto("\nGAME OVER! Tente novamente.")
            return

    digitar_texto("\n🏆 PARABÉNS! Você derrotou todos os inimigos e venceu o jogo! 🎉")

introducao()




