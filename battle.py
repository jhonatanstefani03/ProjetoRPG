import time

from player import *
from monster import Goblin, Orc, Dragao, FinalBoss


# Substitua pelo nome correto do seu arquivo

def turno_batalha(jogador, monstro):
    print(f"\nA batalha contra {monstro.nome} começa! ⚔️")
    
    while jogador.hp > 0 and monstro.hp > 0:
        jogador.hp = jogador.hp_max
        print(f"\nHP do {jogador.nome}: {jogador.hp} | HP do {monstro.nome}: {monstro.hp}")
        print("Escolha sua ação:")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Curar")

        escolha = input("Digite sua escolha: ")
        time.sleep(1)
        if escolha == "1":
            print("\nEscolha o tipo de ataque:")
            print("1 - Ataque Básico")
            print("2 - Ataque Especial")
            tipo_ataque = input("Digite sua escolha: ")
            time.sleep(0.5)
            if tipo_ataque == "1":
                dano = jogador.atacar()
            elif tipo_ataque == "2":
                dano = jogador.usar_ataque_especial()
            time.sleep(1)
            monstro.hp -= dano
            print(f"{jogador.nome} causou {dano:.2f} de dano! HP do {monstro.nome}: {monstro.hp}")

        elif escolha == "2":
            defesa = jogador.defender()
            print(f"{jogador.nome} se defendeu, aumentando defesa para {defesa}!")
            time.sleep(1)

        elif escolha == "3":
             cura = jogador.curar()
             print(f"{jogador.nome} se curou, recuperando {cura:.2f} pontos de vida! HP atual: {jogador.hp}")
             time.sleep(1)
        if monstro.hp <= 0:
            print(f"\n{monstro.nome} foi derrotado! 🎉")
            print(jogador.restaurar_hp())  # Restaura o HP ao valor inicial
        
            break
        time.sleep(1)
        print(f"\nTurno do {monstro.nome}:")
        dano_monstro = monstro.atacar()
        jogador.hp -= dano_monstro
        print(f"{monstro.nome} atacou e causou {dano_monstro:.2f} de dano! HP do {jogador.nome}: {jogador.hp}")

        if jogador.hp <= 0:
            print(f"\n{jogador.nome} foi derrotado! 💀")
            break

        input("\nPressione ENTER para o próximo turno...")
        time.sleep(1)

def iniciar_jogo():
    print("\n🎮 Bem-vindo ao RPG de Turnos! 🎮")
    jogador = escolher_classe()

    inimigos = [Goblin(), Orc(), Dragao()]  # Agora usamos as classes de monstros!

    for inimigo in inimigos:
        turno_batalha(jogador, inimigo)
        if jogador.hp <= 0:
            print("\nGAME OVER! Tente novamente.")
            return

    print("\n🔥 O chefe final apareceu! É o Rei Demônio! 🔥")
    boss = FinalBoss()
    turno_batalha(jogador,boss)
    time.sleep(1)

    print("\n🏆 PARABÉNS! Você derrotou todos os inimigos e venceu o jogo! 🎉")



# Iniciar o jogo
iniciar_jogo()
