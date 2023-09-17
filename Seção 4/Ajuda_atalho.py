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
        elif keyboard.is_pressed('ctrl+alt+s'): #adicionar codigo
            posicao_atual = pg.position()
            pg.click(x=260, y=80)
            pg.moveTo(posicao_atual)
        elif keyboard.is_pressed('ctrl+alt+a'):
            posicao_atual = pg.position()
            pg.click(x=430, y=85)
            pg.moveTo(posicao_atual)
        elif keyboard.is_pressed('ctrl+alt+d'):
            posicao_atual = pg.position()
            pg.click(x=327, y=84)
            pg.moveTo(posicao_atual)




        # Durma brevemente para evitar alto uso da CPU
        time.sleep(0.05)

if __name__ == "__main__":
    check_key_combination()