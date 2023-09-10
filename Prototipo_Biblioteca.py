import time
import keyboard

def check_key_combination():
    while True:
        # Verifique se as teclas Ctrl, Alt e M foram pressionadas simultaneamente
        if keyboard.is_pressed('ctrl+alt+m'):
            print('The Ctrl+Alt+M key combination was pressed.')
            break

        # Durma brevemente para evitar alto uso da CPU
        time.sleep(0.05)

if __name__ == "__main__":
    check_key_combination()