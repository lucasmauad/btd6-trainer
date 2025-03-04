import pyautogui as pg
import time as t
import keyboard as k

f12_pressed = False
posi_inicial = [870, 925]
seta_de_voltar_os_mapas = [270, 425] 
map = [1408, 617] 
facil = [662, 408] 
deflation = [1265, 445] 
ok = [964, 755] 
village = [1582, 651] 
upgrade_100 = [324, 494]
upgrade_001 = [324, 808] 
upgrade_010 = [324, 665]
up_100L = [1552, 490]
up_010L = [1547, 632]
up_001L = [1545, 779]
sniper = [1533, 583]
alch = [1605, 562]
proxima = [985, 915]
home = [712, 871]
bot_mira = [1425, 370]


def quebra():
    """Interrompe o processo e retorna à tela inicial."""
    k.press('esc')
    t.sleep(0.1)
    k.release('esc')
    t.sleep(0.3)
    pg.click(1067, 860)
    t.sleep(0.5)
    pg.click(1081, 706)
    t.sleep(0.8)
    k.press('esc')
    t.sleep(0.1)
    k.release('esc')
    t.sleep(0.4)
    pg.click(838, 856)


def up_tower(b):
    """Caso queira upar um boneco muda aqui"""
    match b:
        case 1: #dart monkey
            pg.click([832, 380])
            k.press_and_release('q')
            t.sleep(0.4)
            for i in range(2):
                pg.click([832, 380])
                t.sleep(0.4)
                
            for i in range(4): 
                pg.click(up_001L)
                t.sleep(0.1)
            
            for i in range(2):
                pg.click(up_010L)
                t.sleep(0.1)
                
        case 2: #dartling gunner
            pg.click([832, 380])
            k.press_and_release('m')
            t.sleep(0.4)
            for i in range(2):
                pg.click([832, 380])
                t.sleep(0.3)
            
            for i in range(2):
                pg.click(up_100L)
                t.sleep(0.1)
                
            for i in range(2):
                pg.click(up_010L)
                t.sleep(0.1)
            
            t.sleep(0.2)
            k.press_and_release('tab')
            t.sleep(0.5)
            pg.mouseDown(bot_mira)
            t.sleep(0.3)
            pg.mouseUp(bot_mira)
            t.sleep(0.5)
            pg.click([250, 770])
            t.sleep(0.3)
        
        case 3:#ice monkey
            pg.click([832, 380])
            k.press_and_release('t')
            t.sleep(0.4)
            for i in range(2):
                pg.click([832, 380])
                t.sleep(0.4)
                
            for i in range(4): 
                pg.click(up_100L)
                t.sleep(0.1)
            
            for i in range(2): 
                pg.click(up_010L)
                t.sleep(0.1)
            
            
        case _:
            return
                   

def main_loop(up = 0):
    """Executa a automação do jogo até que seja interrompida."""
    global f12_pressed  # Permite modificar a variável global

    while f12_pressed:
        i = 0

        pg.click(posi_inicial)
        t.sleep(1)
        for _ in range(2):
            pg.click(seta_de_voltar_os_mapas)
            t.sleep(1)

        pg.click(map)
        t.sleep(1)
        pg.click(facil)
        t.sleep(1)
        pg.click(deflation)
        t.sleep(3)
        pg.click(ok)
        t.sleep(0.5)

        pg.click(village)
        t.sleep(0.3)
        k.press_and_release('k')
        t.sleep(0.2)
        pg.click(village)
        t.sleep(0.1)
        pg.click(village)
        t.sleep(0.4)

        for _ in range(2):
            pg.click(upgrade_100)
            t.sleep(0.1)
            pg.click(upgrade_001)
            t.sleep(0.1)

        pg.click(sniper)
        t.sleep(0.1)
        k.press_and_release('z')
        t.sleep(0.5)
        pg.click(sniper)
        t.sleep(0.1)
        pg.click(sniper)
        t.sleep(0.4)

        for _ in range(2):
            pg.click(upgrade_010)
            t.sleep(0.1)

        for _ in range(4):
            pg.click(upgrade_001)
            t.sleep(0.1)

        pg.click(alch)
        t.sleep(0.1)
        k.press_and_release('f')
        t.sleep(0.5)
        pg.click(alch)
        t.sleep(0.2)
        pg.click(alch)
        t.sleep(0.4)

        for _ in range(4):
            pg.click(upgrade_100)
            t.sleep(0.1)

        pg.click(upgrade_001)
        t.sleep(0.3)

        if up != 0:
            up_tower(up)
            t.sleep(0.3)
        # Inicia o jogo
        for _ in range(2):
            k.press_and_release('space')
            t.sleep(0.2)

        while i <= 505:
            t.sleep(0.5)
            pg.click(ok)
            i += 1
            if k.read_key == 'f8': #Sai do loop e da função
                quebra()
                f12_pressed = False
                return  
            if k.read_key == 'f7': #Para o loop sem sair do mapa
                f12_pressed = False
                return

        pg.click(proxima)
        t.sleep(0.5)
        pg.click(home)
        t.sleep(5)


def start_bot(up = 0):
    """Gerencia o início e interrupção do script usando teclas de atalho."""
    global f12_pressed

    while True:
        if k.read_key() == 'f12':
            f12_pressed = True
            main_loop(up)
            
        if k.read_key() == 'f10':
            print(pg.position())
               

start_bot(3)