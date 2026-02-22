def potencia(a,b):
    if b ==0:
        return 1
    return a * potencia ( a. b-1)
def potencia_optimizado(a,b):
    if b==0:
        return 1
    if b%2 == 0:
        mitad = potencia_optimizado(a,b //2)
        return mitad*mitad
    else:
        return a* potencia_optimizado(a,b -1)
    
    #alg recursivo que yo le entregue un numnero y que sume los digitos hasta ese numero
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
    
    def potencia_tail(a, b, acc=1):
        if b == 0:
            return acc
        return potencia_tail(a, b - 1, a * acc)