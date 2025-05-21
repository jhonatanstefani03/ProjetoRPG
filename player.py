class Player:
    def __init__(self,nome,ataque,defesa,cura, hp):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.cura = cura
        self.hp = hp
        self.hp_max = hp
        
    def atacar(self):
        return self.ataque

    def defender(self):
        defesa_total = self.defesa * 1.2  # Defesa aumentada em 20% ao ativar
        return f"{self.nome} se defendeu, reduzindo o dano em {defesa_total:.2f}!"

    def curar(self):
        vida_recuperada = self.cura * 1.5
        return vida_recuperada# Cura aumentada em 50%

    def restaurar_hp(self):
        self.hp = self.hp  # Restaura o HP ao valor inicial
        return f"{self.nome} recuperou todo o HP após vencer a batalha! 💖"


class Mago(Player):
    def __init__(self):
        super().__init__(nome='Mago',ataque=10, defesa=5, cura=8, hp=50)
        self.ataque_especial = 'bola de fogo'

      
    
    def usar_ataque_especial(self):
        dano_especial = self.ataque * 3
        print('dano Especial de fogo!!')# 30% a mais de dano
        return dano_especial





class Guerreiro(Player):
    def __init__(self ):
        super().__init__(nome='Guerreiro',ataque=12, defesa=8, cura=5, hp=60)
        self.ataque_especial = "Golpe Poderoso"

     
    

    def usar_ataque_especial(self):
        dano_especial = self.ataque * 2
        print('dano Especial Espada Flamejante!!')
        return dano_especial# 30% a mais de dano

        

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
