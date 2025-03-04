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