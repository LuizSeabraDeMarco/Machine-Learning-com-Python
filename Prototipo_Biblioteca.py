import pynput.keyboard
import time

def on_press(key):
  print(key)

listener = pynput.keyboard.Listener(on_press=on_press)
listener.start()
time.sleep(60 * 10)

# Faça outras coisas aqui

listener.stop()
print('oi')