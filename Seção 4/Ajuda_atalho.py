import time
import keyboard
import pyautogui as pg


def check_key_combination():
    while True:
        # Verifique se as teclas Ctrl, Alt e M foram pressionadas simultaneamente
        if keyboard.is_pressed('ctrl+alt+m'):
            print('The Ctrl+Alt+M key combination was pressed.')
            print('FIM')
            break
        elif keyboard.is_pressed('ctrl+s'): # more code
            posicao_atual = pg.position()
            pg.click(x=930, y=270)
            pg.moveTo(posicao_atual)
        elif keyboard.is_pressed('ctrl+d'): #more text
            posicao_atual = pg.position()
            pg.click(x=1076, y=253)
            pg.moveTo(posicao_atual)
        elif keyboard.is_pressed('ctrl+alt+n'): #run all
            posicao_atual = pg.position()
            pg.click(x=1324, y=269)
            pg.moveTo(posicao_atual)




        # Durma brevemente para evitar alto uso da CPU
        time.sleep(0.05)

if __name__ == "__main__":
    check_key_combination()