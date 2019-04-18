import sympy


def mdc_ext(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        x, y, d = mdc_ext(b, a % b)
        return [y, x - (a // b) * y, d]


def mdc(phi):
    current = 0
    e = -1
    while current != 1:
        previous = phi
        current = sympy.randprime(2, 40)
        rest = previous % current
        e = current
        while rest != 0:
            previous = current
            current = rest
            rest = previous % current

    return e


class Rsa:
    def __init__(self, publicKey=[], privateKey=[]):
        self.publicKey = publicKey
        self.privateKey = privateKey

    def setup(self, publicKey=[], privateKey=[]):
        if publicKey == [] and privateKey == []:
            publicKey, privateKey = self.generateKey()
            self.__init__(publicKey, privateKey)
        else:
            self.privateKey = privateKey
            self.publicKey = publicKey
        return self.publicKey

    def generateKey(self):
        p = sympy.randprime(10, 100)
        q = sympy.randprime(10, 100)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = mdc(phi)

        d, a, b = mdc_ext(e, phi)

        if d < 0:
            d = d % phi
            d += phi

        return [n, e], [n, d]

    def encrypt(self, text, publicKey):
        message = ""
        for i in range(len(text)):
            message += chr((ord(text[i]) ** publicKey[1]) % publicKey[0])
        print(message)
        return message

    def decrypt(self, text):
        message = ""
        print(self.privateKey)
        for i in range(len(text)):
            message += chr((ord(text[i]) ** self.privateKey[1]) % self.privateKey[0])
        print(message)
        return message
