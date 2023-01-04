import ServerGet as server

class Controls:
    def __init__(self):
        self.forward = 'Forward'
        self.backward = 'Backward'
        self.left = 'Left'
        self.right = 'Right'

    def loop(self):
        pass

class ServerLink:
    def __init__(self,server):
        self.server = server
    def Get(self,request):
        response = server.Get(self.server,request)
        return response



link = ServerLink('https://TankController.charsarg.repl.co/commands')
response = link.Get({'request':'wheels'})
print(response)
