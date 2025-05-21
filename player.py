import random

class Player:
    def __init__(self,nome,ataque,defesa,cura, hp):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.cura = cura
        self.hp = hp
        self.hp_max = hp
        
    def atacar(self):
        frase = self.frase_ataque()  # Obtém a frase aleatória da classe específica
        
        return self.ataque

    def frase_ataque(self):
        return "Ataque realizado!"

    def defender(self):
        defesa_total = self.defesa * 1.2  # Defesa aumentada em 20% ao ativar
        return f"{self.nome} se defendeu, reduzindo o dano em {defesa_total:.2f}!"

    def curar(self):
        vida_recuperada = self.cura * 2
        self.hp += vida_recuperada
          # Atualiza o HP do jogador
        
        if self.hp > self.hp_max:
            self.hp = self.hp_max
        print(f"DEBUG: {self.nome} curou {vida_recuperada:.2f}. HP atualizado para {self.hp:.2f}")
        

    def restaurar_hp(self):
        self.hp = self.hp  # Restaura o HP ao valor inicial
        return f"{self.nome} recuperou todo o HP após vencer a batalha! 💖"


class Mago(Player):
    def __init__(self):
        super().__init__(nome='Mago',ataque=10, defesa=5, cura=8, hp=50)
        self.ataque_especial = 'bola de fogo'

      
    def frase_ataque(self):
        frases_mago = [
            "\nSinta o poder do meu... cajadão!",
            "\nAbracadabra! Ou era Abacatebraba... enfim, toma!",
            " \nUé, funcionou? FUNCIONOU! Anota aí, primeiro sucesso da carreira!"
        ]
        print(random.choice(frases_mago))

    def usar_ataque_especial(self):
        dano_especial = self.ataque * 3
        print("🔥 Magia suprema ativada! 🔥")
        return dano_especial
    






class Guerreiro(Player):
    def __init__(self ):
        super().__init__(nome='Guerreiro',ataque=12, defesa=8, cura=5, hp=60)
        self.ataque_especial = "Golpe Poderoso"

     
    def frase_ataque(self):
        frases_guerreiro = [
             "BOOOM! ISSO que eu chamo de aperto de mão!",
             "Derrubei? Hmmm… pensei que fosse mais forte.",
              "Tá sentindo esse cheiro? É cheiro de vitória (ou queimado, sei lá)."
        ]
        print(random.choice(frases_guerreiro))

    def usar_ataque_especial(self):
        dano_especial = self.ataque * 2
        print("⚔️ Espada Flamejante em ação! ⚔️")
        return dano_especial


        

def escolher_classe():
    print("Escolha sua classe:")
    print("1 - Mago 🪄")
    print("2 - Guerreiro ⚔️")
    
    escolha = input("Digite o número correspondente à sua classe: ")
    
    if escolha == "1":
        return Mago()
    elif escolha == "2":
        return Guerreiro()
    else:
        print("Escolha inválida! Tente novamente.")
        return escolher_classe()
