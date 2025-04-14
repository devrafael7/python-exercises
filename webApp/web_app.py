import eel

eel.init('Gui')

@eel.expose
def App():
    print("App running!")

App()

eel.start('index.html', size=(600, 800))