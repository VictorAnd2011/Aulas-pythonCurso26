#irei tentar simular um lançamento obliquo, desconsiderando a resistencia do ar
import math
import pygame
import pygame_gui

#inicia o sistema do pygame
pygame.init()

#defina largura, altura, cria a tela e o gerenciador da interface
largura = 1266
altura = 650
gerenciador = pygame_gui.UIManager((largura,altura))
tela = pygame.display.set_mode((largura,altura))

#coloca um título
pygame.display.set_caption('SIMULADOR DE LANÇAMENTO')

#cria um relógio para ser usado para limitar o fps e fazer os calculos físicos
relogio = pygame.time.Clock()

#cria cores que vão ser mais usadas
branco = (255,255,255)
preto = (20, 20, 25)
verde = (70, 200, 120)
vermelho = (255,0,0)

ativo = True

def funcaoLancamento(vx,v0y): #fórmulas para a posição
        x = x0 + vx*t
        y = y0 - v0y*t + 5*t**2 #sinais tão invertidos pois a contagem de pixels é de cima para baixo
        return x,y

def tela_func(x,y):
    dt = relogio.tick(60)/1000
    tela.fill(preto)
    pygame.draw.line(
        tela, #onde vai criar a linha
        verde, #a cor
        (0,500), #onde começa
        (1266,500), #onde termina
        2 #largura em px
    )

    tela.blit(texto_aviso,ct_aviso)
    
    for i, linha in enumerate(texto_info):
        if linha == '--- SIMULAÇÃO EM ANDAMENTO ---' or linha == '--- SIMULAÇÃO FINALIZADA ---' or linha == '--- SIMULAÇÃO DE LANÇAMENTO ---':
            linha_info = fonte_titulo.render(linha, True, verde)
            i += -1
        else:
            linha_info = fonte_info.render(linha, True, branco)
        tela.blit(linha_info, (35, (2+i) * 35))

    pygame.draw.lines(
        tela,
        branco,
        False,
        pontos,
        2
    )

    #cria um círculo
    pygame.draw.circle(
        tela,
        vermelho,
        (x,y), #onde está o circulo
        6 #raio
    )

    return dt





def objeto_lancado(v0,ang):
    global t,x,y, texto_info
    
    executando = True
    hmax = 0
    ang  = math.radians(ang) #angulo em rads
    cos = round(math.cos(ang),3) #cos do angulo
    sen = round(math.sin(ang),3) #sen do angulo
    vx = v0*cos #retorna a velocidade horizontal, que é constante
    v0y = v0*sen #retorna a velocidade vertical inicial, que é variável

    while executando:
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False, False
        t += dt
        vy = v0y - g*t
        x,y = funcaoLancamento(vx,v0y) #retorna a posição
        x_sim = x-100
        if y > y0:
            y = y0

        y_sim = round((y-500)*-1,1)

        texto_info = ('--- SIMULAÇÃO EM ANDAMENTO ---',
            f'A distancia atual é de: {x_sim:.2f}m',
            f'A altura atual é de: {y_sim:.2f}m',
            f'A velocidade vertical atual é de: {vy:.2f}m/s',
            f'O tempo atual é de: {t:.2f}s'
            )

        if y_sim > hmax:
            hmax = y_sim

                

        tela_func(x,y)

        pontos.append((x,y))
        

        pygame.display.flip()
        if round(y,1) >= y0 and t > 0.1:
            texto_info = ('--- SIMULAÇÃO FINALIZADA ---',
                        f'A distância máxima foi de: {x_sim:.2f}m',
                        f'A altura máxima foi de: {hmax:.2f}m',
                        f'A velocidade horinzontal foi de: {vx:.1f}m/s',
                        f'A velocidade vertical inicial foi de: {v0y:.1f}m/s',
                        f'O tempo de lançamento foi de: {t:.2f}s')
            
            
            
            while executando:
                tela_func(x,y)
                
                botao_iniciar.hide()
                select_ang.hide()
                selec_v.hide()
                botao_reiniciar.show()
                
                gerenciador.update(dt)
                gerenciador.draw_ui(tela)
                pygame.display.flip()

                
                
                for evento in pygame.event.get():
                    
                    if evento.type == pygame.QUIT:
                        return False, False

                    gerenciador.process_events(evento)
                    
                    if (evento.type == pygame_gui.UI_BUTTON_PRESSED and evento.ui_element == botao_reiniciar):
                        botao_iniciar.show()
                        select_ang.show()
                        selec_v.show()
                        botao_reiniciar.hide()
                        return False, True


selec_v = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect(900, 60, 300, 40),
        manager=gerenciador,
        placeholder_text="VELOCIDADE EM m/s"
    )

select_ang = pygame_gui.elements.UITextEntryLine(
    relative_rect=pygame.Rect(900, 120, 300, 40),
    manager=gerenciador,
    placeholder_text="ANGULO EM GRAUS"
)

botao_iniciar = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(900, 180, 200, 50),
    text="Iniciar lancamento",
    manager=gerenciador
)

botao_reiniciar = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect(900, 60, 200, 50),
    text='REINICIAR',
    manager=gerenciador
    )
botao_reiniciar.hide()


while ativo:

    
    t = 0 #tempo inicial
    x0 = 100 #posição horizontal do objeto inicial
    y0 = 500 #posição vertical do objeto inicial
    y = y0 
    x = x0
    v0 = 100 #velocidade inicial
    ang = 45 #angulo de lançamento
    g = 9.81

    fonte_titulo = pygame.font.Font(None,36)
    fonte_info = pygame.font.Font(None,20)

    ct_aviso = (633, 200)
    ct_info = (0,0)


    texto_aviso = fonte_titulo.render(
        '',
        False,
        branco
    )
    texto_info = ''



    pontos = [(x0,y0),(x,y)]



    



    #cria um loop, para que o programa continue rodando
    executando = True
    while executando:

        texto_info = ('--- SIMULAÇÃO DE LANÇAMENTO ---',)
        
        dt = tela_func(x0,y0)

        

        #verifica evento por evento
        for evento in pygame.event.get():
            #se o evento for sair, ele termina o loop e sai
            if evento.type == pygame.QUIT:

                executando = False
                ativo = False
                
            #recebe os eventos de botão
            gerenciador.process_events(evento)
            #se o evento for apertar o botão iniciar, ele começa o lançamento
            if (evento.type == pygame_gui.UI_BUTTON_PRESSED and evento.ui_element == botao_iniciar):
                while executando:
                    try:
                        v0 = float(selec_v.get_text().replace(',','.'))
                        ang = float(select_ang.get_text().replace(',','.'))

                        if v0 < 0:
                            texto_aviso = fonte_titulo.render(
                                'Velocidade negativa inválido!!!',
                                True,
                                vermelho
                            )
                            
                        elif ang > 90 or ang < 0:
                            texto_aviso = fonte_titulo.render(
                                'Ângulo inválido!!!',
                                True,
                                vermelho
                            )
                        
                            
                        else:
                            texto_aviso = fonte_titulo.render(
                                '',
                                False,
                                branco
                            )
                            ct_aviso = (0,0)
                            executando, ativo = objeto_lancado(v0,ang)

                    except ValueError:  
                        texto_aviso = fonte_titulo.render(
                            'Valores inválidos!!!',
                            True,
                            vermelho
                        )
                        

                    break
                        
                    
            
                    


        gerenciador.update(dt)
        gerenciador.draw_ui(tela)

        #atualiza a imagem
        pygame.display.flip()

pygame.quit()

