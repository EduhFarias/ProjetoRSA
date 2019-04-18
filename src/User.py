from Client import *
from Rsa import *

class User:
    def __init__(self, name="", password=""):
        self.name = name
        self.password = password
        self.message = "none"

    def createNewUser(self):
        print("Nome:")
        name = input()
        print("Senha:")
        password = input()
        self.__init__(name, password)


    def login(self, users):
        print("Nome:")
        name = input()
        print("Senha:")
        password = input()
        for i in range(len(users)):
            if users[i].name == name:
                if users[i].password == password:
                    print("Logado com sucesso!")
                    return users[i]
                else:
                    print("Senha incorreta!")
        print("Usuário/senha inválido!")
        return None

    def sendMessage(self, users):
        print("Para quem enviar:")
        name = input()

        client = Client()
        if client.checkUser(name):
            print("Digite a mensagem:")
            message = input()
            print("Digite a chave pública:")
            n, e = map(int, input().split(),)
            publicKey = [n, e]
            rsa = Rsa()
            message = rsa.encrypt(message, publicKey)
            for i in range(len(users)):
                if users[i].name == name:
                    users[i].message = message
                    break
        else:
            print("Usuário não encontrado")

    def readMessage(self):
        rsa = Rsa()
        print(self.message)
        #rsa.decrypt(self.message)
