import eel
class GUI:
    @eel.expose
    def __init__(self):
        eel.init("../kiqpo/native")
        eel.start("index.html")


x = GUI()
