from User import *

def execute():
    file = open("dados.txt", "r")
    user = User()
    rsa = Rsa()
    publicKey, privateKey = getKey(file)
    rsa.setup(publicKey, privateKey)
    client = getUsers(file, rsa)

    while True:
        print("1. Login\n2. Criar novo usuário\n0. Encerrar")
        choice = int(input())
        if choice < 0 or choice > 2:
            print("Entrada inválida!")
        else:
            if choice == 1:
                user = user.login(client.users)
                if user is not None:
                    while True:
                        print("1. Ver valor da chave pública\n2. Enviar mensagem\n"
                              "3. Ver mensagem\n4. Excluir usuário\n0. Encerrar")
                        c = int(input())
                        if c == 1:
                            print(rsa.publicKey)
                        if c == 2:
                            user.sendMessage(client.users)
                        if c == 3:
                            user.readMessage()
                        if c == 4:
                            client.removeUser(user)
                            break
                        if c == 0:
                            break
                else:
                    user = User()

            elif choice == 2:
                newUser = User()
                newUser.createNewUser()
                client.users.append(newUser)
            else:
                client.closing(rsa)
                print("Encerrando...")
                break

def getKey(file):
    l = []
    line = file.readline()
    n = ""
    if len(line) > 0:
        for i in range(len(line)):
            if 48 <= ord(line[i]) <= 57:
                n += line[i]
            else:
                if n != "":
                    l.append(int(n))
                    n = ""
        return [l[0], l[1]], [l[2], l[3]]
    else:
        return [], []

def getUsers(file, rsa):
    client = Client()

    b = file.readlines()
    for i in range(0,len(b)-2, 3):
        name = b[0+i]
        password = b[1+i]
        message = b[2+i]
        name, password, message = txt(name, password, message)

        name = rsa.decrypt(name)
        password = rsa.decrypt(password)
        message = rsa.decrypt(message)

        newUser = User(name, password)
        newUser.message = message
        client.users.append(newUser)
    return client

def txt(name, password, message):
    name = name.replace(" ", "")
    name = name.replace("\n", "")
    password = password.replace(" ", "")
    password = password.replace("\n", "")
    message = message.replace(" ", "")
    message = message.replace("\n", "")
    return name, password, message