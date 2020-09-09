from flexx import flx

class Example(flx.Widget):

    def init(self):
        flx.Button(text='hello')
        flx.Button(text='world')

app = flx.App(Example)
#app.launch('app')  # to run as a desktop app
app.launch('browser')  # to open in the browser
flx.run()  # mainloop will exit when the app is closed