import sys

def inverter(numero):
    resultado = 0
    while numero > 0:
        resultado = resultado * 10 + (numero % 10)
        numero //= 10
    return resultado

def resolver_inversao(A, B):
    MAX_VALOR = 10001 
    
    distancias = [-1] * MAX_VALOR
    visitado = [False] * MAX_VALOR
    
    fila = [0] * MAX_VALOR 

    inicio = 0
    fim = 0

    fila[fim] = A
    fim += 1
    
    visitado[A] = True
    distancias[A] = 0

    while inicio < fim:
        numero_atual = fila[inicio]
        inicio += 1 

        if numero_atual == B:
            return distancias[B]

        proximo_somar_um = numero_atual + 1

        if proximo_somar_um < MAX_VALOR and not visitado[proximo_somar_um]:
            fila[fim] = proximo_somar_um
            fim += 1 
            visitado[proximo_somar_um] = True 
            distancias[proximo_somar_um] = distancias[numero_atual] + 1
        
        proximo_inverter = inverter(numero_atual)
    
        if proximo_inverter < MAX_VALOR and not visitado[proximo_inverter]:
            fila[fim] = proximo_inverter
            fim += 1 
            visitado[proximo_inverter] = True 
            distancias[proximo_inverter] = distancias[numero_atual] + 1 
            
    return -1 

def main():
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            A, B = map(int, sys.stdin.readline().split())
            print(resolver_inversao(A, B))
    except (IOError, ValueError):
        pass

if __name__ == '__main__':
    main()
