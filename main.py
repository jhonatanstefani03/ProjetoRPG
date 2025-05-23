import pygame
import sys

# from battle import introducao
#
# if __name__ == "__main__":
#     introducao()

def menu_visual():
    pygame.init()
    pygame.mixer.init()
    largura, altura = 800, 600
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Mini-RPG")

    # Inicia música no menu
    pygame.mixer.music.load("musicas/musica.mp3")
    pygame.mixer.music.play(-1)

    fundo = pygame.image.load("imagens/fundo_menu.jpg").convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    # Letreiro em destaque com fundo escurecido
    letreiro = pygame.image.load("imagens/letreiro.png").convert_alpha()
    letreiro = pygame.transform.scale(letreiro, (480, 120))
    letreiro_rect = letreiro.get_rect(center=(largura // 2, 110))  # mais acima
    fundo_letreiro = pygame.Surface((500, 130), pygame.SRCALPHA)
    fundo_letreiro.fill((0, 0, 0, 120))  # RGBA, alpha 120 = semi-transparente

    botao_normal = pygame.image.load("imagens/Botao - start.png").convert_alpha()
    botao_hover = pygame.image.load("imagens/Botao - start_hover.png").convert_alpha()
    botao_normal = pygame.transform.scale(botao_normal, (200, 60))
    botao_hover = pygame.transform.scale(botao_hover, (200, 60))
    botao_rect = botao_normal.get_rect(center=(largura // 2, 500))

    som_clique = pygame.mixer.Sound("musicas/click.wav")

    clock = pygame.time.Clock()
    rodando = True
    while rodando:
        tela.blit(fundo, (0, 0))
        tela.blit(fundo_letreiro, (letreiro_rect.left - 10, letreiro_rect.top - 5))
        tela.blit(letreiro, letreiro_rect.topleft)

        mouse_pos = pygame.mouse.get_pos()
        mouse_hover = botao_rect.collidepoint(mouse_pos)
        tela.blit(botao_hover if mouse_hover else botao_normal, botao_rect.topleft)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN and mouse_hover:
                som_clique.play()
                pygame.time.wait(200)
                # Transição sem fechar pygame
                cena_intro_com_narrador(tela)
                return

        pygame.display.update()
        clock.tick(60)


def cena_intro_com_narrador(tela):
    largura, altura = 800, 600

    fundo = pygame.image.load("imagens/fundo_menu.jpg").convert()
    fundo = pygame.transform.scale(fundo, (largura, altura))

    narrador = pygame.image.load("imagens/Narrador maluco.png").convert_alpha()
    narrador = pygame.transform.scale(narrador, (220, 220))

    fonte = pygame.font.SysFont("arial", 20)
    fonte_pequena = pygame.font.SysFont("arial", 16, italic=True)

    falas = [
        "🎙️ Narrador Maluco:",
        "“Aê, meu filho! Estamos sendo atacados por criaturas inimagináveis!”",
        "“E você! Um novato, noob, nível 0... da ralé.”",
        "“Bem... todo o Reino acredita que você é o escolhido para nos salvar.”",
        "“Portanto, sem delongas... escolha sua classe e vai pro fight!”"
    ]

    indice_fala = 0
    texto_renderizado = ""
    clock = pygame.time.Clock()

    narrador_x = 850
    narrador_final_x = 560

    tempo_digito = pygame.time.get_ticks()
    velocidade = 30

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if len(texto_renderizado) >= len(falas[indice_fala]):
                    indice_fala += 1
                    texto_renderizado = ""
                    tempo_digito = pygame.time.get_ticks()
                    if indice_fala >= len(falas):
                        from battle import iniciar_jogo
                        iniciar_jogo()
                        return

        tela.blit(fundo, (0, 0))

        if narrador_x > narrador_final_x:
            narrador_x -= 8
        else:
            narrador_x = narrador_final_x
        tela.blit(narrador, (narrador_x, 360))

        # Balão de fala: volta ao tamanho padrão
        pygame.draw.rect(tela, (255, 255, 255), (40, 310, 520, 160))
        pygame.draw.rect(tela, (0, 0, 0), (40, 310, 520, 160), 4)

        if indice_fala < len(falas):
            atual = falas[indice_fala]
            agora = pygame.time.get_ticks()
            num_chars = (agora - tempo_digito) // velocidade
            texto_renderizado = atual[:num_chars]
            render = renderizar_texto_multilinha(texto_renderizado, fonte, 500)
            for i, linha in enumerate(render):
                tela.blit(linha, (60, 340 + i * 25))

        # Texto de instrução: agora centralizado dentro do balão
        texto_clique = fonte_pequena.render("Clique para continuar...", True, (80, 80, 80))
        texto_rect = texto_clique.get_rect(center=(40 + 520 // 2, 310 + 160 - 20))
        tela.blit(texto_clique, texto_rect.topleft)

        pygame.display.update()
        clock.tick(60)


def renderizar_texto_multilinha(texto, fonte, largura_max):
    palavras = texto.split(" ")
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        teste = linha_atual + palavra + " "
        if fonte.size(teste)[0] <= largura_max:
            linha_atual = teste
        else:
            linhas.append(fonte.render(linha_atual.strip(), True, (0, 0, 0)))
            linha_atual = palavra + " "
    linhas.append(fonte.render(linha_atual.strip(), True, (0, 0, 0)))
    return linhas


if __name__ == "__main__":
    menu_visual()
