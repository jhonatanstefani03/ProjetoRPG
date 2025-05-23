import time
import sys
import msvcrt
from player import *
from monster import Goblin, Orc, Esqueleto, Troll, FinalBoss

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


#FIM FUNÇAO MUSICA PYGAME----------------------------------------------------------------

#INTRODUÇÃO DO TURNO------------------------------------------------------------------
def turno_batalha(jogador, monstro):
    
    tocar_musica('musicas\\musica.mp3')
    digitar_texto(f"\nUm novo inimigo surge... 👀")
    digitar_texto(f"\nÉ o temido {monstro.nome}!")
    digitar_texto(f"\n{monstro.nome} diz: \"{monstro.frase_entrada()}\"")

    while jogador.hp > 0 and monstro.hp > 0:
 #TURNO DO JOGADOR !!!--------------------------------------------------------------------       
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
                if random.random() < 0.15:  # adiciona 15% de chance de errar
                    digitar_texto(f"{jogador.nome} diz: \"{jogador.frase_erro()}\"")
                    dano = 0
                else:
                    digitar_texto(f"{jogador.nome} diz: \"{jogador.frase_ataque()}\"")
                    dano = jogador.atacar() - monstro.defesa

            elif tipo_ataque == "2":
                if random.random() < 0.20:  # 20% de chance de errar especial
                    print(f"{jogador.nome} tentou usar {jogador.ataque_especial}, mas...")
                    print(f"{jogador.nome} diz: \"{jogador.frase_erro()}\"")
                    dano = 0
                else:
                    print(f"{jogador.nome} usou {jogador.ataque_especial}!")
                    dano = jogador.usar_ataque_especial()

            monstro.hp -= dano
            print(f"{jogador.nome} causou {dano:.2f} de dano! HP do {monstro.nome}: {monstro.hp}")
            if dano > 0:
                print(f"{monstro.nome} reage: \"{monstro.frase_dano()}\"")

        elif escolha == "2":
            frase = jogador.frase_defesa()
            defesa = jogador.defender()
            print(f"{jogador.nome} diz: \"{frase}\"")
            print(f"{jogador.nome} se defendeu, aumentando defesa para {defesa}!")

        elif escolha == "3":
            frase = jogador.frase_cura()
            jogador.curar()
            print(f"{jogador.nome} diz: \"{frase}\"")
            print(f"{jogador.nome} se curou! HP atual: {jogador.hp}")

        if monstro.hp <= 0:
            jogador.hp =jogador.hp_max
            trocar_musica('musicas\\vitoria.mp3')
            digitar_texto(f"\n{monstro.nome} foi derrotado! 🎉")
            print(f"{monstro.nome} diz: \"{monstro.frase_derrota()}\"")
            input("Pressione ENTER para continuar...")
            print(jogador.restaurar_hp())  # Restaura o HP ao valor inicial
            trocar_musica("musicas\\musica.mp3")
            break
#TURNO DO MONSTRO -------------------------------------------------------------------------
        time.sleep(1)
        digitar_texto(f"\nTurno do {monstro.nome}:")
        if random.random() < 0.15:
            print(f"{monstro.nome} diz: \"{monstro.frase_erro()}\"")
            dano_monstro = 0
        else:
            frase = monstro.frase_ataque()
            digitar_texto(f"{monstro.nome} diz: \"{frase}\"")
            dano_monstro = monstro.atacar() - jogador.defesa

        jogador.hp -= dano_monstro
        print(f"{monstro.nome} causou {dano_monstro:.2f} de dano! HP do {jogador.nome}: {jogador.hp}")
        if dano_monstro > 0:
            print(f"{jogador.nome} reage: \"{jogador.frase_dano()}\"")
#---------------------------------------------------------------------------------
#JOGADOR  DERROTADO!!----------------------------------------------------------
        if jogador.hp <= 0:
            print(f"\n{jogador.nome} foi derrotado! 💀")
            print(f"{jogador.nome} diz: \"{jogador.frase_derrota()}\"")
            break
        jogador.defesa = jogador.defesa_base
#-----------------------------------------------------------------
#BOTAO DE TURNO--------------------------------------------------
        input("\nPressione ENTER para o próximo turno...")
#-----------------------------------------------------------------

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
    digitar_texto(f'\n🎙️ Narrador Maluco:')
    digitar_texto('“Aê, meu filho! Estamos sendo\natacados por criaturas\ninimagináveis. E você! Um novato,')
    digitar_texto( '\nnoob, nível 0, da ralé... Cof, cof...\nBem, quer dizer, todo o Reino')
    digitar_texto ('\nacredita que você é o escolhido\npara nos salvar.\nPortanto, sem delongas,')
    digitar_texto('\nescolha sua classe e vai pro fight!”')
    escolha()

def escolha():
    escolha = input("Digite '1' para começar, '2' para creditos ou 'sair' para deixar a aventura: ").strip().lower()
    
    if escolha == "1":
        iniciar_jogo()
        parar_musica()
    elif escolha == "2":
        creditos()
       #return introducao()
    else:
       digitar_texto("\n👋 Adeus, viajante! Que sua jornada um dia recomece!")
       parar_musica()


def creditos():
    digitar_texto('"Este jogo foi produzido com muito carinho, cafeína e dedicação pela equipe, esperamos que aproveitem!"\n')
    digitar_texto('Creditos:\n')
    digitar_texto('Jhonatan Stefani da Silva\n' \
    'Hernando José de Souza Neto\n' \
    'Márcio Lisley Brito Pereira\n' \
    'Renato Andrade Bastos\n' \
    'Thuani Sampaio da Silva')
    digitar_texto('e não menos importantes... Google, YouTube e o glorioso ChatGPT\n')
    return escolha()


def iniciar_jogo():
    digitar_texto("\n🎮 Bem-vindo ao RPG de Turnos! 🎮")
    jogador = escolher_classe()

    digitar_texto(f'\n🎙️ Narrador Maluco:')
    digitar_texto(
        f'“Ah, maravilha. O destino do Reino nas mãos de um acéfalo {jogador.nome}... AHAHAH cof, cof, digo... corajoso soldado.”')
    time.sleep(1.2)
    digitar_texto(
        '\n“Fica tranquilo que não é nenhum soulslike, jovem, o tutorial é básico mesmo! O tempo para aprender é sempre curto...')
    digitar_texto(
        'em compensação, os requisitos para qualificação mínima pra esse estágio seriam 12 anos de experiência na NASA')
    digitar_texto('e mestrado em Necromancia Quântica aplicada à pancadaria...”')
    digitar_texto('aproveita então que tamo te dando essa chance de aprendizado prático!!')
    digitar_texto(
        '\n“Mas olha... a tarefa é árdua, o monstro é feio, o chão é escorregadio e a taxa de sucesso é de 3%')
    digitar_texto('(sem garantia, nem que venha com o Celso Russomanno).')
    digitar_texto('Portanto...\nportanto... TE VIRAAAA!”')
    digitar_texto('\n💨 *POOF!*')

    ####### **INTRODUÇÃO NOVA: Escolha de Caminho** ####
    digitar_texto("\n💨 Você foi teletransportado para uma bifurcação muito curiosa...")
    digitar_texto("“Ó o drama, hein! 2 caminhos... 2 escolhas... 2 tipos de sofrimento.”")
    digitar_texto("“Mas escolhe com sabedoria, hein? Cada rota tem seus próprios 'presentinhos'...”")

    digitar_texto(
        "\n 1. Floresta verde e úmida,\ncom cogumelos esquisitos,\nfolhas no bolso e monstros no arbusto.\n🌲 Lar de Goblins agricultores e Orcs marombas.")
    digitar_texto(
        "\n 2. Deserto amarelo,\nfrita no sol e toma porrada de miragem.\n🏜️ Lar de Esqueletos Coachs e Trolls do Wifi ruim.")

    caminho = input("\nEscolha seu caminho (1 - Floresta, 2 - Deserto): ").strip()

    if caminho == "1":
        inimigos = [Goblin(), Orc()]
        digitar_texto("\n🌲 Você adentra a floresta escura... Sons estranhos ecoam entre as árvores.")
    elif caminho == "2":
        inimigos = [Esqueleto(), Troll()]
        digitar_texto("\n🏜️ Você caminha pelas dunas escaldantes do deserto... Algo se move sob a areia.")
    else:
        digitar_texto("🚫 Caminho inválido! Você tropeça e volta para casa. ☠️")
        return

    for inimigo in inimigos:
        turno_batalha(jogador, inimigo)
        if jogador.hp <= 0:
            digitar_texto("\nGAME OVER! Tente novamente.")
            return
    trocar_musica('musicas\\finalboss.mp3')
    digitar_texto("\n🔥 O chefe final apareceu! É o ERROR-9090! 🔥")
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




