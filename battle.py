import time
import sys
from player import *
from monster import Goblin, Orc, Dragao, FinalBoss




def turno_batalha(jogador, monstro):
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
            digitar_texto(f"\n{monstro.nome} foi derrotado! 🎉")
            print(jogador.restaurar_hp())  # Restaura o HP ao valor inicial

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
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()


def introducao():
    digitar_texto('“Aê, meu filho! Estamos sendo\natacados por criaturas\ninimagináveis. E você! Um novato,')
    digitar_texto( '\nnoob, nível 0, da ralé... Cof, cof...\nBem, quer dizer, todo o Reino')
    digitar_texto ('\nacredita que você é o escolhido\npara nos salvar.\nPortanto, sem delongas,')
    digitar_texto('\nescolha sua classe e vai pro fight!”')

    escolha = input("Digite '1' para começar ou 'sair' para deixar a aventura: ").strip().lower()
    
    if escolha == "1":
        iniciar_jogo()
    else:
       digitar_texto("\n👋 Adeus, viajante! Que sua jornada um dia recomece!")





def iniciar_jogo():
    digitar_texto("\n🎮 Bem-vindo ao RPG de Turnos! 🎮")
    jogador = escolher_classe()

    inimigos = [Goblin(), Orc(), Dragao()]  # Agora usamos as classes de monstros!

    for inimigo in inimigos:
        turno_batalha(jogador, inimigo)
        if jogador.hp <= 0:
            digitar_texto("\nGAME OVER! Tente novamente.")
            return

    digitar_texto("\n🔥 O chefe final apareceu! É o Rei Demônio! 🔥")
    boss = FinalBoss()
    turno_batalha(jogador,boss)

    digitar_texto("\n🏆 PARABÉNS! Você derrotou todos os inimigos e venceu o jogo! 🎉")

introducao()




