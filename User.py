

class User:
    name = ""
    password = ""
    messages = []
    accepted = False

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def createNewUser(self):
        print("Nome:")
        name = input()
        print("Senha:")
        password = input()
        self.__init__(name, password)
