

# Subclasses de monstros com características únicas
class Monsters:
    def __init__(self, nome, dano, defesa, hp):
        self.nome = nome
        self.dano = dano
        self.defesa = defesa
        self.hp = hp

    def atacar(self):
        return self.dano

    def defender(self):
        return self.defesa * 1.1  # Defesa aumentada em 10%

class Goblin(Monsters):
    def __init__(self):
        super().__init__("Goblin", dano=8, defesa=4, hp=40)

class Orc(Monsters):
    def __init__(self):
        super().__init__("Orc", dano=12, defesa=6, hp=50)

class Dragao(Monsters):
    def __init__(self):
        super().__init__("Dragão", dano=20, defesa=10, hp=80)

class FinalBoss(Monsters):
    def __init__(self):
        super().__init__("Rei Demônio",dano=25, defesa=20,hp=100)

    def ataque_especial(self):
        self.dano = self.dano *1.3
