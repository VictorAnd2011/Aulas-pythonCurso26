import pygame
import pygame_gui

pygame.init()

largura = 500
altura = 600

gerenciador = pygame_gui.UIManager((largura,altura))
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

digitado = ''
fonte = pygame.font.Font(None, 36)

class Botoes:

    def __init__(self, val, x, y, tx, ty, gerenciador):
        self.val = val
        self.tecla = pygame_gui.elements.UIButton(
                    relative_rect=pygame.Rect(x,y,tx,ty),
                    text=val,
                    manager=gerenciador
                    )

    def digitando(self,digitado):
        if digitado == 'ERROR':
            digitado = ''
        
        if digitado != '':
            if self.val not in ['+','-']:
                digitado += self.val

            elif digitado[-1] not in ['+','-']:
                digitado += self.val
        else:
            if self.val not in ['+','*','/','**','.']:
                digitado += self.val
        return digitado

def calculo(digitado):
    try:
        digitado = eval(digitado)
        digitado = str(digitado)
        return digitado
    except (ValueError, SyntaxError, TypeError, ZeroDivisionError,NameError):
        return 'ERROR'
    




bot1 = Botoes('1',60,300,100,50,gerenciador)
bot2 = Botoes('2',160,300,100,50,gerenciador)
bot3 = Botoes('3',260,300,100,50,gerenciador)
bot4 = Botoes('4',60,350,100,50,gerenciador)
bot5 = Botoes('5',160,350,100,50,gerenciador)
bot6 = Botoes('6',260,350,100,50,gerenciador)
bot7 = Botoes('7',60,400,100,50,gerenciador)
bot8 = Botoes('8',160,400,100,50,gerenciador)
bot9 = Botoes('9',260,400,100,50,gerenciador)
bot0 = Botoes('0',60,450,100,50,gerenciador)
botPonto = Botoes('.',60,500,100,50,gerenciador)


botSoma = Botoes('+',160,450,100,50,gerenciador)
botSub = Botoes('-',260,450,100,50,gerenciador)
botMult = Botoes('*',360,300,100,50,gerenciador)
botDiv = Botoes('/',360,350,100,50,gerenciador)
botExp = Botoes('**',360,400,100,50,gerenciador)

botResult = Botoes('=',360,450,100,50,gerenciador)


teclas = {
    '1' : bot1,
    '2' : bot2,
    '3' : bot3,
    '4' : bot4,
    '5' : bot5,
    '6' : bot6,
    '7' : bot7,
    '8' : bot8,
    '9' : bot9,
    '0' : bot0,
    '.' : botPonto,
    '+' : botSoma,
    '-' : botSub,
    '*' : botMult,
    '/' : botDiv,
    '**' : botExp,
    '=' : botResult,
    }

executando = True

while executando:
    tela.fill((30,30,30))
    dt = relogio.tick(60) / 1000
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

        elif evento.type == pygame_gui.UI_BUTTON_PRESSED:
            for chave, valor in teclas.items():
                if valor.tecla == evento.ui_element:
                    botao = valor
                    break
                    
            if botao is not None and chave != '=':
                digitado = botao.digitando(digitado)
            else:
                digitado = calculo(digitado)
                

        gerenciador.process_events(evento)



    texto = fonte.render(
        digitado,
        False,
        (255, 255, 255)
        )
    retangulo_texto = texto.get_rect(
        midtop=(largura // 2, 50)
        )

    tela.blit(texto, retangulo_texto)
    


    
    gerenciador.update(dt)
    gerenciador.draw_ui(tela)
    pygame.display.flip()
    
pygame.quit()