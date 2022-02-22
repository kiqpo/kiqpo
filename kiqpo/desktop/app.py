import eel
class GUI:
    @eel.expose
    def __init__(self):
        eel.init("./kiqpo/native")
        eel.start("")

@eel.expose
def save(file):
    open(file, 'x')


def main():
    GUI()
