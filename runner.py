from services import *
import time
import eel


get_qrcode()
eel.init("web")
eel.start("main.html", size=(1450, 1000))