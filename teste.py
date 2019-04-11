import sympy
from Rsa import *

#Cifração -------------------------------------------------------------
def main():
    """print("0. Criar chaves\n1. Cifrar mensagem\n2. Decifrar mensagem\n3. Encerrar")
    choice = int(input())
    newKey = Rsa()
    while choice != 3:
        if choice == 0:
            newKey.setup()
            print(newKey.publicKey, newKey.privateKey)
        elif choice == 1:
            print("Mensagem a ser cifrada:")
            newKey.encrypt(input())
        elif choice == 2:
            newKey.decrypt()
        else:
            print("Encerrando..")
        print("0. Criar chaves\n1. Cifrar mensagem\n2. Decifrar mensagem\n3. Encerrar")
        choice = int(input())

    """
    p = sympy.randprime(10, 50)
    q = sympy.randprime(10, 50)
    n = p * q
    totiente = (p-1) * (q-1)

    print("P:%d, Q:%d, N:%d, TOTIENTE:%d" %(p, q, n, totiente))

    atual = 0
    e = -1
    while atual != 1:
        ant = totiente
        atual = sympy.randprime(2, 40)
        resto = ant % atual
        e = atual

        while resto != 0:
            ant = atual
            atual = resto
            resto = ant % atual

    print("MDC(%d,%d) = %d" %(totiente, e, atual))
    publicKey = [totiente, e]

    text = input()
    saida = []

    for i in range(len(text)):
        a = ord(text[i])
        conv = (a ** e) % n
        saida.append(conv)
        print("O: %d %c, T: %d %c" %(a, a, conv, conv))

    o, p, d = xmdc(e, totiente)
    print(o, p, d)

    for i in range(len(text)):
        if o < 0:
            o = o % totiente
            o += totiente
        conv = (saida[i] ** o) % n
        print(chr(conv), conv)

#Cifração -------------------------------------------------------------

#Decifração -------------------------------------------------------------

# chave privada(d,n) d é o coeficiente para decifrar e n o conjunto, pode ser n ou p e q


def xmdc(a, b):
    if b == 0:
        return [1, 0, a]
    else:
        x, y, d = xmdc(b, a % b)
        return [y, x - (a // b) * y, d]
#Decifração -------------------------------------------------------------

if __name__ == '__main__':
    main()
