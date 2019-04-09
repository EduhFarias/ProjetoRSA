import sympy

#Cifração -------------------------------------------------------------

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
for i in range(5):
    a = ord(text[i])
    conv = (a ** e) % n
    print("O: %d, T: %d" %(a, conv))

#Cifração -------------------------------------------------------------

#Decifração -------------------------------------------------------------

# chave privada(d,n) d é o coeficiente para decifrar e n o conjunto, pode ser n ou p e q

#Decifração -------------------------------------------------------------