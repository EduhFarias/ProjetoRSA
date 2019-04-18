

class Client:
    def __init__(self, users=[]):
        self.users = users

    def addUser(self, newUser):
        self.users.append(newUser)

    def removeUser(self, user):
        for i in range(len(self.users)):
            if self.users[i] == user.name:
                self.users.remove(user)
                return

    def checkUser(self, name):
        for i in range(len(self.users)):
            if self.users[i].name == name:
                return True
        return False

    def closing(self, rsa):

        with open("dados.txt", "w", encoding="utf-8") as file:

            file.write("(" + str(rsa.publicKey[0]) + ", " + str(rsa.publicKey[1]) + ") ("
                       + str(rsa.privateKey[0]) + ", " + str(rsa.privateKey[1]) + ")\n")
            for i in range(len(self.users)):
                name = self.users[i].name
                password = self.users[i].password
                message = self.users[i].message

                name = rsa.encrypt(name, rsa.publicKey)
                password = rsa.encrypt(password, rsa.publicKey)
                message = rsa.encrypt(message, rsa.publicKey)
                file.write(name+"\n")
                file.write(password+"\n")
                file.write(message+"\n")
            file.flush()
            file.close()
