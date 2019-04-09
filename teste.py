import sympy

#Cifração -------------------------------------------------------------
def main():
    p = sympy.randprime(10,100)
    q = sympy.randprime(10,100)
    n = p * q
    totiente = (p-1) * (q-1)

    print("P:%d, Q:%d, N:%d, TOTIENTE:%d" %(p, q, n, totiente))

    atual = 0
    e = -1
    while(atual != 1):
        ant = totiente
        atual = sympy.randprime(2,80)
        resto = ant % atual
        e = atual

        while(resto != 0):
            ant = atual
            atual = resto
            resto = ant % atual

    print("MDC(%d,%d) = %d" %(totiente, e, atual))
    publicKey = [totiente, e]

    text = "teste"
    saida = []
    for i in range(5):
        a = ord(text[i])
        conv = (a ** e) % n
        saida.append(conv)
        print("O: %d, T: %d" %(a, conv))

    o,p,d = xmdc(13,640)
    print(o,p,d)

    for i in range(5):
        conv = (saida[i] ** o) % n
        print(chr(conv))

#Cifração -------------------------------------------------------------

#Decifração -------------------------------------------------------------

# chave privada(d,n) d é o coeficiente para decifrar e n o conjunto, pode ser n ou p e q

def xmdc(a,b):
    if b==0:
        return [1,0,a]
    else:
        x,y,d=xmdc(b, a%b)
        return [y,x-(a//b)*y,d]

#Decifração -------------------------------------------------------------

if __name__ == '__main__':
    main()
