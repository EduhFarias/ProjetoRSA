import sympy


def xmdc(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        x, y, d = xmdc(b, a % b)
        return [y, x - (a // b) * y, d]

class Rsa:

    def __init__(self):
        self.publicKey = []
        self.privateKey = []
        self.message = ""

    def setup(self): # setup(self, publicKey, privateKey)
        # Recebe tbm, publicKey e privateKey
        # Caso as chaves não estejam definidas elas serão criadas, em ambos os casos é retornado a chave publica
        # em forma de tupla para o usuario ----- Quebrar a funçao em duas, setup e generateKey
        p = sympy.randprime(10, 100)
        q = sympy.randprime(10, 100)
        n = p * q
        totient = (p - 1) * (q - 1)
        e = self.mdc(totient)

        d, p, o = xmdc(e, totient)
        print("-1 ", d)
        if d < 0:
            d = d % n
            d += n
            print("-2 ", d)
        self.publicKey = [n, e]
        self.privateKey = [n, d]

    def encrypt(self, text): #encrypt(self, text, publicKey)
        message = ""
        for i in range(len(text)):
            message += chr((ord(text[i]) ** self.publicKey[1]) % self.publicKey[0])
        self.message = message
        print(self.message)

    def decrypt(self):
        message = ""
        for i in range(len(self.message)):
            message += chr((ord(self.message[i]) ** self.privateKey[1]) % self.privateKey[0])
            print(ord(self.message[i]), ord(message[i]))
        print(message)

    def mdc(self, totient):
        atual = 0
        e = -1
        while atual != 1:
            ant = totient
            atual = sympy.randprime(2, 40)
            resto = ant % atual
            e = atual

            while resto != 0:
                ant = atual
                atual = resto
                resto = ant % atual

        return e

